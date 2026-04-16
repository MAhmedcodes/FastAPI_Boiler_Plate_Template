from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.modules.Users.repository.user_repository import UserRepository
from app.modules.Auth.repository.otp_repository import OTPRepository
from shared.utils.email_utils import send_verification_email
from app.core.celery.tasks.email_tasks import send_welcome_email_task


class VerificationService:

    @staticmethod
    def request_verification(db: Session, user_id: int):
        """Generate OTP and send to user email"""
        user_repo = UserRepository(db)
        user = user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # OAuth users cannot request verification
        if user.oauth_provider:  # type: ignore
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="OAuth users are already verified"
            )

        # Already verified users cannot request again
        if user.is_verified:  # type: ignore
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already verified"
            )

        # Generate OTP
        otp_repo = OTPRepository(db)
        otp_code = otp_repo.generate_otp(user_id)

        # Send email synchronously (no background worker)
        send_verification_email(user.email, otp_code)  # type: ignore

        return {"message": "Verification OTP sent to your email"}

    @staticmethod
    def verify_otp(db: Session, user_id: int, otp_code: str):
        """Verify OTP and mark user as verified"""
        user_repo = UserRepository(db)
        user = user_repo.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )

        # OAuth users cannot verify via OTP
        if user.oauth_provider:  # type: ignore
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="OAuth users are already verified"
            )

        # Already verified users cannot verify again
        if user.is_verified:  # type: ignore
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User is already verified"
            )

        # Verify OTP
        otp_repo = OTPRepository(db)
        if not otp_repo.verify_otp(user_id, otp_code):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid or expired OTP"
            )

        # Mark user as verified
        user_repo.verify_user(user_id)
        send_welcome_email_task.delay(user.email, user.first_name)  # type: ignore

        return {"message": "User verified successfully"}
