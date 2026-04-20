import apiClient from "./client";

// Email/Password Register
export const register = (userData) => {
  return apiClient.post("/users/register", userData);
};

// Email/Password Login
export const login = (username, password, organization_id) => {
  const formData = new URLSearchParams();
  formData.append("username", username);
  formData.append("password", password);
  formData.append("organization_id", organization_id);

  return apiClient.post("/auth/login", formData, {
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
  });
};

// Request OTP
export const requestOTP = () => {
  return apiClient.post("/auth/request-verification");
};

// Verify OTP
export const verifyOTP = (otp_code) => {
  return apiClient.post("/auth/verify-otp", { otp_code });
};

// Get Current User
export const getCurrentUser = () => {
  return apiClient.get("/users/me");
};

// Logout
export const logout = () => {
  return apiClient.post("/users/logout");
};

// Google OAuth URL
export const getGoogleAuthUrl = (inviteToken = "") => {
  if (inviteToken) {
    return `http://localhost:8000/auth/google/login?invite_token=${inviteToken}`;
  }
  return "http://localhost:8000/auth/google/login";
};

// GitHub OAuth URL
export const getGithubAuthUrl = (inviteToken = "") => {
  if (inviteToken) {
    return `http://localhost:8000/auth/github/login?invite_token=${inviteToken}`;
  }
  return "http://localhost:8000/auth/github/login";
};
