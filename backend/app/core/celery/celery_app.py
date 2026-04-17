from celery import Celery
from app.core.config.config import settings

celery_app = Celery(
    "fastapi_boilerplate",
    broker=settings.REDIS_BROKER_URL,
    backend=settings.REDIS_RESULT_BACKEND,
)

celery_app.conf.update(
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    task_track_started=True,
    task_time_limit=30 * 60,
    task_queues={
        "email_queue": {
            "exchange": "email_queue",
            "routing_key": "email_queue",
        },
        "maintenance_queue": {  # NEW
            "exchange": "maintenance_queue",
            "routing_key": "maintenance_queue",
        },
    },
    task_routes={
        "app.core.celery.tasks.email_tasks.*": {"queue": "email_queue"},
        "app.core.celery.tasks.reminder_tasks.*": {"queue": "email_queue"},
        # NEW
        "app.core.celery.tasks.cleanup_tasks.*": {"queue": "maintenance_queue"},
    },
    # NEW: Result expiration settings
    result_expires=15 * 24 * 3600,  # Results expire after 15 days
    task_ignore_result=False,
    task_store_errors_even_if_ignored=True,
)
