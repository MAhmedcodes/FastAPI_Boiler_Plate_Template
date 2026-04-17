from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, text
from app.core.database.database import Base


class TaskControl(Base):
    __tablename__ = "task_controls"

    id = Column(Integer, primary_key=True, nullable=False)
    # 'welcome_email', 'reminder_email', 'cleanup'
    task_name = Column(String, nullable=False, unique=True)
    is_paused = Column(Boolean, nullable=False, server_default=text('false'))
    paused_at = Column(TIMESTAMP(timezone=True), nullable=True)
    updated_at = Column(TIMESTAMP(timezone=True),
                        server_default=text('now()'), onupdate=text('now()'))
