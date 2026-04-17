# Redis cleanup utilities

from redis import Redis
from app.core.config.config import settings


def get_redis_connection():
    """Get Redis connection"""
    return Redis.from_url(settings.REDIS_RESULT_BACKEND)


def get_queue_length(queue_name: str):
    """Get number of messages in a queue"""
    redis_client = get_redis_connection()
    return redis_client.llen(f"celery_{queue_name}")


def get_task_result_count():
    """Get number of stored task results"""
    redis_client = get_redis_connection()
    return len(redis_client.keys("*"))  # type: ignore
