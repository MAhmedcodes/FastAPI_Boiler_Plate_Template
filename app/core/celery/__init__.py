from app.core.celery.celery_app import celery_app

# This is where tasks get registered - AFTER celery_app exists
from app.core.celery.tasks import email_tasks

__all__ = ["celery_app"]
