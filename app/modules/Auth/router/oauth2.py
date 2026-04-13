from fastapi import Depends, APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.dependencies.dependencies import get_db
from app.modules.Auth.schema import schema
from app.modules.Auth.services.oauth2_service import OAuth2Service


router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login", response_model=schema.Token)
def login(
    cred: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    # Authenticate user
    user = OAuth2Service.authenticate_user(db, cred.username, cred.password)
    
    # Create access token
    access_token = OAuth2Service.create_access_token_for_user(user.id) # type: ignore
    
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

