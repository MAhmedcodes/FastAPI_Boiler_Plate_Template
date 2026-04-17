from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.dependencies.dependencies import get_db
from app.modules.Organizations.schema import schema
from app.modules.Organizations.services.organization_service import OrganizationService

router = APIRouter(prefix="/organizations", tags=["Organizations"])


@router.get("/", response_model=schema.OrganizationListResponse)
def get_all_organizations(db: Session = Depends(get_db)):
    """Get all available organizations"""
    result = OrganizationService.get_all_organizations(db)
    return result


@router.post("/create", response_model=schema.OrganizationOut)
def create_organization(
    org_data: schema.OrganizationCreate,
    db: Session = Depends(get_db)
):
    """Create a new organization"""
    result = OrganizationService.create_organization(db, org_data.name)
    return result


@router.post("/join", response_model=schema.JoinOrganizationResponse)
def join_organization(
    request: schema.JoinOrganizationRequest,
    db: Session = Depends(get_db)
):
    """Request to join an organization - returns invite links"""
    result = OrganizationService.join_organization(db, request.organization_id)
    return result
