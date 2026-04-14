from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.Users.repository.user_repository import UserRepository


class OAuthService:

    @staticmethod
    def extract_name_from_google(user_info: dict):
        """Extract first and last name from Google user info"""
        first_name = user_info.get('given_name', '')
        last_name = user_info.get('family_name', '')

        # Fallback if structured names are not available
        if not first_name and not last_name:
            full_name = user_info.get('name', '')
            name_parts = full_name.split(' ', 1)
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

        return first_name, last_name

    @staticmethod
    def handle_google_oauth(db: Session, user_info: dict):
        """Handle Google OAuth login/registration"""

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

        # 🔹 Step 1: Check how this email was originally registered
        reg_method = user_repo.check_email_registration_method(
            email)  # type: ignore

        # ❌ If registered via password → block OAuth login
        if reg_method == "password":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This email is registered with email/password. Please login using password."
            )

        # 🔹 Step 2: Check if user exists with THIS provider (Google)
        user = user_repo.get_by_oauth('google', google_id)

        # 🔹 Step 3: If not found, check if email exists with another provider
        if not user:
            existing_user = user_repo.get_by_email(email)

            # ❌ Block if registered with different OAuth provider
            if existing_user and existing_user.oauth_provider and existing_user.oauth_provider != 'google':  # type: ignore
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"This email is already registered with {existing_user.oauth_provider}. Please login with {existing_user.oauth_provider}."
                )

        # 🔹 Step 4: If user not found via provider
        if not user:
            user = user_repo.get_by_email(email)

            if user:
                # ❌ Prevent provider switching (IMPORTANT FIX)
                if user.oauth_provider != 'google':  # type: ignore
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"This account is registered with {user.oauth_provider}. Please login using that provider."
                    )

                # ✅ Same provider → allow updating OAuth info
                user = user_repo.update_oauth_info(user, 'google', google_id)

                # Update missing name fields if needed
                if not user.first_name:  # type: ignore
                    user.first_name = first_name
                    user.last_name = last_name  # type: ignore
                    db.commit()
                    db.refresh(user)

            else:
                # ✅ New user → create account with is_verified=True
                user = user_repo.create_oauth_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    oauth_provider='google',
                    oauth_id=google_id,
                    is_verified=True  # OAuth users are auto-verified
                )

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
    def handle_github_oauth(db: Session, user_info: dict, github_id: str, email: str):
        """Handle GitHub OAuth login/registration"""

        first_name, last_name = OAuthService.extract_name_from_github(
            user_info)

        user_repo = UserRepository(db)

        # 🔹 Step 1: Check how this email was originally registered
        reg_method = user_repo.check_email_registration_method(email)

        # ❌ If registered via password → block OAuth login
        if reg_method == "password":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="This email is registered with email/password. Please login using password."
            )

        # 🔹 Step 2: Check if user exists with THIS provider (GitHub)
        user = user_repo.get_by_oauth('github', github_id)

        # 🔹 Step 3: If not found, check if email exists with another provider
        if not user:
            existing_user = user_repo.get_by_email(email)

            # ❌ Block if registered with different OAuth provider
            if existing_user and existing_user.oauth_provider and existing_user.oauth_provider != 'github':  # type: ignore
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"This email is already registered with {existing_user.oauth_provider}. Please login with {existing_user.oauth_provider}."
                )

        # 🔹 Step 4: If user not found via provider
        if not user:
            user = user_repo.get_by_email(email)

            if user:
                # ❌ Prevent provider switching (IMPORTANT FIX)
                if user.oauth_provider != 'github':  # type: ignore
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"This account is registered with {user.oauth_provider}. Please login using that provider."
                    )

                # ✅ Same provider → allow updating OAuth info
                user = user_repo.update_oauth_info(user, 'github', github_id)

                # Update missing name fields if needed
                if not user.first_name:  # type: ignore
                    user.first_name = first_name
                    user.last_name = last_name  # type: ignore
                    db.commit()
                    db.refresh(user)

            else:
                # ✅ New user → create account with is_verified=True
                user = user_repo.create_oauth_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    oauth_provider='github',
                    oauth_id=github_id,
                    is_verified=True  # OAuth users are auto-verified
                )

        return user
