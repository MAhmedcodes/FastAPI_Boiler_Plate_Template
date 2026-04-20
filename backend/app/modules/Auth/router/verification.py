from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.core.dependencies.dependencies import get_db
from app.core.security.OAuth2.oauth2 import current_user
from app.modules.Users.models import model
from app.modules.Auth.services.verification_service import VerificationService

router = APIRouter(prefix="/auth", tags=["Verification"])


class OTPVerifyRequest(BaseModel):
    otp_code: str


@router.post("/request-verification")
def request_verification(
    db: Session = Depends(get_db),
    current_user: model.User = Depends(current_user)
):
    """Request OTP for email verification"""
    return VerificationService.request_verification(db, current_user.id)  # type: ignore


@router.post("/verify-otp")
def verify_otp(
    request: OTPVerifyRequest,
    db: Session = Depends(get_db),
    current_user: model.User = Depends(current_user)
):
    """Submit OTP to verify user"""
    return VerificationService.verify_otp(db, current_user.id, request.otp_code)  # type: ignore
