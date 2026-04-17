import React from "react";

function ResponseDisplay({ title, response, error, loading }) {
  if (loading) {
    return (
      <div style={styles.container}>
        <h4>{title}</h4>
        <div style={styles.loading}>Loading...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div style={styles.container}>
        <h4>{title}</h4>
        <pre style={styles.error}>{JSON.stringify(error, null, 2)}</pre>
      </div>
    );
  }

  if (!response) {
    return (
      <div style={styles.container}>
        <h4>{title}</h4>
        <div style={styles.empty}>No response yet</div>
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <h4>{title}</h4>
      <pre style={styles.success}>{JSON.stringify(response, null, 2)}</pre>
    </div>
  );
}

const styles = {
  container: {
    marginTop: "20px",
    padding: "15px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f9f9f9",
  },
  loading: {
    color: "#2196F3",
    fontStyle: "italic",
  },
  error: {
    color: "#f44336",
    backgroundColor: "#ffebee",
    padding: "10px",
    borderRadius: "4px",
    overflowX: "auto",
  },
  success: {
    color: "#4CAF50",
    backgroundColor: "#e8f5e9",
    padding: "10px",
    borderRadius: "4px",
    overflowX: "auto",
  },
  empty: {
    color: "#999",
    fontStyle: "italic",
  },
};

export default ResponseDisplay;
