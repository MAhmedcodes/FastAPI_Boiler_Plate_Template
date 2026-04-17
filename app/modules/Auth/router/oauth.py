from fastapi import Depends, HTTPException, Request, APIRouter
from sqlalchemy.orm import Session

from app.core.dependencies.dependencies import get_db
from app.modules.Auth.schema import schema
from app.core.security.OAuth.oauth import oauth
from app.core.config.config import settings
from app.modules.Auth.services.oauth_service import OAuthService
from app.modules.Auth.services.oauth2_service import OAuth2Service
from app.core.middleware.security_layer import limiter

router = APIRouter(prefix="/auth", tags=["Authentication"])

# Google OAuth


@router.get("/google/login")
@limiter.limit("10/minute")
async def google_login(
    request: Request,
    invite_token: str  # NEW: accept invite token
):
    redirect_uri = settings.google_redirect_uri
    # Pass invite_token as state parameter
    if invite_token:
        return await oauth.google.authorize_redirect(request, redirect_uri, state=invite_token)
    return await oauth.google.authorize_redirect(request, redirect_uri)


@router.get("/google/callback", response_model=schema.OAuthResponse)
@limiter.limit("10/minute")
async def google_callback(
    request: Request,
    state: str,  # This contains the invite_token
    db: Session = Depends(get_db)
):
    try:
        token = await oauth.google.authorize_access_token(request)
        user_info = token.get('userinfo')

        if not user_info:
            resp = await oauth.google.get('userinfo', token=token)
            user_info = resp.json()

        # Pass invite_token from state
        user = OAuthService.handle_google_oauth(
            db, user_info, invite_token=state)

        jwt_token = OAuth2Service.create_access_token_for_user(
            user.id, user.organization_id)  # type: ignore

        return schema.OAuthResponse(
            access_token=jwt_token,
            token_type="bearer",
            user_id=user.id,  # type: ignore

            email=user.email,  # type: ignore

            message="Google login successful"
        )

    except Exception as e:
        print(f"Google login error: {str(e)}")
        raise HTTPException(
            status_code=400, detail=f"Google login failed: {str(e)}")

# GitHub OAuth


@router.get("/github/login")
@limiter.limit("10/minute")
async def github_login(
    request: Request,
    invite_token: str  # NEW: accept invite token
):
    redirect_uri = settings.github_redirect_uri
    # Pass invite_token as state parameter
    if invite_token:
        return await oauth.github.authorize_redirect(request, redirect_uri, state=invite_token)
    return await oauth.github.authorize_redirect(request, redirect_uri)


@router.get("/github/callback", response_model=schema.OAuthResponse)
@limiter.limit("10/minute")
async def github_callback(
    request: Request,
    state: str,  # This contains the invite_token
    db: Session = Depends(get_db)
):
    try:
        token = await oauth.github.authorize_access_token(request)

        resp = await oauth.github.get('user', token=token)
        user_info = resp.json()

        email = user_info.get('email')
        if not email:
            resp_emails = await oauth.github.get('user/emails', token=token)
            emails = resp_emails.json()
            for e in emails:
                if e.get('primary') and e.get('verified'):
                    email = e.get('email')
                    break

        github_id = str(user_info.get('id'))

        if not email:
            raise HTTPException(
                status_code=400, detail="Could not get email from GitHub")

        # Pass invite_token from state
        user = OAuthService.handle_github_oauth(
            db, user_info, github_id, email, invite_token=state)

        jwt_token = OAuth2Service.create_access_token_for_user(
            user.id, user.organization_id)  # type: ignore

        return schema.OAuthResponse(
            access_token=jwt_token,
            token_type="bearer",
            user_id=user.id,  # type: ignore
            email=user.email,  # type: ignore

            message="GitHub login successful"
        )

    except Exception as e:
        print(f"github login error: {str(e)}")
        raise HTTPException(
            status_code=400, detail=f"github login failed: {str(e)}")
