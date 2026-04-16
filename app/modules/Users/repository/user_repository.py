from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session
from app.modules.Users.models import model
from typing import List, Optional
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

    # app/modules/Users/repository/user_repository.py

        # Update create_oauth_user method to accept is_verified parameter
    def create_oauth_user(self, email: str, first_name: str, last_name: str, oauth_provider: str, oauth_id: str, is_verified: bool = True) -> model.User:
        """Create new OAuth user with verified status"""
        user = model.User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=None,
            oauth_provider=oauth_provider,
            oauth_id=oauth_id,
            is_verified=is_verified  # OAuth users are auto-verified
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
        user.oauth_provider = provider  # type: ignore
        user.oauth_id = oauth_id  # type: ignore
        self.db.commit()
        self.db.refresh(user)
        return user

    def check_email_registration_method(self, email: str) -> Optional[str]:
        # Check which method an email is registered with. Returns 'oauth', 'password', or None
        user = self.db.query(model.User).filter(
            model.User.email == email
        ).first()

        if not user:
            return None

        if user.password is not None:
            return "password"
        elif user.oauth_provider is not None:
            return "oauth"

        return None

    def get_by_oauth_and_email(self, provider: str, email: str) -> Optional[model.User]:
        """Get user by provider and email - ensures same provider"""
        return self.db.query(model.User).filter(
            model.User.email == email,
            model.User.oauth_provider == provider
        ).first()

    def verify_user(self, user_id: int) -> Optional[model.User]:
        """Mark user as verified"""
        user = self.get_by_id(user_id)
        if user:
            user.is_verified = True  # type: ignore
            self.db.commit()
            self.db.refresh(user)
        return user

    def update_last_login(self, user_id: int) -> None:
        """Update user's last login timestamp"""
        user = self.get_by_id(user_id)
        if user:
            user.last_login = datetime.now(timezone.utc)  # type: ignore
            self.db.commit()

    def get_inactive_verified_users(self, days: int) -> List[model.User]:
        """Get verified users who haven't logged in for X days"""
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
        return self.db.query(model.User).filter(
            model.User.is_verified == True,
            model.User.last_login < cutoff_date
        ).all()
