from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.Users.repository.user_repository import UserRepository
from app.modules.Auth.services.oauth2_service import OAuth2Service

class UserService:
    
    @staticmethod
    def register_user(db: Session, email: str, first_name: str, last_name: str, password: str):
        """Register a new user with email/password"""
        user_repo = UserRepository(db)
    
        # Check if email already exists
        existing_user = user_repo.get_by_email(email)
        if existing_user:
            # Check how it was registered
            if existing_user.oauth_provider is not None:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"This email is already registered with {existing_user.oauth_provider}. Please login with {existing_user.oauth_provider}."
                )
            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="User with this email already exists"
                )
    
        # Create new user
        user = user_repo.create_user(email, first_name, last_name, password)
    
        # Create JWT token
        access_token = OAuth2Service.create_access_token_for_user(user.id) # type: ignore
    
        return {
            "user": user,
            "access_token": access_token
        }
    