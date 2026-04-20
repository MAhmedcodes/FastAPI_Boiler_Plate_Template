from app.core.celery.celery_app import celery_app
from app.core.database.database import Sessionlocal
from app.modules.Users.repository.user_repository import UserRepository
from shared.utils.email_utils import send_inactive_reminder_email
from datetime import datetime, timezone
from app.modules.jobs.repository.job_repository import TaskControlRepository


@celery_app.task(name="send_inactive_reminder_task", queue="email_queue")
def send_inactive_reminder_task(days_threshold: int = 5):
    """
    Send reminder emails to inactive verified users
    Runs daily via Celery Beat
    """
    db = Sessionlocal()
    try:
        # Check if task is paused
        task_control_repo = TaskControlRepository(db)
        if task_control_repo.is_paused("reminder_email"):
            print(f"[REMINDER TASK] Task is paused. No reminders sent.")
            return {"status": "paused", "message": "Task is paused"}

        user_repo = UserRepository(db)

        # Get users inactive for X days
        inactive_users = user_repo.get_inactive_verified_users(days_threshold)

        print(f"[REMINDER TASK] Found {len(inactive_users)} inactive users")

        # Send email to each inactive user
        for user in inactive_users:
            # Calculate exact days inactive
            days_inactive = (datetime.now(timezone.utc) -
                             user.last_login).days  # type: ignore
            send_inactive_reminder_email(
                to_email=user.email, first_name=user.first_name, days_inactive=days_inactive)  # type: ignore

        return {"processed": len(inactive_users)}
    except Exception as e:
        print(f"[REMINDER TASK] Failed: {e}")
        raise
    finally:
        db.close()
