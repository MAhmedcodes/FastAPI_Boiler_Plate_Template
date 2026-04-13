from sqlalchemy.orm import Session
from app.modules.Users.models import model
from typing import Optional
from shared.utils import utils

class UserRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_email(self, email: str) -> Optional[model.User]:
        """Get user by email"""
        return self.db.query(model.User).filter(
            model.User.email == email
        ).first()
    
    def get_by_oauth(self, provider: str, oauth_id: str) -> Optional[model.User]:
        """Get user by OAuth provider and ID"""
        return self.db.query(model.User).filter(
            model.User.oauth_provider == provider,
            model.User.oauth_id == oauth_id
        ).first()
    
    def get_by_id(self, user_id: int) -> Optional[model.User]:
        """Get user by ID"""
        return self.db.query(model.User).filter(
            model.User.id == user_id
        ).first()
    
    def create(self, email: str, password=None, oauth_provider=None, oauth_id=None) -> model.User:
        """Create new user (without name - for backward compatibility)"""
        user = model.User(
            email=email,
            password=password,
            oauth_provider=oauth_provider,
            oauth_id=oauth_id,
            first_name='',  # Empty default
            last_name=''    # Empty default
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def create_oauth_user(self, email: str, first_name: str, last_name: str, oauth_provider: str, oauth_id: str) -> model.User:
        """Create new OAuth user with name"""
        user = model.User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=None,
            oauth_provider=oauth_provider,
            oauth_id=oauth_id
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def create_user(self, email: str, first_name: str, last_name: str, password: str) -> model.User:
        """Create new user with password and name"""
        hashed_password = utils.hashing(password)
        user = model.User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=hashed_password,
            oauth_provider=None,
            oauth_id=None
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    def update_oauth_info(self, user: model.User, provider: str, oauth_id: str) -> model.User:
        """Update existing user with OAuth info"""
        user.oauth_provider = provider # type: ignore
        user.oauth_id = oauth_id # type: ignore
        self.db.commit()
        self.db.refresh(user)
        return user
    