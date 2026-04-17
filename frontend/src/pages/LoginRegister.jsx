import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  register,
  login,
  getGoogleAuthUrl,
  getGithubAuthUrl,
} from "../api/auth";
import ResponseDisplay from "../components/common/ResponseDisplay";

function LoginRegister() {
  const navigate = useNavigate();
  const [isLogin, setIsLogin] = useState(true);
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  // Form states
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [inviteToken, setInviteToken] = useState("");
  const [orgId, setOrgId] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      if (isLogin) {
        // Login
        const res = await login(email, password, parseInt(orgId) || 1);
        setResponse(res.data);
        // Save token
        if (res.data.access_token) {
          localStorage.setItem("access_token", res.data.access_token);
          localStorage.setItem("organization_id", res.data.organization_id);
        }
      } else {
        // Register
        const res = await register({
          email,
          password,
          first_name: firstName,
          last_name: lastName,
          invite_token: inviteToken,
        });
        setResponse(res.data);
        // Save token and navigate to OTP page
        if (res.data.access_token) {
          localStorage.setItem("access_token", res.data.access_token);
          navigate("/otp");
        }
      }
    } catch (err) {
      setError(err.response?.data || { message: err.message });
    } finally {
      setLoading(false);
    }
  };

  const handleGoogleLogin = () => {
    window.location.href = getGoogleAuthUrl(inviteToken);
  };

  const handleGithubLogin = () => {
    window.location.href = getGithubAuthUrl(inviteToken);
  };

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <h1>{isLogin ? "Login" : "Register"}</h1>

        <div style={styles.toggle}>
          <button
            style={{ ...styles.toggleBtn, ...(isLogin ? styles.active : {}) }}
            onClick={() => setIsLogin(true)}
          >
            Login
          </button>
          <button
            style={{ ...styles.toggleBtn, ...(!isLogin ? styles.active : {}) }}
            onClick={() => setIsLogin(false)}
          >
            Register
          </button>
        </div>

        <form onSubmit={handleSubmit} style={styles.form}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={styles.input}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={styles.input}
          />

          {!isLogin && (
            <>
              <input
                type="text"
                placeholder="First Name"
                value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                required
                style={styles.input}
              />
              <input
                type="text"
                placeholder="Last Name"
                value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
                style={styles.input}
              />
              <input
                type="text"
                placeholder="Invite Token"
                value={inviteToken}
                onChange={(e) => setInviteToken(e.target.value)}
                required
                style={styles.input}
              />
            </>
          )}

          {isLogin && (
            <input
              type="number"
              placeholder="Organization ID"
              value={orgId}
              onChange={(e) => setOrgId(e.target.value)}
              required
              style={styles.input}
            />
          )}

          <button type="submit" style={styles.submitBtn} disabled={loading}>
            {loading ? "Processing..." : isLogin ? "Login" : "Register"}
          </button>
        </form>

        <div style={styles.divider}>OR</div>

        <div style={styles.oauthButtons}>
          <button
            onClick={handleGoogleLogin}
            style={{ ...styles.oauthBtn, ...styles.google }}
          >
            Sign in with Google
          </button>
          <button
            onClick={handleGithubLogin}
            style={{ ...styles.oauthBtn, ...styles.github }}
          >
            Sign in with GitHub
          </button>
        </div>

        <ResponseDisplay
          title="Response"
          response={response}
          error={error}
          loading={loading}
        />
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
    width: "450px",
  },
  toggle: {
    display: "flex",
    marginBottom: "20px",
    borderBottom: "1px solid #ddd",
  },
  toggleBtn: {
    flex: 1,
    padding: "10px",
    border: "none",
    backgroundColor: "transparent",
    cursor: "pointer",
    fontSize: "16px",
  },
  active: {
    borderBottom: "2px solid #4CAF50",
    color: "#4CAF50",
  },
  form: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },
  input: {
    padding: "12px",
    border: "1px solid #ddd",
    borderRadius: "5px",
    fontSize: "14px",
  },
  submitBtn: {
    padding: "12px",
    backgroundColor: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "16px",
    marginTop: "10px",
  },
  divider: {
    textAlign: "center",
    margin: "20px 0",
    color: "#999",
  },
  oauthButtons: {
    display: "flex",
    flexDirection: "column",
    gap: "10px",
  },
  oauthBtn: {
    padding: "12px",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "14px",
    color: "white",
  },
  google: {
    backgroundColor: "#DB4437",
  },
  github: {
    backgroundColor: "#333",
  },
};

export default LoginRegister;
