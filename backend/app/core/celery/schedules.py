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

    # NEW: Cleanup job - runs every 15 days at 2:00 AM
    "cleanup_job": {
        "task": "app.core.celery.tasks.cleanup_tasks.full_cleanup_task",
        # Every 15 days at 2 AM
        "schedule": crontab(day_of_month="*/15", hour=2, minute=0),
        "options": {"queue": "maintenance_queue"},
    },
}
