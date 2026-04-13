# app/services/auth_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.modules.Users.models import model



class OAuthService:

    @staticmethod
    def handle_google_oauth(db: Session, user_info: dict):
        """Handle Google OAuth login/registration"""
        email = user_info.get('email')
        google_id = str(user_info.get('sub'))
        
        if not email:
            raise HTTPException(status_code=400, detail="Email not provided by Google")
        
        # Find or create user
        user = db.query(model.User).filter(
            model.User.oauth_provider == 'google',
            model.User.oauth_id == google_id
        ).first()
        
        if not user:
            # Check if user exists with same email
            user = db.query(model.User).filter(
                model.User.email == email
            ).first()
            
            if user:
                # Update existing user with OAuth info
                user.oauth_provider = 'google' # type: ignore
                user.oauth_id = google_id  # type: ignore
                db.commit()
                db.refresh(user)
            else:
                # Create new user
                user = model.User(
                    email=email,
                    password=None,
                    oauth_provider='google',
                    oauth_id=google_id
                )
                db.add(user)
                db.commit()
                db.refresh(user)
        
        return user
    
    @staticmethod
    def handle_github_oauth(db: Session, user_info: dict, github_id: str, email: str):
        """Handle GitHub OAuth login/registration"""
        # Find or create user
        user = db.query(model.User).filter(
            model.User.oauth_provider == 'github',
            model.User.oauth_id == github_id
        ).first()
        
        if not user:
            # Check if user exists with same email
            user = db.query(model.User).filter(
                model.User.email == email
            ).first()
            
            if user:
                # Update existing user with OAuth info
                user.oauth_provider = 'github' # type: ignore
                user.oauth_id = github_id # type: ignore
                db.commit()
                db.refresh(user)
            else:
                # Create new user
                user = model.User(
                    email=email,
                    password=None,
                    oauth_provider='github',
                    oauth_id=github_id
                )
                db.add(user)
                db.commit()
                db.refresh(user)
        
        return user
    