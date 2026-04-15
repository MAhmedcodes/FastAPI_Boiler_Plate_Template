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
    
        # Check registration method
        reg_method = user_repo.check_email_registration_method(email)
    
        if reg_method == "oauth":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="This email is registered with Google/GitHub. Please use OAuth login."
            )
    
        if reg_method is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Invalid Email or Password"
            )
    
        user = user_repo.get_by_email(email)
    
        if not utils.verify(password, user.password):  # type: ignore
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid Email or Password"
            )
        user_repo.update_last_login(user.id) # type: ignore
        return user
    
    @staticmethod
    def create_access_token_for_user(user_id: int):
        """Create access token for user"""
        return oauth2.create_access_token(data={"id": user_id})
    