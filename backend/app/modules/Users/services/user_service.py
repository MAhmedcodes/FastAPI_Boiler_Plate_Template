from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.Users.repository.user_repository import UserRepository
from app.modules.Auth.services.oauth2_service import OAuth2Service
from app.core.celery.tasks.email_tasks import send_welcome_email_task


class UserService:

    @staticmethod
    def register_user(db: Session, email: str, first_name: str, last_name: str, password: str, invite_token: str):
        """Register a new user with invite token"""
        user_repo = UserRepository(db)

        # Get organization by invite token
        org = user_repo.get_organization_by_invite_token(invite_token)
        if not org:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired invite token. Please request a new invite link."
            )

        organization_id = org.id
        organization_name = org.name

        # Check if user exists in this organization
        existing_user = user_repo.get_by_email_and_org(
            email, organization_id)  # type: ignore
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User with email '{email}' already exists in organization '{organization_name}'. Please login instead."
            )

        # Create new user
        user = user_repo.create_user(
            email, first_name, last_name, password, organization_id)  # type: ignore

        # Create JWT token with organization
        access_token = OAuth2Service.create_access_token_for_user(
            user.id, organization_id)  # type: ignore

        # Note: Welcome email will be sent after OTP verification, not here

        return {
            "user": user,
            "access_token": access_token
        }
