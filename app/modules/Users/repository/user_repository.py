from sqlalchemy.orm import Session
from app.modules.Users.models import model
from typing import Optional, List
from shared.utils import utils
from datetime import datetime, timedelta, timezone
from app.modules.Organizations.models.model import Organization


class UserRepository:

    def __init__(self, db: Session):
        self.db = db

    # ========== MULTI-TENANT METHODS ==========

    def get_by_email_and_org(self, email: str, organization_id: int) -> Optional[model.User]:
        """Get user by email AND organization_id"""
        return self.db.query(model.User).filter(
            model.User.email == email,
            model.User.organization_id == organization_id
        ).first()

    def get_by_oauth_and_org(self, provider: str, oauth_id: str, organization_id: int) -> Optional[model.User]:
        """Get user by OAuth provider and organization"""
        return self.db.query(model.User).filter(
            model.User.oauth_provider == provider,
            model.User.oauth_id == oauth_id,
            model.User.organization_id == organization_id
        ).first()

    def get_by_id(self, user_id: int) -> Optional[model.User]:
        """Get user by ID"""
        return self.db.query(model.User).filter(model.User.id == user_id).first()

    # ========== CREATE METHODS ==========

    def create_user(self, email: str, first_name: str, last_name: str, password: str, organization_id: int) -> model.User:
        """Create new user with password and organization"""
        hashed_password = utils.hashing(password)
        user = model.User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=hashed_password,
            oauth_provider=None,
            oauth_id=None,
            organization_id=organization_id,
            is_verified=False
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def create_oauth_user(self, email: str, first_name: str, last_name: str, oauth_provider: str, oauth_id: str, organization_id: int, is_verified: bool = True) -> model.User:
        """Create new OAuth user with organization"""
        user = model.User(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=None,
            oauth_provider=oauth_provider,
            oauth_id=oauth_id,
            organization_id=organization_id,
            is_verified=is_verified
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    # ========== UPDATE METHODS ==========

    def update_oauth_info(self, user: model.User, provider: str, oauth_id: str) -> model.User:
        """Update existing user with OAuth info"""
        user.oauth_provider = provider  # type: ignore
        user.oauth_id = oauth_id  # type: ignore
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_last_login(self, user_id: int) -> None:
        """Update user's last login timestamp"""
        user = self.get_by_id(user_id)
        if user:
            user.last_login = datetime.now(timezone.utc)  # type: ignore
            self.db.commit()

    def verify_user(self, user_id: int) -> Optional[model.User]:
        """Mark user as verified"""
        user = self.get_by_id(user_id)
        if user:
            user.is_verified = True  # type: ignore
            self.db.commit()
            self.db.refresh(user)
        return user

    # ========== HELPER METHODS ==========

    def check_email_registration_method(self, email: str, organization_id: int) -> Optional[str]:
        """Check registration method for email within organization"""
        user = self.db.query(model.User).filter(
            model.User.email == email,
            model.User.organization_id == organization_id
        ).first()

        if not user:
            return None

        if user.password is not None:
            return "password"
        elif user.oauth_provider is not None:
            return "oauth"

        return None

    def get_inactive_verified_users(self, days: int) -> List[model.User]:
        """Get verified users who haven't logged in for X days"""
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days)
        return self.db.query(model.User).filter(
            model.User.is_verified == True,
            model.User.last_login < cutoff_date
        ).all()

    # ========== NEW: ORGANIZATION INVITE METHODS ==========

    def get_organization_by_invite_token(self, invite_token: str):
        """Get organization by invite token"""
        return self.db.query(Organization).filter(Organization.invite_token == invite_token).first()

    def get_organization_by_id(self, organization_id: int):
        """Get organization by ID"""
        return self.db.query(Organization).filter(Organization.id == organization_id).first()
