from sqlalchemy.orm import Session
from app.modules.Auth.models.model import OTP
from datetime import datetime, timedelta, timezone
import random


class OTPRepository:

    def __init__(self, db: Session):
        self.db = db

    def generate_otp(self, user_id: int) -> str:
        """Generate 6-digit OTP and store in database"""
        # Delete old unused OTPs for this user
        self.db.query(OTP).filter(
            OTP.user_id == user_id,
            OTP.is_used == False
        ).delete()

        # Generate new OTP
        otp_code = str(random.randint(100000, 999999))
        expires_at = datetime.now(timezone.utc) + timedelta(hours=24)

        otp = OTP(
            user_id=user_id,
            otp_code=otp_code,
            expires_at=expires_at,
            is_used=False
        )
        self.db.add(otp)
        self.db.commit()
        self.db.refresh(otp)

        return otp_code

    def verify_otp(self, user_id: int, otp_code: str) -> bool:
        """Verify OTP and mark as used if valid"""
        otp = self.db.query(OTP).filter(
            OTP.user_id == user_id,
            OTP.otp_code == otp_code,
            OTP.is_used == False,
            OTP.expires_at > datetime.now(timezone.utc)
        ).first()

        if not otp:
            return False

        otp.is_used = True  # type: ignore
        self.db.commit()
        return True
