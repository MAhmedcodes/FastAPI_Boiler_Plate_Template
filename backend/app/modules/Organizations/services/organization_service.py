from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.Organizations.repository.organization_repository import OrganizationRepository
from app.core.config.config import settings


class OrganizationService:

    @staticmethod
    def get_all_organizations(db: Session):
        """Get all organizations"""
        org_repo = OrganizationRepository(db)
        organizations = org_repo.get_all()
        return {
            "organizations": organizations,
            "count": len(organizations)
        }

    @staticmethod
    def create_organization(db: Session, name: str):
        """Create a new organization"""
        org_repo = OrganizationRepository(db)

        # Check if name exists
        existing = org_repo.get_by_name(name)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Organization '{name}' already exists"
            )

        # Create organization
        org = org_repo.create(name=name)

        return org

    @staticmethod
    def join_organization(db: Session, organization_id: int):
        """Generate invite links for joining an organization"""
        org_repo = OrganizationRepository(db)

        # Get organization
        org = org_repo.get_by_id(organization_id)
        if not org:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Organization not found"
            )

        # Base URL for invite links
        base_url = "http://localhost:8000"

        # Generate invite links
        google_link = f"{base_url}/auth/google/login?invite_token={org.invite_token}"
        github_link = f"{base_url}/auth/github/login?invite_token={org.invite_token}"

        return {
            "organization_id": org.id,
            "organization_name": org.name,
            "invite_token": org.invite_token,
            "google_invite_link": google_link,
            "github_invite_link": github_link,
            "message": f"Use the links above to join {org.name}"
        }
