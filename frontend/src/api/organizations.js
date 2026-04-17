import apiClient from "./client";

// Get all organizations
export const getOrganizations = () => {
  return apiClient.get("/organizations/");
};

// Create organization
export const createOrganization = (name) => {
  return apiClient.post("/organizations/create", { name });
};

// Join organization (get invite links)
export const joinOrganization = (organization_id) => {
  return apiClient.post("/organizations/join", { organization_id });
};
