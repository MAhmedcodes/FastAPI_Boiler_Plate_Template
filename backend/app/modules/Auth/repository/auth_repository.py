from sqlalchemy.orm import Session
from app.modules.Users.models import model
from typing import Optional

class AuthRepository:
    
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_for_auth(self, email: str) -> Optional[model.User]:
        """Get user by email for authentication"""
        return self.db.query(model.User).filter(
            model.User.email == email
        ).first()
    
    def get_user_by_id(self, user_id: int) -> Optional[model.User]:
        """Get user by ID for token validation"""
        return self.db.query(model.User).filter(
            model.User.id == user_id
        ).first()
    