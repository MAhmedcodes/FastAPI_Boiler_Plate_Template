from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from app.core.dependencies.dependencies import get_db
from app.core.security.OAuth2.oauth2 import current_user
from app.modules.Users.schema import schema
from app.modules.Users.services.user_service import UserService
from app.core.middleware.security_layer import limiter
from app.modules.Users.models import model

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/register", response_model=schema.RegisterResponse)
@limiter.limit("5/minute")
async def register(
    request: Request,
    user_data: schema.UserCreate,
    db: Session = Depends(get_db)
):
    """
    Register a new user with invite token

    - **email**: Valid email address
    - **first_name**: User's first name
    - **last_name**: User's last name
    - **password**: User's password (min 6 characters)
    - **invite_token**: Organization invite token
    """

    # Validate password length
    if len(user_data.password) < 6:  # type: ignore
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Password must be at least 6 characters"
        )

    # Validate email format (basic)
    if '@' not in user_data.email or '.' not in user_data.email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid email format"
        )

    # Validate required fields
    if not user_data.first_name or not user_data.last_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="First name and last name are required"
        )

    # Validate invite token
    if not user_data.invite_token:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invite token is required"
        )

    try:
        result = UserService.register_user(
            db=db,
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            password=user_data.password,  # type: ignore
            invite_token=user_data.invite_token
        )

        return schema.RegisterResponse(
            access_token=result["access_token"],
            token_type="bearer",
            user_id=result["user"].id,
            email=result["user"].email,
            first_name=result["user"].first_name,
            last_name=result["user"].last_name,
            organization_id=result["user"].organization_id,
            message="User registered successfully"
        )

    except HTTPException:
        # Re-raise HTTP exceptions from service
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Registration failed: {str(e)}"
        )


@router.get("/me", response_model=schema.CurrentUser)
def get_current_user(
    current_user: model.User = Depends(current_user),
    db: Session = Depends(get_db)
):
    """
    Get current logged-in user information

    Requires Bearer token in Authorization header
    """
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    return schema.CurrentUser(
        id=current_user.id,  # type: ignore
        email=current_user.email,  # type: ignore
        first_name=current_user.first_name,  # type: ignore
        last_name=current_user.last_name,  # type: ignore
        organization_id=current_user.organization_id  # type: ignore
    )


token_blacklist = set()


@router.post("/logout")
def logout(current_user: model.User = Depends(current_user)):
    """
    Logout user - revoke current token
    Note: For production, store blacklisted tokens in Redis
    """
    # For now, just return success
    # In production, you would add the token to a blacklist
    return {
        "message": "Successfully logged out",
        "user_id": current_user.id,
        "email": current_user.email
    }
