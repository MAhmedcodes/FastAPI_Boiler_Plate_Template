from sqlalchemy.orm import Session
from app.modules.jobs.models.model import TaskControl
from typing import Optional
from datetime import datetime, timezone


class TaskControlRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_task_name(self, task_name: str) -> Optional[TaskControl]:
        """Get task control by name"""
        return self.db.query(TaskControl).filter(TaskControl.task_name == task_name).first()

    def create_or_update(self, task_name: str, is_paused: bool) -> TaskControl:
        """Create or update task control status"""
        task_control = self.get_by_task_name(task_name)

        if task_control:
            task_control.is_paused = is_paused  # type: ignore
            if is_paused:
                task_control.paused_at = datetime.now(  # type: ignore
                    timezone.utc)
        else:
            task_control = TaskControl(
                task_name=task_name,
                is_paused=is_paused
            )
            self.db.add(task_control)

        self.db.commit()
        self.db.refresh(task_control)
        return task_control

    def is_paused(self, task_name: str) -> bool:
        """Check if a task is paused"""
        task_control = self.get_by_task_name(task_name)
        return task_control.is_paused if task_control else False  # type: ignore

    def get_all(self):
        """Get all task controls"""
        return self.db.query(TaskControl).all()
