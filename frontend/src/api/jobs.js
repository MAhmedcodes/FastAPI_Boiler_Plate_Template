import apiClient from "./client";

// Get all workers
export const getWorkers = () => {
  return apiClient.get("/jobs/workers");
};

// Get active tasks
export const getActiveTasks = () => {
  return apiClient.get("/jobs/active");
};

// Trigger cleanup job
export const triggerCleanup = () => {
  return apiClient.post("/jobs/trigger/cleanup");
};

// Get task status
export const getTaskStatus = (taskId) => {
  return apiClient.get(`/jobs/task/${taskId}`);
};

// Revoke task
export const revokeTask = (taskId, terminate = false) => {
  return apiClient.post("/jobs/task/revoke", { task_id: taskId, terminate });
};

// Pause task
export const pauseTask = (taskName) => {
  return apiClient.post("/jobs/pause", { task_name: taskName });
};

// Resume task
export const resumeTask = (taskName) => {
  return apiClient.post("/jobs/resume", { task_name: taskName });
};

// Get paused tasks
export const getPausedTasks = () => {
  return apiClient.get("/jobs/paused");
};
