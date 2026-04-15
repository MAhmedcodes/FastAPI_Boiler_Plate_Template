# Celery Beat schedules for periodic tasks

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    # Inactive user reminder - runs daily at 9:00 AM
    "inactive_user_reminder": {
        "task": "app.core.celery.tasks.reminder_tasks.send_inactive_reminder_task",
        "schedule": crontab(hour=9, minute=0),  # 9:00 AM daily
        "kwargs": {"days_threshold": 5},  # Users inactive for 5+ days
        "options": {"queue": "email_queue"},
    },
}
