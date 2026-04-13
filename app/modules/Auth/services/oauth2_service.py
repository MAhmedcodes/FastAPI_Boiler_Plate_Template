from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from shared.utils import utils
from app.core.security.OAuth2 import oauth2
from app.modules.Users.repository.user_repository import UserRepository

class OAuth2Service:
    
    @staticmethod
    def authenticate_user(db: Session, email: str, password: str):
        """Authenticate user with email and password"""
        user_repo = UserRepository(db)
        user = user_repo.get_by_email(email)
        
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid Email or Password"
            )
        
        if not utils.verify(password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Email or Password"
            )
        
        return user
    
    @staticmethod
    def create_access_token_for_user(user_id: int):
        """Create access token for user"""
        return oauth2.create_access_token(data={"id": user_id})
    