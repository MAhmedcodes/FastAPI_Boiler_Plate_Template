from pydantic import BaseModel
from typing import Optional, Any, List


class TaskRevokeRequest(BaseModel):
    task_id: str
    terminate: bool = False  # Force kill if True


class TaskStatusResponse(BaseModel):
    task_id: str
    status: str
    ready: bool
    successful: Optional[bool] = None
    failed: Optional[bool] = None
    result: Optional[Any] = None
    error: Optional[str] = None


class TriggerJobResponse(BaseModel):
    task_id: str
    status: str
    message: str


class RevokeTaskResponse(BaseModel):
    task_id: str
    terminate: bool
    status: str
    message: str


class ActiveTasksResponse(BaseModel):
    active_tasks: List[dict]
    count: int


class WorkersResponse(BaseModel):
    workers: List[dict]
    count: int


class TaskNameRequest(BaseModel):
    task_name: str
