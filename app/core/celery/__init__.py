from app.core.celery.tasks import reminder_tasks
from app.core.celery.tasks import email_tasks
from app.core.celery.celery_app import celery_app
from app.core.celery.schedules import CELERY_BEAT_SCHEDULE

# Apply beat schedule
celery_app.conf.beat_schedule = CELERY_BEAT_SCHEDULE

# Import tasks after celery_app exists

__all__ = ["celery_app"]
