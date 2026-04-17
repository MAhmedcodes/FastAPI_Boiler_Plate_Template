import React from "react";
import { Link } from "react-router-dom";

function Home() {
  const token = localStorage.getItem("access_token");
  const isAuthenticated = !!token;

  return (
    <div style={styles.container}>
      <h1>FastAPI Boilerplate</h1>
      <p>Welcome to the API Testing Dashboard</p>

      <div style={styles.stats}>
        <div style={styles.statCard}>
          <h3>Authentication Status</h3>
          <p style={{ color: isAuthenticated ? "#4CAF50" : "#f44336" }}>
            {isAuthenticated ? "✅ Logged In" : "❌ Not Logged In"}
          </p>
        </div>
      </div>

      <div style={styles.menu}>
        <div style={styles.section}>
          <h2>Quick Links</h2>
          <div style={styles.buttonGroup}>
            {!isAuthenticated && (
              <Link to="/auth" style={styles.button}>
                Login / Register
              </Link>
            )}
            <Link to="/organizations" style={styles.button}>
              Organizations
            </Link>
            <Link to="/jobs" style={styles.button}>
              Jobs Control
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}

const styles = {
  container: {
    maxWidth: "800px",
    margin: "0 auto",
    padding: "40px",
    textAlign: "center",
  },
  stats: {
    marginBottom: "30px",
  },
  statCard: {
    backgroundColor: "white",
    padding: "20px",
    borderRadius: "10px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
  },
  menu: {
    marginTop: "40px",
  },
  section: {
    marginBottom: "30px",
    padding: "20px",
    border: "1px solid #ddd",
    borderRadius: "8px",
    backgroundColor: "#f5f5f5",
  },
  buttonGroup: {
    display: "flex",
    gap: "15px",
    justifyContent: "center",
    marginTop: "15px",
    flexWrap: "wrap",
  },
  button: {
    display: "inline-block",
    padding: "10px 20px",
    backgroundColor: "#4CAF50",
    color: "white",
    textDecoration: "none",
    borderRadius: "5px",
    cursor: "pointer",
  },
};

export default Home;
