from app.core.celery.celery_app import celery_app
from shared.utils.email_utils import send_welcome_email


@celery_app.task(name="send_welcome_email_task", queue="email_queue")
def send_welcome_email_task(email: str, first_name: str, organization_name: str):
    """Send welcome email with organization name"""
    send_welcome_email(email, first_name, organization_name)
    return {"email": email, "first_name": first_name, "organization_name": organization_name}
