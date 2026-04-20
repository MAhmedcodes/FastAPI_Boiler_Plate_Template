from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class OrganizationBase(BaseModel):
    name: str


class OrganizationCreate(OrganizationBase):
    pass


class OrganizationOut(OrganizationBase):
    id: int
    invite_token: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True


class OrganizationListResponse(BaseModel):
    organizations: list[OrganizationOut]
    count: int


class JoinOrganizationRequest(BaseModel):
    organization_id: int


class JoinOrganizationResponse(BaseModel):
    organization_id: int
    organization_name: str
    invite_token: str
    google_invite_link: str
    github_invite_link: str
    message: str


class VerifyInviteTokenRequest(BaseModel):
    invite_token: str
