import React, { useState } from "react";
import {
  getWorkers,
  getActiveTasks,
  triggerCleanup,
  getTaskStatus,
  revokeTask,
  pauseTask,
  resumeTask,
  getPausedTasks,
} from "../api/jobs";
import ResponseDisplay from "../components/common/ResponseDisplay";

function Jobs() {
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  // Form states
  const [taskId, setTaskId] = useState("");
  const [taskName, setTaskName] = useState("welcome_email");

  const apiCalls = {
    getWorkers: async () => {
      setLoading(true);
      try {
        const res = await getWorkers();
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    getActiveTasks: async () => {
      setLoading(true);
      try {
        const res = await getActiveTasks();
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    triggerCleanup: async () => {
      setLoading(true);
      try {
        const res = await triggerCleanup();
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    getTaskStatus: async () => {
      if (!taskId) return;
      setLoading(true);
      try {
        const res = await getTaskStatus(taskId);
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    revokeTask: async () => {
      if (!taskId) return;
      setLoading(true);
      try {
        const res = await revokeTask(taskId, true);
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    pauseTask: async () => {
      setLoading(true);
      try {
        const res = await pauseTask(taskName);
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    resumeTask: async () => {
      setLoading(true);
      try {
        const res = await resumeTask(taskName);
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
    getPausedTasks: async () => {
      setLoading(true);
      try {
        const res = await getPausedTasks();
        setResponse(res.data);
      } catch (err) {
        setError(err.response?.data);
      } finally {
        setLoading(false);
      }
    },
  };

  return (
    <div style={styles.container}>
      <h1>Jobs Control Panel</h1>

      <div style={styles.grid}>
        {/* Worker Management */}
        <div style={styles.card}>
          <h2>Workers</h2>
          <button onClick={apiCalls.getWorkers} style={styles.button}>
            Get Workers
          </button>
          <button onClick={apiCalls.getActiveTasks} style={styles.button}>
            Get Active Tasks
          </button>
        </div>

        {/* Cleanup Jobs */}
        <div style={styles.card}>
          <h2>Cleanup Jobs</h2>
          <button onClick={apiCalls.triggerCleanup} style={styles.button}>
            Trigger Cleanup
          </button>
        </div>

        {/* Task Control */}
        <div style={styles.card}>
          <h2>Task Control</h2>
          <input
            type="text"
            placeholder="Task ID"
            value={taskId}
            onChange={(e) => setTaskId(e.target.value)}
            style={styles.input}
          />
          <button
            onClick={apiCalls.getTaskStatus}
            style={styles.button}
            disabled={!taskId}
          >
            Get Status
          </button>
          <button
            onClick={apiCalls.revokeTask}
            style={{ ...styles.button, backgroundColor: "#f44336" }}
            disabled={!taskId}
          >
            Revoke Task
          </button>
        </div>

        {/* Pause/Resume */}
        <div style={styles.card}>
          <h2>Pause / Resume Tasks</h2>
          <select
            value={taskName}
            onChange={(e) => setTaskName(e.target.value)}
            style={styles.select}
          >
            <option value="welcome_email">Welcome Email</option>
            <option value="reminder_email">Reminder Email</option>
            <option value="cleanup">Cleanup</option>
          </select>
          <button
            onClick={apiCalls.pauseTask}
            style={{ ...styles.button, backgroundColor: "#FF9800" }}
          >
            Pause
          </button>
          <button
            onClick={apiCalls.resumeTask}
            style={{ ...styles.button, backgroundColor: "#4CAF50" }}
          >
            Resume
          </button>
          <button onClick={apiCalls.getPausedTasks} style={styles.button}>
            Get Paused Tasks
          </button>
        </div>
      </div>

      <ResponseDisplay
        title="API Response"
        response={response}
        error={error}
        loading={loading}
      />
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "1200px",
    margin: "0 auto",
    padding: "40px",
  },
  grid: {
    display: "grid",
    gridTemplateColumns: "repeat(auto-fit, minmax(350px, 1fr))",
    gap: "20px",
    marginBottom: "30px",
  },
  card: {
    padding: "20px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f9f9f9",
  },
  input: {
    width: "100%",
    padding: "10px",
    margin: "10px 0",
    border: "1px solid #ddd",
    borderRadius: "5px",
    fontSize: "14px",
  },
  select: {
    width: "100%",
    padding: "10px",
    margin: "10px 0",
    border: "1px solid #ddd",
    borderRadius: "5px",
    fontSize: "14px",
  },
  button: {
    width: "100%",
    padding: "10px",
    margin: "5px 0",
    backgroundColor: "#2196F3",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "14px",
  },
};

export default Jobs;
