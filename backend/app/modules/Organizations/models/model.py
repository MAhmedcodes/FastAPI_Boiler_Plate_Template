from sqlalchemy import Column, Integer, String, TIMESTAMP, text
from app.core.database.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    # Unique token for joining
    invite_token = Column(String, nullable=True, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), nullable=False)
