import React, { useState } from "react";
import {
  getOrganizations,
  createOrganization,
  joinOrganization,
} from "../api/organizations";
import ResponseDisplay from "../components/common/ResponseDisplay";

function Organizations() {
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  // Form states
  const [orgName, setOrgName] = useState("");
  const [orgId, setOrgId] = useState("");
  const [inviteLinks, setInviteLinks] = useState(null);

  const handleGetOrganizations = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await getOrganizations();
      setResponse(res.data);
    } catch (err) {
      setError(err.response?.data || { message: err.message });
    } finally {
      setLoading(false);
    }
  };

  const handleCreateOrganization = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await createOrganization(orgName);
      setResponse(res.data);
      setOrgName("");
    } catch (err) {
      setError(err.response?.data || { message: err.message });
    } finally {
      setLoading(false);
    }
  };

  const handleJoinOrganization = async () => {
    setLoading(true);
    setError(null);
    setInviteLinks(null);

    try {
      const res = await joinOrganization(parseInt(orgId));
      setInviteLinks(res.data);
    } catch (err) {
      setError(err.response?.data || { message: err.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={styles.container}>
      <h1>Organizations Management</h1>

      <div style={styles.grid}>
        {/* Get Organizations Section */}
        <div style={styles.card}>
          <h2>Get All Organizations</h2>
          <button
            onClick={handleGetOrganizations}
            style={styles.button}
            disabled={loading}
          >
            Fetch Organizations
          </button>
        </div>

        {/* Create Organization Section */}
        <div style={styles.card}>
          <h2>Create Organization</h2>
          <input
            type="text"
            placeholder="Organization Name"
            value={orgName}
            onChange={(e) => setOrgName(e.target.value)}
            style={styles.input}
          />
          <button
            onClick={handleCreateOrganization}
            style={styles.button}
            disabled={loading || !orgName}
          >
            Create
          </button>
        </div>

        {/* Join Organization Section */}
        <div style={styles.card}>
          <h2>Join Organization</h2>
          <input
            type="number"
            placeholder="Organization ID"
            value={orgId}
            onChange={(e) => setOrgId(e.target.value)}
            style={styles.input}
          />
          <button
            onClick={handleJoinOrganization}
            style={styles.button}
            disabled={loading || !orgId}
          >
            Get Invite Links
          </button>

          {inviteLinks && (
            <div style={styles.inviteLinks}>
              <h4>Invite Links:</h4>
              <p>
                <strong>Invite Token:</strong> {inviteLinks.invite_token}
              </p>
              <p>
                <strong>Google:</strong>{" "}
                <a href={inviteLinks.google_invite_link} target="_blank">
                  {inviteLinks.google_invite_link}
                </a>
              </p>
              <p>
                <strong>GitHub:</strong>{" "}
                <a href={inviteLinks.github_invite_link} target="_blank">
                  {inviteLinks.github_invite_link}
                </a>
              </p>
            </div>
          )}
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
  button: {
    width: "100%",
    padding: "10px",
    backgroundColor: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "14px",
  },
  inviteLinks: {
    marginTop: "15px",
    padding: "10px",
    backgroundColor: "#e8f5e9",
    borderRadius: "5px",
    fontSize: "12px",
    wordBreak: "break-all",
  },
};

export default Organizations;
