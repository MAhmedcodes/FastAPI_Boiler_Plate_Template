from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.Users.repository.user_repository import UserRepository

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
    def handle_google_oauth(db: Session, user_info: dict):
        """Handle Google OAuth login/registration"""
        email = user_info.get('email')
        google_id = str(user_info.get('sub'))
        first_name, last_name = OAuthService.extract_name_from_google(user_info)
        
        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        
        user_repo = UserRepository(db)
        
        # Find or create user
        user = user_repo.get_by_oauth('google', google_id)
        
        if not user:
            # Check if user exists with same email
            user = user_repo.get_by_email(email)
            
            if user:
                # Update existing user with OAuth info
                user = user_repo.update_oauth_info(user, 'google', google_id)
                # Update name if empty
                if not user.first_name: # type: ignore
                    user.first_name = first_name
                    user.last_name = last_name # type: ignore
                    db.commit()
                    db.refresh(user)
            else:
                # Create new user with name
                user = user_repo.create_oauth_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    oauth_provider='google',
                    oauth_id=google_id
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
        first_name, last_name = OAuthService.extract_name_from_github(user_info)
        
        user_repo = UserRepository(db)
        
        # Find or create user
        user = user_repo.get_by_oauth('github', github_id)
        
        if not user:
            # Check if user exists with same email
            user = user_repo.get_by_email(email)
            
            if user:
                # Update existing user with OAuth info
                user = user_repo.update_oauth_info(user, 'github', github_id)
                # Update name if empty
                if not user.first_name: # type: ignore
                    user.first_name = first_name
                    user.last_name = last_name # type: ignore
                    db.commit()
                    db.refresh(user)
            else:
                # Create new user with name
                user = user_repo.create_oauth_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    oauth_provider='github',
                    oauth_id=github_id
                )
        
        return user
    