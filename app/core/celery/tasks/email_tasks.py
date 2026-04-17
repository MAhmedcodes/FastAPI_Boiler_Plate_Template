# IMPORTANT: Import celery_app AFTER it's created (circular import avoided)
from app.core.celery.celery_app import celery_app
from app.core.database.database import Sessionlocal
from app.modules.jobs.repository.job_repository import TaskControlRepository
from shared.utils.email_utils import send_welcome_email


<<<<<<< Updated upstream
@celery_app.task(name="send_welcome_email_task", queue="email_queue")
def send_welcome_email_task(email: str, first_name: str):
    send_welcome_email(email, first_name)
    return {"email": email, "first_name": first_name}
=======
def send_welcome_email_task(email: str, first_name: str, organization_name: str):
    # Check if task is paused
    db = Sessionlocal()
    try:
        repo = TaskControlRepository(db)
        if repo.is_paused("welcome_email"):
            print(f"[WELCOME EMAIL] Task paused. Email to {email} not sent.")
            return {"status": "paused", "email": email}
    finally:
        db.close()

    # Continue with normal execution
    send_welcome_email(email, first_name, organization_name)
    return {"email": email, "first_name": first_name, "organization_name": organization_name}
>>>>>>> Stashed changes
