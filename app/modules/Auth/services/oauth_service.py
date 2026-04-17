from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.Users.repository.user_repository import UserRepository
from app.modules.Users.models import model
from app.core.celery.tasks.email_tasks import send_welcome_email_task


class OAuthService:

    @staticmethod
    def extract_name_from_google(user_info: dict):
        """Extract first and last name from Google user info"""
        first_name = user_info.get('given_name', '')
        last_name = user_info.get('family_name', '')

        if not first_name and not last_name:
            full_name = user_info.get('name', '')
            name_parts = full_name.split(' ', 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

        return first_name, last_name

    @staticmethod
    def handle_google_oauth(db: Session, user_info: dict, invite_token: str):
        """Handle Google OAuth login/registration with invite token"""

        email = user_info.get('email')
        google_id = str(user_info.get('sub'))
        first_name, last_name = OAuthService.extract_name_from_google(
            user_info)

        if not email:
            raise HTTPException(
                status_code=400,
                detail="Email not provided by Google"
            )

        user_repo = UserRepository(db)

        # Get organization from invite token if provided
        organization_id = None
        if invite_token:
            org = user_repo.get_organization_by_invite_token(invite_token)
            if not org:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid or expired invite token"
                )
            organization_id = org.id
        else:
            # Fallback to default organization (for existing users)
            default_org = user_repo.get_organization_by_invite_token("default")
            if default_org:
                organization_id = default_org.id
            else:
                organization_id = 1

        # Get organization name for email
        org = user_repo.get_organization_by_id(organization_id)  # type: ignore
        organization_name = org.name if org else "Our Platform"

        # FIRST: Check if this Google user already exists in this organization
        user = user_repo.get_by_oauth_and_org(
            'google', google_id, organization_id)  # type: ignore

        if user:
            # User already exists in this organization - just update last login
            user_repo.update_last_login(user.id)  # type: ignore
            return user

        # SECOND: Check if this Google user exists in ANY organization (by oauth_id only)
        any_org_user = db.query(model.User).filter(
            model.User.oauth_provider == 'google',
            model.User.oauth_id == google_id
        ).first()

        if any_org_user:
            # User exists in another organization - create NEW user in this organization
            user = user_repo.create_oauth_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                oauth_provider='google',
                oauth_id=google_id,
                organization_id=organization_id,  # type: ignore
                is_verified=True
            )
            send_welcome_email_task.delay(  # type: ignore
                email, first_name, organization_name)  # type: ignore
            user_repo.update_last_login(user.id)  # type: ignore
            return user

        # THIRD: Check if email exists in this organization (password user)
        existing_user = user_repo.get_by_email_and_org(
            email, organization_id)  # type: ignore

        if existing_user:
            # User exists but not with OAuth - link account
            if existing_user.oauth_provider:  # type: ignore
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"This email is already registered with {existing_user.oauth_provider}"
                )
            # Link OAuth to existing user
            user = user_repo.update_oauth_info(
                existing_user, 'google', google_id)
            user_repo.update_last_login(user.id)  # type: ignore
            return user

        # FOURTH: Create brand new user
        user = user_repo.create_oauth_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            oauth_provider='google',
            oauth_id=google_id,
            organization_id=organization_id,  # type: ignore
            is_verified=True
        )
        send_welcome_email_task.delay(  # type: ignore
            email, first_name, organization_name)  # type: ignore
        user_repo.update_last_login(user.id)  # type: ignore

        return user

    @staticmethod
    def extract_name_from_github(user_info: dict):
        """Extract first and last name from GitHub user info"""
        name = user_info.get('name', '')

        if name:
            name_parts = name.split(' ', 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''
        else:
            login = user_info.get('login', '')
            first_name = login
            last_name = ''

        return first_name, last_name

    @staticmethod
    def handle_github_oauth(db: Session, user_info: dict, github_id: str, email: str, invite_token: str):
        """Handle GitHub OAuth login/registration with invite token"""

        first_name, last_name = OAuthService.extract_name_from_github(
            user_info)

        user_repo = UserRepository(db)

        # Get organization from invite token if provided
        organization_id = None
        if invite_token:
            org = user_repo.get_organization_by_invite_token(invite_token)
            if not org:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Invalid or expired invite token"
                )
            organization_id = org.id
        else:
            # Fallback to default organization
            default_org = user_repo.get_organization_by_invite_token("default")
            if default_org:
                organization_id = default_org.id
            else:
                organization_id = 1

        # Get organization name for email
        org = user_repo.get_organization_by_id(organization_id)  # type: ignore
        organization_name = org.name if org else "Our Platform"

        # FIRST: Check if this GitHub user already exists in this organization
        user = user_repo.get_by_oauth_and_org(
            'github', github_id, organization_id)  # type: ignore

        if user:
            user_repo.update_last_login(user.id)  # type: ignore
            return user

        # SECOND: Check if this GitHub user exists in ANY organization (by oauth_id only)
        any_org_user = db.query(model.User).filter(
            model.User.oauth_provider == 'github',
            model.User.oauth_id == github_id
        ).first()

        if any_org_user:
            user = user_repo.create_oauth_user(
                email=email,
                first_name=first_name,
                last_name=last_name,
                oauth_provider='github',
                oauth_id=github_id,
                organization_id=organization_id,  # type: ignore
                is_verified=True
            )
            send_welcome_email_task.delay(  # type: ignore
                email, first_name, organization_name)  # type: ignore
            user_repo.update_last_login(user.id)  # type: ignore
            return user

        # THIRD: Check if email exists in this organization (password user)
        existing_user = user_repo.get_by_email_and_org(
            email, organization_id)  # type: ignore

        if existing_user:
            if existing_user.oauth_provider:  # type: ignore
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"This email is already registered with {existing_user.oauth_provider}"
                )
            user = user_repo.update_oauth_info(
                existing_user, 'github', github_id)
            user_repo.update_last_login(user.id)  # type: ignore
            return user

        # FOURTH: Create brand new user
        user = user_repo.create_oauth_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            oauth_provider='github',
            oauth_id=github_id,
            organization_id=organization_id,  # type: ignore
            is_verified=True
        )
        send_welcome_email_task.delay(  # type: ignore
            email, first_name, organization_name)  # type: ignore
        user_repo.update_last_login(user.id)  # type: ignore

        return user
