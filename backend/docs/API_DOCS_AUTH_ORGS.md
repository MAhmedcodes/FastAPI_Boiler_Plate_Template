# API Documentation - Authentication & Organizations

## Table of Contents

- [Overview](#overview)
- [Base URL](#base-url)
- [Authentication](#authentication)
- [Common Response Codes](#common-response-codes)
- [Authentication Endpoints](#authentication-endpoints)
- [OAuth Endpoints](#oauth-endpoints)
- [Organization Endpoints](#organization-endpoints)
- [Error Handling](#error-handling)

---

## Overview

This document covers all authentication and organization management endpoints for the FastAPI SaaS Boilerplate. All endpoints follow RESTful conventions and return JSON responses.

---

## Base URL

```
Development: http://localhost:8000/api/v1
Production: https://api.yourdomain.com/api/v1
```

---

## Authentication

Most endpoints require a valid JWT token in the Authorization header:

```http
Authorization: Bearer <your_jwt_token>
```

### Token Expiration

- **Access Token**: 30 minutes (default)
- **Refresh Token**: 7 days (if implemented)

---

## Common Response Codes

| Code | Description                                      |
| ---- | ------------------------------------------------ |
| 200  | Success - Request completed successfully         |
| 201  | Created - Resource created successfully          |
| 400  | Bad Request - Invalid input data                 |
| 401  | Unauthorized - Missing or invalid token          |
| 403  | Forbidden - Insufficient permissions             |
| 404  | Not Found - Resource doesn't exist               |
| 409  | Conflict - Resource already exists               |
| 422  | Unprocessable Entity - Validation error          |
| 429  | Too Many Requests - Rate limit exceeded          |
| 500  | Internal Server Error - Server error occurred    |

---

## Authentication Endpoints

### 1. Register User

Create a new user account with email verification.

**Endpoint:** `POST /auth/register`

**Rate Limit:** 3 requests/minute

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "full_name": "John Doe",
  "invite_token": "optional-org-invite-token"
}
```

**Request Fields:**

| Field        | Type   | Required | Description                                |
| ------------ | ------ | -------- | ------------------------------------------ |
| email        | string | Yes      | Valid email address (unique per org)       |
| password     | string | Yes      | Min 8 chars, 1 uppercase, 1 number, 1 special |
| full_name    | string | Yes      | User's full name                           |
| invite_token | string | No       | Organization invite token (join existing)  |

**Success Response:** `201 Created`

```json
{
  "message": "User registered successfully. Please verify your email.",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_verified": false,
    "organization_id": "660e8400-e29b-41d4-a716-446655440001",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "organization": {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "name": "John Doe's Organization",
    "invite_token": "johndoe-a1b2c3"
  }
}
```

**Error Responses:**

```json
// 409 Conflict - User already exists
{
  "detail": "User with this email already exists in this organization"
}

// 400 Bad Request - Invalid invite token
{
  "detail": "Invalid invite token"
}

// 422 Validation Error - Weak password
{
  "detail": [
    {
      "loc": ["body", "password"],
      "msg": "Password must contain at least one uppercase letter",
      "type": "value_error"
    }
  ]
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!",
    "full_name": "John Doe"
  }'
```

---

### 2. Login

Authenticate user and receive JWT tokens.

**Endpoint:** `POST /auth/login`

**Rate Limit:** 5 requests/minute

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "organization_id": "optional-org-id"
}
```

**Request Fields:**

| Field           | Type   | Required | Description                              |
| --------------- | ------ | -------- | ---------------------------------------- |
| email           | string | Yes      | User's email address                     |
| password        | string | Yes      | User's password                          |
| organization_id | string | No       | Specific org to login to (multi-org users) |

**Success Response:** `200 OK`

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_verified": true,
    "organization_id": "660e8400-e29b-41d4-a716-446655440001"
  }
}
```

**Error Responses:**

```json
// 401 Unauthorized - Invalid credentials
{
  "detail": "Incorrect email or password"
}

// 403 Forbidden - Email not verified
{
  "detail": "Please verify your email before logging in"
}

// 400 Bad Request - Multiple organizations
{
  "detail": "User belongs to multiple organizations. Please specify organization_id",
  "organizations": [
    {
      "id": "660e8400-e29b-41d4-a716-446655440001",
      "name": "Acme Corp"
    },
    {
      "id": "770e8400-e29b-41d4-a716-446655440002",
      "name": "Beta Inc"
    }
  ]
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "SecurePass123!"
  }'
```

---

### 3. Verify Email

Verify user's email address with OTP code.

**Endpoint:** `POST /auth/verify-email`

**Rate Limit:** 10 requests/minute

**Request Body:**

```json
{
  "email": "user@example.com",
  "otp_code": "123456"
}
```

**Request Fields:**

| Field    | Type   | Required | Description                    |
| -------- | ------ | -------- | ------------------------------ |
| email    | string | Yes      | User's email address           |
| otp_code | string | Yes      | 6-digit verification code      |

**Success Response:** `200 OK`

```json
{
  "message": "Email verified successfully",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "is_verified": true
  }
}
```

**Error Responses:**

```json
// 400 Bad Request - Invalid OTP
{
  "detail": "Invalid or expired OTP code"
}

// 404 Not Found - User not found
{
  "detail": "User not found"
}

// 400 Bad Request - Already verified
{
  "detail": "Email already verified"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/auth/verify-email" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "otp_code": "123456"
  }'
```

---

### 4. Resend OTP

Request a new OTP code via email.

**Endpoint:** `POST /auth/resend-otp`

**Rate Limit:** 3 requests/5 minutes

**Request Body:**

```json
{
  "email": "user@example.com"
}
```

**Success Response:** `200 OK`

```json
{
  "message": "OTP sent successfully to user@example.com"
}
```

**Error Responses:**

```json
// 404 Not Found
{
  "detail": "User not found"
}

// 400 Bad Request - Already verified
{
  "detail": "Email already verified"
}

// 429 Too Many Requests
{
  "detail": "Please wait 5 minutes before requesting a new OTP"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/auth/resend-otp" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com"
  }'
```

---

### 5. Get Current User

Retrieve authenticated user's information.

**Endpoint:** `GET /auth/me`

**Authentication:** Required

**Success Response:** `200 OK`

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_verified": true,
  "provider": "email",
  "organization": {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "name": "Acme Corp",
    "invite_token": "acmecorp-a1b2c3"
  },
  "created_at": "2024-01-15T10:30:00Z",
  "last_login": "2024-01-20T14:25:00Z"
}
```

**Error Responses:**

```json
// 401 Unauthorized
{
  "detail": "Could not validate credentials"
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 6. Logout

Invalidate user's session.

**Endpoint:** `POST /auth/logout`

**Authentication:** Required

**Success Response:** `200 OK`

```json
{
  "message": "Logged out successfully"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/auth/logout" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## OAuth Endpoints

### 1. Google Login

Initiate Google OAuth login flow.

**Endpoint:** `GET /auth/google/login`

**Query Parameters:**

| Parameter    | Type   | Required | Description                         |
| ------------ | ------ | -------- | ----------------------------------- |
| invite_token | string | No       | Organization invite token           |

**Response:** `302 Redirect`

Redirects user to Google OAuth consent screen.

**Example Request:**

```bash
# Without invite token
curl -X GET "http://localhost:8000/api/v1/auth/google/login"

# With invite token
curl -X GET "http://localhost:8000/api/v1/auth/google/login?invite_token=acmecorp-a1b2c3"
```

---

### 2. Google Callback

Google OAuth callback handler.

**Endpoint:** `GET /auth/google/callback`

**Query Parameters:**

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| code      | string | Yes      | Authorization code from Google |
| state     | string | Yes      | CSRF protection state          |

**Response:** `302 Redirect`

Redirects to frontend with token in URL:
```
http://localhost:5173/oauth-callback?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Error Redirect:**
```
http://localhost:5173/oauth-callback?error=authentication_failed
```

---

### 3. GitHub Login

Initiate GitHub OAuth login flow.

**Endpoint:** `GET /auth/github/login`

**Query Parameters:**

| Parameter    | Type   | Required | Description               |
| ------------ | ------ | -------- | ------------------------- |
| invite_token | string | No       | Organization invite token |

**Response:** `302 Redirect`

Redirects user to GitHub OAuth consent screen.

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/auth/github/login"
```

---

### 4. GitHub Callback

GitHub OAuth callback handler.

**Endpoint:** `GET /auth/github/callback`

**Query Parameters:**

| Parameter | Type   | Required | Description                    |
| --------- | ------ | -------- | ------------------------------ |
| code      | string | Yes      | Authorization code from GitHub |
| state     | string | Yes      | CSRF protection state          |

**Response:** `302 Redirect`

Same as Google callback - redirects to frontend with token or error.

---

## Organization Endpoints

### 1. Create Organization

Create a new organization (tenant).

**Endpoint:** `POST /organizations/`

**Authentication:** Required

**Request Body:**

```json
{
  "name": "Acme Corporation"
}
```

**Success Response:** `201 Created`

```json
{
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "name": "Acme Corporation",
  "invite_token": "acmecorporation-x7y8z9",
  "owner_id": "550e8400-e29b-41d4-a716-446655440000",
  "created_at": "2024-01-15T10:30:00Z",
  "member_count": 1
}
```

**Error Responses:**

```json
// 409 Conflict - Organization already exists
{
  "detail": "Organization with this name already exists"
}

// 422 Validation Error
{
  "detail": [
    {
      "loc": ["body", "name"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/organizations/" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Acme Corporation"
  }'
```

---

### 2. List Organizations

Get all organizations (admin only) or user's organizations.

**Endpoint:** `GET /organizations/`

**Authentication:** Required

**Query Parameters:**

| Parameter | Type    | Default | Description                    |
| --------- | ------- | ------- | ------------------------------ |
| skip      | integer | 0       | Number of records to skip      |
| limit     | integer | 100     | Maximum records to return      |

**Success Response:** `200 OK`

```json
[
  {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "name": "Acme Corporation",
    "invite_token": "acmecorporation-x7y8z9",
    "created_at": "2024-01-15T10:30:00Z",
    "member_count": 5
  },
  {
    "id": "770e8400-e29b-41d4-a716-446655440002",
    "name": "Beta Inc",
    "invite_token": "betainc-p4q5r6",
    "created_at": "2024-01-18T14:20:00Z",
    "member_count": 3
  }
]
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/organizations/?skip=0&limit=10" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 3. Get Organization

Retrieve organization details by ID.

**Endpoint:** `GET /organizations/{organization_id}`

**Authentication:** Required

**Path Parameters:**

| Parameter       | Type | Description          |
| --------------- | ---- | -------------------- |
| organization_id | UUID | Organization ID      |

**Success Response:** `200 OK`

```json
{
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "name": "Acme Corporation",
  "invite_token": "acmecorporation-x7y8z9",
  "created_at": "2024-01-15T10:30:00Z",
  "owner": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "owner@example.com",
    "full_name": "John Doe"
  },
  "members": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "email": "owner@example.com",
      "full_name": "John Doe",
      "role": "owner"
    },
    {
      "id": "880e8400-e29b-41d4-a716-446655440003",
      "email": "member@example.com",
      "full_name": "Jane Smith",
      "role": "member"
    }
  ],
  "member_count": 2
}
```

**Error Responses:**

```json
// 404 Not Found
{
  "detail": "Organization not found"
}

// 403 Forbidden
{
  "detail": "You don't have access to this organization"
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/organizations/660e8400-e29b-41d4-a716-446655440001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 4. Update Organization

Update organization details.

**Endpoint:** `PUT /organizations/{organization_id}`

**Authentication:** Required (Owner only)

**Request Body:**

```json
{
  "name": "Acme Corp Updated"
}
```

**Success Response:** `200 OK`

```json
{
  "id": "660e8400-e29b-41d4-a716-446655440001",
  "name": "Acme Corp Updated",
  "invite_token": "acmecorpupdated-x7y8z9",
  "updated_at": "2024-01-20T16:45:00Z"
}
```

**Error Responses:**

```json
// 403 Forbidden - Not owner
{
  "detail": "Only organization owner can update organization details"
}

// 404 Not Found
{
  "detail": "Organization not found"
}
```

**Example Request:**

```bash
curl -X PUT "http://localhost:8000/api/v1/organizations/660e8400-e29b-41d4-a716-446655440001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Acme Corp Updated"
  }'
```

---

### 5. Delete Organization

Delete an organization (owner only).

**Endpoint:** `DELETE /organizations/{organization_id}`

**Authentication:** Required (Owner only)

**Success Response:** `200 OK`

```json
{
  "message": "Organization deleted successfully"
}
```

**Error Responses:**

```json
// 403 Forbidden
{
  "detail": "Only organization owner can delete organization"
}

// 400 Bad Request - Has members
{
  "detail": "Cannot delete organization with active members. Remove all members first."
}
```

**Example Request:**

```bash
curl -X DELETE "http://localhost:8000/api/v1/organizations/660e8400-e29b-41d4-a716-446655440001" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 6. Get My Organizations

Get all organizations the current user belongs to.

**Endpoint:** `GET /organizations/my-organizations`

**Authentication:** Required

**Success Response:** `200 OK`

```json
[
  {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "name": "Acme Corporation",
    "role": "owner",
    "joined_at": "2024-01-15T10:30:00Z"
  },
  {
    "id": "770e8400-e29b-41d4-a716-446655440002",
    "name": "Beta Inc",
    "role": "member",
    "joined_at": "2024-01-18T14:20:00Z"
  }
]
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/organizations/my-organizations" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 7. Generate Invite Token

Generate or regenerate organization invite token.

**Endpoint:** `POST /organizations/{organization_id}/invite`

**Authentication:** Required (Owner only)

**Success Response:** `200 OK`

```json
{
  "invite_token": "acmecorp-new123",
  "invite_url": "http://localhost:5173/register?invite=acmecorp-new123",
  "message": "Invite token generated successfully"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/organizations/660e8400-e29b-41d4-a716-446655440001/invite" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## Error Handling

### Standard Error Response Format

All errors follow this format:

```json
{
  "detail": "Error message description"
}
```

### Validation Error Format

```json
{
  "detail": [
    {
      "loc": ["body", "field_name"],
      "msg": "Validation error message",
      "type": "error_type"
    }
  ]
}
```

### Rate Limit Error

```json
{
  "detail": "Rate limit exceeded. Please try again in 60 seconds."
}
```

### Authentication Error

```json
{
  "detail": "Could not validate credentials",
  "headers": {
    "WWW-Authenticate": "Bearer"
  }
}
```

---

## Best Practices

### 1. Token Storage

```javascript
// Store token in localStorage or secure cookie
localStorage.setItem('access_token', response.access_token);

// Include in subsequent requests
fetch('/api/v1/auth/me', {
  headers: {
    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
  }
});
```

### 2. Error Handling

```javascript
try {
  const response = await fetch('/api/v1/auth/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });
  
  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail);
  }
  
  const data = await response.json();
  // Handle success
} catch (error) {
  // Handle error
  console.error(error.message);
}
```

### 3. Multi-Organization Handling

```javascript
// Check if user belongs to multiple orgs
if (error.organizations) {
  // Show organization selector
  const selectedOrg = await showOrgSelector(error.organizations);
  
  // Login with specific org
  await login(email, password, selectedOrg.id);
}
```

---

## Postman Collection

Import this collection to test all endpoints:

```json
{
  "info": {
    "name": "FastAPI SaaS - Auth & Organizations",
    "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
  },
  "variable": [
    {
      "key": "base_url",
      "value": "http://localhost:8000/api/v1"
    },
    {
      "key": "access_token",
      "value": ""
    }
  ]
}
```

---

**Last Updated:** 2024  
**API Version:** v1  
**Base URL:** `/api/v1`
