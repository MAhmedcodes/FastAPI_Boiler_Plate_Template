from sqlalchemy.orm import Session
from app.modules.Organizations.models.model import Organization
from typing import Optional, List
import secrets
import string


class OrganizationRepository:

    def __init__(self, db: Session):
        self.db = db

    def generate_invite_token(self, length: int = 12) -> str:
        """Generate unique invite token"""
        alphabet = string.ascii_uppercase + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))

    def get_all(self) -> List[Organization]:
        """Get all organizations"""
        return self.db.query(Organization).all()

    def get_by_id(self, org_id: int) -> Optional[Organization]:
        """Get organization by ID"""
        return self.db.query(Organization).filter(Organization.id == org_id).first()

    def get_by_invite_token(self, invite_token: str) -> Optional[Organization]:
        """Get organization by invite token"""
        return self.db.query(Organization).filter(Organization.invite_token == invite_token).first()

    def get_by_name(self, name: str) -> Optional[Organization]:
        """Get organization by name"""
        return self.db.query(Organization).filter(Organization.name == name).first()

    def create(self, name: str) -> Organization:
        """Create a new organization with unique invite token"""
        invite_token = self.generate_invite_token()
        org = Organization(
            name=name,
            invite_token=invite_token
        )
        self.db.add(org)
        self.db.commit()
        self.db.refresh(org)
        return org
