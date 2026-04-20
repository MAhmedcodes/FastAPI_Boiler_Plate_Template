from sqlalchemy import Integer, Column, String, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.sql import text
from app.core.database.database import Base


class OTP(Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    otp_code = Column(String(6), nullable=False)
    expires_at = Column(TIMESTAMP(timezone=True), nullable=False)
    is_used = Column(Boolean, nullable=False, server_default=text('false'))
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
