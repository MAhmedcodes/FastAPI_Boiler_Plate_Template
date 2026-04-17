import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { requestOTP, verifyOTP } from "../api/auth";
import ResponseDisplay from "../components/common/ResponseDisplay";

function OTPVerification() {
  const navigate = useNavigate();
  const [step, setStep] = useState("request"); // 'request' or 'verify'
  const [otpCode, setOtpCode] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const handleRequestOTP = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await requestOTP();
      setResponse(res.data);
      setStep("verify");
    } catch (err) {
      setError(err.response?.data || { message: err.message });
    } finally {
      setLoading(false);
    }
  };

  const handleVerifyOTP = async () => {
    setLoading(true);
    setError(null);
    setResponse(null);

    try {
      const res = await verifyOTP(otpCode);
      setResponse(res.data);
      // Navigate to logout page after successful verification
      setTimeout(() => {
        navigate("/logout");
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
        <h1>Email Verification</h1>

        {step === "request" ? (
          <div>
            <p>Click the button below to request an OTP verification code.</p>
            <button
              onClick={handleRequestOTP}
              style={styles.button}
              disabled={loading}
            >
              {loading ? "Sending..." : "Get OTP"}
            </button>
          </div>
        ) : (
          <div>
            <p>Enter the OTP code sent to your email:</p>
            <input
              type="text"
              placeholder="Enter 6-digit OTP"
              value={otpCode}
              onChange={(e) =>
                setOtpCode(e.target.value.replace(/\D/g, "").slice(0, 6))
              }
              maxLength={6}
              style={styles.input}
            />
            <button
              onClick={handleVerifyOTP}
              style={styles.button}
              disabled={loading || !otpCode}
            >
              {loading ? "Verifying..." : "Verify OTP"}
            </button>
          </div>
        )}

        <ResponseDisplay
          title="Response"
          response={response}
          error={error}
          loading={loading}
        />

        {response?.message === "User verified successfully" && (
          <div style={styles.successMessage}>
            ✅ Verification successful! Redirecting to logout page...
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
    width: "450px",
    textAlign: "center",
  },
  input: {
    width: "100%",
    padding: "12px",
    margin: "10px 0",
    border: "1px solid #ddd",
    borderRadius: "5px",
    fontSize: "16px",
    textAlign: "center",
  },
  button: {
    width: "100%",
    padding: "12px",
    backgroundColor: "#4CAF50",
    color: "white",
    border: "none",
    borderRadius: "5px",
    cursor: "pointer",
    fontSize: "16px",
    marginTop: "10px",
  },
  successMessage: {
    marginTop: "20px",
    padding: "10px",
    backgroundColor: "#e8f5e9",
    color: "#4CAF50",
    borderRadius: "5px",
  },
};

export default OTPVerification;
