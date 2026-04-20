import React from "react";
import { Link, useNavigate } from "react-router-dom";

function Header() {
  const navigate = useNavigate();
  const token = localStorage.getItem("access_token");
  const isAuthenticated = !!token;

  const handleLogout = () => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("organization_id");
    navigate("/");
  };

  return (
    <header style={styles.header}>
      <div style={styles.logo}>
        <Link to="/" style={styles.logoLink}>
          FastAPI Boilerplate
        </Link>
      </div>

      <nav style={styles.nav}>
        <Link to="/organizations" style={styles.navLink}>
          Organizations
        </Link>
        <Link to="/jobs" style={styles.navLink}>
          Jobs
        </Link>

        {isAuthenticated ? (
          <button onClick={handleLogout} style={styles.logoutBtn}>
            Logout
          </button>
        ) : (
          <Link to="/auth" style={styles.navLink}>
            Login
          </Link>
        )}
      </nav>
    </header>
  );
}

const styles = {
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "15px 30px",
    backgroundColor: "#2c3e50",
    color: "white",
    boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
  },
  logo: {
    fontSize: "20px",
    fontWeight: "bold",
  },
  logoLink: {
    color: "white",
    textDecoration: "none",
  },
  nav: {
    display: "flex",
    gap: "20px",
    alignItems: "center",
  },
  navLink: {
    color: "white",
    textDecoration: "none",
    padding: "8px 15px",
    borderRadius: "5px",
    transition: "background-color 0.3s",
  },
  logoutBtn: {
    backgroundColor: "#e74c3c",
    color: "white",
    border: "none",
    padding: "8px 15px",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "14px",
  },
};

export default Header;
