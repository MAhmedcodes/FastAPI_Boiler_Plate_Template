import React from "react";
import Header from "./Header";
import Sidebar from "./Sidebar";

function Layout({ children }) {
  const token = localStorage.getItem("access_token");
  const isAuthenticated = !!token;

  return (
    <div style={styles.container}>
      <Header />

      <div style={styles.mainContainer}>
        {isAuthenticated && <Sidebar />}

        <main
          style={{
            ...styles.content,
            ...(isAuthenticated
              ? styles.contentWithSidebar
              : styles.contentWithoutSidebar),
          }}
        >
          {children}
        </main>
      </div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: "100vh",
    backgroundColor: "#f5f6fa",
  },
  mainContainer: {
    display: "flex",
  },
  contentWithSidebar: {
    marginLeft: "250px",
    padding: "20px",
    width: "calc(100% - 250px)",
  },
  contentWithoutSidebar: {
    marginLeft: 0,
    padding: "20px",
    width: "100%",
  },
};

export default Layout;
