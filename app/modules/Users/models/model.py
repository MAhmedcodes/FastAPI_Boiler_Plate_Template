from sqlalchemy import ForeignKey, Integer, Column, String, TIMESTAMP, UniqueConstraint, text, Boolean
from sqlalchemy.orm import relationship
from app.core.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
    oauth_provider = Column(String, nullable=True)  # 'google' or 'github'
    # ID from Google/GitHub
    oauth_id = Column(String, unique=False, nullable=True)
    is_verified = Column(Boolean, nullable=False, server_default=text('false'))
    last_login = Column(TIMESTAMP(timezone=True), nullable=True)
    organization_id = Column(Integer, ForeignKey(
        "organizations.id", ondelete="CASCADE"),)
    # "organizations.id", ondelete="CASCADE"), nullable=False)
    __table_args__ = (
        UniqueConstraint('email', 'organization_id',
                         name='unique_email_per_organization'),
    )
