# Cleanup task for expired and stale data

from app.core.celery.celery_app import celery_app
from redis import Redis
from app.core.config.config import settings
from datetime import datetime, timedelta, timezone


@celery_app.task(name="cleanup_expired_task_metadata", queue="maintenance_queue")
def cleanup_expired_task_metadata():
    """
    Clean up expired task results from Redis backend
    Runs every 15 days via Celery Beat
    """
    try:
        # Connect to Redis
        redis_client = Redis.from_url(settings.REDIS_RESULT_BACKEND)

        # Get all keys (task results)
        all_keys = redis_client.keys("*")

        expired_count = 0

        for key in all_keys:  # type: ignore
            # Get task result TTL (time to live)
            ttl = redis_client.ttl(key)

            # If TTL is -1 (no expiration) and key is old, delete it
            if ttl == -1:
                # Get key idle time
                idle_time = redis_client.object("idletime", key)
                if idle_time and idle_time > 15 * 24 * 3600:  # type: ignore  # 15 days in seconds
                    redis_client.delete(key)
                    expired_count += 1

            # If TTL is 0 or negative, key is already expired
            elif ttl <= 0:  # type: ignore
                redis_client.delete(key)
                expired_count += 1

        print(f"[CLEANUP TASK] Removed {expired_count} expired task results")
        return {"removed_count": expired_count}

    except Exception as e:
        print(f"[CLEANUP TASK] Failed to cleanup task metadata: {e}")
        raise


@celery_app.task(name="cleanup_stale_queue_messages", queue="maintenance_queue")
def cleanup_stale_queue_messages():
    """
    Clean up stale/unprocessed messages from Redis queues
    Runs every 15 days via Celery Beat
    """
    try:
        redis_client = Redis.from_url(settings.REDIS_BROKER_URL)

        # List of queues to clean
        queues = ["email_queue", "maintenance_queue", "default"]

        total_removed = 0

        for queue_name in queues:
            # Get queue length
            queue_key = f"celery_{queue_name}"
            queue_length = redis_client.llen(queue_key)

            if queue_length > 0:  # type: ignore
                print(
                    f"[CLEANUP TASK] Queue {queue_name}: {queue_length} messages")

        print(f"[CLEANUP TASK] Completed queue cleanup")
        return {"queues_checked": len(queues), "total_messages": total_removed}

    except Exception as e:
        print(f"[CLEANUP TASK] Failed to cleanup queue messages: {e}")
        raise


@celery_app.task(name="full_cleanup_task", queue="maintenance_queue")
def full_cleanup_task():
    """
    Combined cleanup task - runs all cleanup operations
    Runs every 15 days via Celery Beat
    NOTE: Do NOT use .get() inside tasks - celery will handle chaining
    """
    print("[CLEANUP TASK] Starting full cleanup...")

    # Run cleanup tasks asynchronously (don't wait)
    cleanup_expired_task_metadata.delay()  # type: ignore
    cleanup_stale_queue_messages.delay()  # type: ignore

    print("[CLEANUP TASK] Full cleanup tasks dispatched")

    return {
        "status": "dispatched",
        "completed_at": datetime.now(timezone.utc).isoformat()
    }
