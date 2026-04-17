import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { logout, getCurrentUser } from "../api/auth";
import ResponseDisplay from "../components/common/ResponseDisplay";

function Logout() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Get current user info
    const fetchUser = async () => {
      try {
        const res = await getCurrentUser();
        setUser(res.data);
      } catch (err) {
        console.error("Failed to get user:", err);
      }
    };
    fetchUser();
  }, []);

  const handleLogout = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await logout();
      setResponse(res.data);
      // Clear token
      localStorage.removeItem("access_token");
      localStorage.removeItem("organization_id");
      // Redirect to home after 2 seconds
      setTimeout(() => {
        navigate("/");
      }, 2000);
    } catch (err) {
      setError(err.response?.data || { message: err.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1>Logout</h1>

        {user && (
          <div style={styles.userInfo}>
            <p>
              <strong>Logged in as:</strong> {user.email}
            </p>
            <p>
              <strong>Name:</strong> {user.first_name} {user.last_name}
            </p>
            <p>
              <strong>Organization ID:</strong> {user.organization_id}
            </p>
          </div>
        )}

        <button onClick={handleLogout} style={styles.button} disabled={loading}>
          {loading ? "Logging out..." : "Logout"}
        </button>

        <ResponseDisplay
          title="Logout Response"
          response={response}
          error={error}
          loading={loading}
        />

        {response?.message === "Successfully logged out" && (
          <div style={styles.successMessage}>
            ✅ Logged out successfully! Redirecting to home page...
          </div>
        )}
      </div>
    </div>
  );
}

const styles = {
  container: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    minHeight: "100vh",
    backgroundColor: "#f0f2f5",
  },
  card: {
    backgroundColor: "white",
    padding: "40px",
    borderRadius: "10px",
    boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
    width: "500px",
    textAlign: "center",
  },
  userInfo: {
    backgroundColor: "#e3f2fd",
    padding: "15px",
    borderRadius: "5px",
    marginBottom: "20px",
    textAlign: "left",
  },
  button: {
    width: "100%",
    padding: "12px",
    backgroundColor: "#f44336",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "16px",
  },
  successMessage: {
    marginTop: "20px",
    padding: "10px",
    backgroundColor: "#e8f5e9",
    color: "#4CAF50",
    borderRadius: "5px",
  },
};

export default Logout;
