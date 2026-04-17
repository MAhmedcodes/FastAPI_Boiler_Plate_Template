from fastapi import APIRouter, HTTPException, status
from app.modules.jobs.services.job_control_service import JobControlService
from app.modules.jobs.schema.schema import (
    TriggerJobResponse,
    RevokeTaskResponse,
    TaskStatusResponse,
    ActiveTasksResponse,
    WorkersResponse,
    TaskRevokeRequest,
    TaskNameRequest
)

router = APIRouter(prefix="/jobs", tags=["Job Control"])


@router.post("/trigger/cleanup", response_model=TriggerJobResponse)
async def trigger_cleanup_job():
    """
    Manually trigger the cleanup job
    Useful for testing or on-demand cleanup
    """
    try:
        result = JobControlService.trigger_cleanup_job()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to trigger cleanup job: {str(e)}"
        )


@router.post("/task/revoke", response_model=RevokeTaskResponse)
async def revoke_task(request: TaskRevokeRequest):
    """
    Revoke/stop a running task by its ID
    Set terminate=True to forcefully kill the task
    """
    try:
        result = JobControlService.revoke_task(
            request.task_id, request.terminate)
        if result.get("status") == "failed":
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=result.get("error")
            )
        return result
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to revoke task: {str(e)}"
        )


@router.get("/task/{task_id}", response_model=TaskStatusResponse)
async def get_task_status(task_id: str):
    """
    Get status of a specific task by its ID
    """
    try:
        result = JobControlService.get_task_status(task_id)
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get task status: {str(e)}"
        )


@router.get("/active", response_model=ActiveTasksResponse)
async def get_active_tasks():
    """
    Get all currently running tasks
    """
    try:
        result = JobControlService.get_active_tasks()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get active tasks: {str(e)}"
        )


@router.get("/workers", response_model=WorkersResponse)
async def get_workers():
    """
    Get all available Celery workers and their status
    """
    try:
        result = JobControlService.get_all_workers()
        return result
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to get workers: {str(e)}"
        )


@router.post("/pause")
def pause_task(request: TaskNameRequest):
    """
    Pause a task (welcome_email, reminder_email, or cleanup)
    """
    result = JobControlService.pause_task(request.task_name)
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["message"])
    return result


@router.post("/resume")
def resume_task(request: TaskNameRequest):
    """
    Resume a paused task
    """
    result = JobControlService.resume_task(request.task_name)
    if result.get("error"):
        raise HTTPException(status_code=400, detail=result["message"])
    return result


@router.get("/paused")
def get_paused_tasks():
    """
    Get all paused tasks
    """
    return JobControlService.get_paused_tasks()
