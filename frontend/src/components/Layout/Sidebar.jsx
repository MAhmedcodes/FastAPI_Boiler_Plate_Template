import React from "react";
import { NavLink } from "react-router-dom";

function Sidebar() {
  const menuItems = [
    { path: "/", name: "Dashboard", icon: "🏠" },
    { path: "/auth", name: "Login / Register", icon: "🔐" },
    { path: "/organizations", name: "Organizations", icon: "🏢" },
    { path: "/jobs", name: "Jobs Control", icon: "⚙️" },
  ];

  return (
    <aside style={styles.sidebar}>
      <div style={styles.sidebarHeader}>
        <h3>Menu</h3>
      </div>

      <nav style={styles.nav}>
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            style={({ isActive }) => ({
              ...styles.navLink,
              ...(isActive ? styles.activeNavLink : {}),
            })}
          >
            <span style={styles.icon}>{item.icon}</span>
            <span>{item.name}</span>
          </NavLink>
        ))}
      </nav>
    </aside>
  );
}

const styles = {
  sidebar: {
    width: "250px",
    backgroundColor: "#34495e",
    color: "white",
    height: "calc(100vh - 60px)",
    position: "fixed",
    left: 0,
    top: "60px",
    overflowY: "auto",
  },
  sidebarHeader: {
    padding: "20px",
    borderBottom: "1px solid #3d566e",
    textAlign: "center",
  },
  nav: {
    padding: "10px 0",
  },
  navLink: {
    display: "flex",
    alignItems: "center",
    gap: "12px",
    padding: "12px 20px",
    color: "#ecf0f1",
    textDecoration: "none",
    transition: "background-color 0.3s",
  },
  activeNavLink: {
    backgroundColor: "#2c3e50",
    borderLeft: "4px solid #4CAF50",
  },
  icon: {
    fontSize: "18px",
  },
};

export default Sidebar;
