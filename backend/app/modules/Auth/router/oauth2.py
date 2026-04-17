from fastapi import Depends, APIRouter, Request, Form
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.dependencies.dependencies import get_db
from app.modules.Auth.schema import schema
from app.modules.Auth.services.oauth2_service import OAuth2Service
from app.core.middleware.security_layer import limiter

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/login", response_model=schema.Token)
@limiter.limit("5/minute")
def login(
    request: Request,
    cred: OAuth2PasswordRequestForm = Depends(),
    organization_id: int = Form(...),  # REQUIRED now
    db: Session = Depends(get_db)
):
    # Authenticate user with organization
    user = OAuth2Service.authenticate_user(
        db, cred.username, cred.password, organization_id)

    # Create access token with organization
    access_token = OAuth2Service.create_access_token_for_user(
        user.id, user.organization_id)  # type: ignore

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "organization_id": user.organization_id
    }
