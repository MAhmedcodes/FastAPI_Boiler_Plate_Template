# Job control service for Celery tasks

from app.core.celery.celery_app import celery_app
from app.core.celery.tasks.cleanup_tasks import full_cleanup_task
from celery.result import AsyncResult
from app.core.database.database import Sessionlocal
from app.modules.jobs.repository.job_repository import TaskControlRepository


class JobControlService:

    @staticmethod
    def trigger_cleanup_job():
        """Manually trigger the cleanup job"""
        task = full_cleanup_task.delay()  # type: ignore
        return {
            "task_id": task.id,
            "status": "started",
            "message": "Cleanup job triggered successfully"
        }

    @staticmethod
    def revoke_task(task_id: str, terminate: bool = False):
        """
        Revoke/stop a running task
        terminate=True will forcefully kill the task
        """
        try:
            # Revoke the task
            celery_app.control.revoke(task_id, terminate=terminate)

            return {
                "task_id": task_id,
                "terminate": terminate,
                "status": "revoked",
                "message": f"Task {task_id} has been revoked"
            }
        except Exception as e:
            return {
                "task_id": task_id,
                "error": str(e),
                "status": "failed"
            }

    @staticmethod
    def get_task_status(task_id: str):
        """Get status of a specific task"""
        task_result = AsyncResult(task_id, app=celery_app)

        result = {
            "task_id": task_id,
            "status": task_result.status,
            "ready": task_result.ready(),
            "successful": task_result.successful() if task_result.ready() else None,
            "failed": task_result.failed() if task_result.ready() else None,
        }

        # Add result if available
        if task_result.ready() and task_result.result:
            result["result"] = task_result.result

        # Add error if failed
        if task_result.failed():
            result["error"] = str(task_result.info)

        return result

    @staticmethod
    def get_active_tasks():
        """Get all currently active/running tasks"""
        inspector = celery_app.control.inspect()
        active_tasks = inspector.active()

        if not active_tasks:
            return {"active_tasks": [], "count": 0}

        # Flatten the results from all workers
        tasks = []
        for worker, task_list in active_tasks.items():
            for task in task_list:
                tasks.append({
                    "worker": worker,
                    "task_id": task.get("id"),
                    "name": task.get("name"),
                    "args": task.get("args"),
                    "kwargs": task.get("kwargs"),
                    "started_at": task.get("time_start"),
                })

        return {"active_tasks": tasks, "count": len(tasks)}

    @staticmethod
    def get_scheduled_tasks():
        """Get all scheduled/queued tasks"""
        inspector = celery_app.control.inspect()
        scheduled_tasks = inspector.scheduled()

        if not scheduled_tasks:
            return {"scheduled_tasks": [], "count": 0}

        tasks = []
        for worker, task_list in scheduled_tasks.items():
            for task in task_list:
                tasks.append({
                    "worker": worker,
                    "task_id": task.get("request", {}).get("id"),
                    "name": task.get("request", {}).get("name"),
                    "eta": task.get("eta"),
                })

        return {"scheduled_tasks": tasks, "count": len(tasks)}

    @staticmethod
    def get_all_workers():
        """Get all available Celery workers"""
        inspector = celery_app.control.inspect()

        # Get worker stats
        stats = inspector.stats()
        # Get active queues
        active_queues = inspector.active_queues()

        if not stats:
            return {"workers": [], "count": 0}

        workers = []
        for worker_name in stats.keys():
            worker_info = {
                "name": worker_name,
                "status": "online",
                "stats": stats.get(worker_name, {}),
            }

            # Add queue info if available
            if active_queues and worker_name in active_queues:
                worker_info["queues"] = active_queues[worker_name]

            workers.append(worker_info)

        return {"workers": workers, "count": len(workers)}

# Add these methods to JobControlService class

    @staticmethod
    def pause_task(task_name: str):
        """
        Pause a specific task type (welcome_email, reminder_email, cleanup)
        Paused tasks will not execute even if triggered
        """
        available_tasks = ["welcome_email", "reminder_email", "cleanup"]

        if task_name not in available_tasks:
            return {
                "error": True,
                "message": f"Invalid task name. Available: {', '.join(available_tasks)}"
            }

        db = Sessionlocal()
        try:
            repo = TaskControlRepository(db)
            task_control = repo.create_or_update(task_name, is_paused=True)

            return {
                "task_name": task_name,
                "is_paused": True,
                "paused_at": task_control.paused_at,
                "message": f"Task '{task_name}' has been paused"
            }
        finally:
            db.close()

    @staticmethod
    def resume_task(task_name: str):
        """
        Resume a paused task
        """
        available_tasks = ["welcome_email", "reminder_email", "cleanup"]

        if task_name not in available_tasks:
            return {
                "error": True,
                "message": f"Invalid task name. Available: {', '.join(available_tasks)}"
            }

        db = Sessionlocal()
        try:
            repo = TaskControlRepository(db)
            task_control = repo.create_or_update(task_name, is_paused=False)

            return {
                "task_name": task_name,
                "is_paused": False,
                "message": f"Task '{task_name}' has been resumed"
            }
        finally:
            db.close()

    @staticmethod
    def get_paused_tasks():
        """
        Get all paused tasks status
        """
        db = Sessionlocal()
        try:
            repo = TaskControlRepository(db)
            all_controls = repo.get_all()

            result = []
            for control in all_controls:
                result.append({
                    "task_name": control.task_name,
                    "is_paused": control.is_paused,
                    "paused_at": control.paused_at
                })

            return {"tasks": result, "count": len(result)}
        finally:
            db.close()
