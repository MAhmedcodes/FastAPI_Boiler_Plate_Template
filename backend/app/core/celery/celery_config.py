from kombu import Queue, Exchange

# Queues
CELERY_TASK_QUEUES = (
    Queue("email_queue", Exchange("email_queue"), routing_key="email_queue"),
    Queue("maintenance_queue", Exchange("maintenance_queue"),
          routing_key="maintenance_queue"),  # NEW
    Queue("default", Exchange("default"), routing_key="default"),
)

# Task routing
CELERY_TASK_ROUTES = {
    "app.core.celery.tasks.email_tasks.*": {"queue": "email_queue"},
    # NEW
    "app.core.celery.tasks.cleanup_tasks.*": {"queue": "maintenance_queue"},
    "*": {"queue": "default"},
}
