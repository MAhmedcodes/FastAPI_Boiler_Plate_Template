# API Documentation - Users, Jobs & Health

## Table of Contents

- [Overview](#overview)
- [Base URL](#base-url)
- [User Endpoints](#user-endpoints)
- [Background Jobs Endpoints](#background-jobs-endpoints)
- [Health & Monitoring Endpoints](#health--monitoring-endpoints)
- [WebSocket Endpoints](#websocket-endpoints)
- [Rate Limiting](#rate-limiting)
- [Examples & Use Cases](#examples--use-cases)

---

## Overview

This document covers user management, background job control, health monitoring, and system endpoints for the FastAPI SaaS Boilerplate.

---

## Base URL

```
Development: http://localhost:8000/api/v1
Production: https://api.yourdomain.com/api/v1
```

---

## User Endpoints

### 1. List Users

Get all users in the current organization.

**Endpoint:** `GET /users/`

**Authentication:** Required

**Query Parameters:**

| Parameter | Type    | Default | Description                    |
| --------- | ------- | ------- | ------------------------------ |
| skip      | integer | 0       | Number of records to skip      |
| limit     | integer | 100     | Maximum records to return      |
| search    | string  | null    | Search by name or email        |
| is_verified | boolean | null  | Filter by verification status  |

**Success Response:** `200 OK`

```json
{
  "total": 25,
  "users": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "email": "user1@example.com",
      "full_name": "John Doe",
      "is_verified": true,
      "provider": "email",
      "created_at": "2024-01-15T10:30:00Z",
      "last_login": "2024-01-20T14:25:00Z"
    },
    {
      "id": "880e8400-e29b-41d4-a716-446655440003",
      "email": "user2@example.com",
      "full_name": "Jane Smith",
      "is_verified": true,
      "provider": "google",
      "created_at": "2024-01-16T11:45:00Z",
      "last_login": "2024-01-20T15:10:00Z"
    }
  ]
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/users/?skip=0&limit=10&search=john" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Example with Filters:**

```bash
# Get only verified users
curl -X GET "http://localhost:8000/api/v1/users/?is_verified=true" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."

# Search users
curl -X GET "http://localhost:8000/api/v1/users/?search=example.com" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 2. Get User by ID

Retrieve detailed information about a specific user.

**Endpoint:** `GET /users/{user_id}`

**Authentication:** Required

**Path Parameters:**

| Parameter | Type | Description      |
| --------- | ---- | ---------------- |
| user_id   | UUID | User identifier  |

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
    "name": "Acme Corporation",
    "role": "member"
  },
  "created_at": "2024-01-15T10:30:00Z",
  "last_login": "2024-01-20T14:25:00Z",
  "email_verified_at": "2024-01-15T10:35:00Z",
  "profile": {
    "avatar_url": null,
    "timezone": "UTC",
    "language": "en"
  }
}
```

**Error Responses:**

```json
// 404 Not Found
{
  "detail": "User not found"
}

// 403 Forbidden - Different organization
{
  "detail": "You don't have permission to view this user"
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/users/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 3. Update User

Update user information.

**Endpoint:** `PUT /users/{user_id}`

**Authentication:** Required (Self or Admin)

**Request Body:**

```json
{
  "full_name": "John Updated Doe",
  "email": "newemail@example.com",
  "profile": {
    "timezone": "America/New_York",
    "language": "en"
  }
}
```

**Request Fields:**

| Field      | Type   | Required | Description                      |
| ---------- | ------ | -------- | -------------------------------- |
| full_name  | string | No       | User's full name                 |
| email      | string | No       | New email (requires reverification) |
| profile    | object | No       | User profile settings            |

**Success Response:** `200 OK`

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "email": "newemail@example.com",
  "full_name": "John Updated Doe",
  "is_verified": false,
  "updated_at": "2024-01-20T16:45:00Z",
  "message": "Email changed. Please verify your new email address."
}
```

**Error Responses:**

```json
// 403 Forbidden
{
  "detail": "You can only update your own profile"
}

// 409 Conflict - Email exists
{
  "detail": "Email already in use"
}
```

**Example Request:**

```bash
curl -X PUT "http://localhost:8000/api/v1/users/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "full_name": "John Updated Doe"
  }'
```

---

### 4. Delete User

Delete a user account.

**Endpoint:** `DELETE /users/{user_id}`

**Authentication:** Required (Self or Admin)

**Success Response:** `200 OK`

```json
{
  "message": "User account deleted successfully",
  "deleted_user_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Error Responses:**

```json
// 403 Forbidden
{
  "detail": "You can only delete your own account"
}

// 400 Bad Request - Organization owner
{
  "detail": "Organization owners must transfer ownership before deleting account"
}
```

**Example Request:**

```bash
curl -X DELETE "http://localhost:8000/api/v1/users/550e8400-e29b-41d4-a716-446655440000" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 5. Change Password

Change user password.

**Endpoint:** `POST /users/{user_id}/change-password`

**Authentication:** Required (Self only)

**Request Body:**

```json
{
  "current_password": "OldPass123!",
  "new_password": "NewSecurePass456!",
  "confirm_password": "NewSecurePass456!"
}
```

**Request Fields:**

| Field            | Type   | Required | Description                 |
| ---------------- | ------ | -------- | --------------------------- |
| current_password | string | Yes      | Current password            |
| new_password     | string | Yes      | New password (min 8 chars)  |
| confirm_password | string | Yes      | Must match new_password     |

**Success Response:** `200 OK`

```json
{
  "message": "Password changed successfully"
}
```

**Error Responses:**

```json
// 400 Bad Request - Wrong current password
{
  "detail": "Current password is incorrect"
}

// 422 Validation Error - Passwords don't match
{
  "detail": "New password and confirm password do not match"
}

// 400 Bad Request - OAuth user
{
  "detail": "Cannot change password for OAuth users"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/users/550e8400-e29b-41d4-a716-446655440000/change-password" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "current_password": "OldPass123!",
    "new_password": "NewSecurePass456!",
    "confirm_password": "NewSecurePass456!"
  }'
```

---

### 6. Get User Statistics

Get statistics about a user's activity.

**Endpoint:** `GET /users/{user_id}/stats`

**Authentication:** Required

**Success Response:** `200 OK`

```json
{
  "user_id": "550e8400-e29b-41d4-a716-446655440000",
  "stats": {
    "total_logins": 45,
    "organizations_count": 2,
    "account_age_days": 30,
    "last_activity": "2024-01-20T14:25:00Z",
    "verification_status": "verified",
    "provider": "email"
  }
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/users/550e8400-e29b-41d4-a716-446655440000/stats" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## Background Jobs Endpoints

### 1. Get Job Status

Get current status of background job processing.

**Endpoint:** `GET /jobs/status`

**Authentication:** Required

**Success Response:** `200 OK`

```json
{
  "email_tasks": {
    "status": "active",
    "paused": false,
    "queue_length": 5,
    "processed_today": 127,
    "failed_today": 2
  },
  "maintenance_tasks": {
    "status": "active",
    "paused": false,
    "queue_length": 0,
    "processed_today": 3,
    "failed_today": 0
  },
  "celery_workers": {
    "total": 2,
    "active": 2,
    "offline": 0
  },
  "scheduler": {
    "status": "running",
    "next_cleanup": "2024-01-21T02:00:00Z",
    "next_reminder": "2024-01-21T10:00:00Z"
  }
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/jobs/status" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 2. Pause Tasks

Pause background task processing.

**Endpoint:** `POST /jobs/pause`

**Authentication:** Required (Admin only)

**Request Body:**

```json
{
  "task_type": "email"
}
```

**Request Fields:**

| Field     | Type   | Required | Description                               |
| --------- | ------ | -------- | ----------------------------------------- |
| task_type | string | Yes      | Type of tasks to pause: "email", "maintenance", "all" |

**Success Response:** `200 OK`

```json
{
  "message": "Email tasks paused successfully",
  "paused_at": "2024-01-20T16:45:00Z",
  "task_type": "email"
}
```

**Error Responses:**

```json
// 400 Bad Request - Already paused
{
  "detail": "Email tasks are already paused"
}

// 403 Forbidden
{
  "detail": "Only administrators can pause tasks"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/jobs/pause" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "email"
  }'
```

---

### 3. Resume Tasks

Resume paused background tasks.

**Endpoint:** `POST /jobs/resume`

**Authentication:** Required (Admin only)

**Request Body:**

```json
{
  "task_type": "email"
}
```

**Success Response:** `200 OK`

```json
{
  "message": "Email tasks resumed successfully",
  "resumed_at": "2024-01-20T16:50:00Z",
  "task_type": "email",
  "pending_tasks": 12
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/jobs/resume" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." \
  -H "Content-Type: application/json" \
  -d '{
    "task_type": "email"
  }'
```

---

### 4. Trigger Cleanup

Manually trigger database cleanup job.

**Endpoint:** `POST /jobs/cleanup`

**Authentication:** Required (Admin only)

**Success Response:** `200 OK`

```json
{
  "message": "Cleanup job queued successfully",
  "task_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "estimated_completion": "2024-01-20T17:00:00Z"
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/jobs/cleanup" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 5. Get Task History

Get history of background tasks.

**Endpoint:** `GET /jobs/history`

**Authentication:** Required (Admin only)

**Query Parameters:**

| Parameter | Type    | Default | Description                      |
| --------- | ------- | ------- | -------------------------------- |
| task_type | string  | null    | Filter by task type              |
| status    | string  | null    | Filter by status: "success", "failed", "pending" |
| limit     | integer | 100     | Maximum records to return        |

**Success Response:** `200 OK`

```json
{
  "total": 245,
  "tasks": [
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "task_type": "email",
      "task_name": "send_otp_email",
      "status": "success",
      "created_at": "2024-01-20T16:30:00Z",
      "completed_at": "2024-01-20T16:30:05Z",
      "duration_seconds": 5,
      "retry_count": 0
    },
    {
      "id": "7ba85f64-5717-4562-b3fc-2c963f66afa7",
      "task_type": "maintenance",
      "task_name": "cleanup_old_tasks",
      "status": "success",
      "created_at": "2024-01-20T02:00:00Z",
      "completed_at": "2024-01-20T02:00:15Z",
      "duration_seconds": 15,
      "deleted_records": 150
    }
  ]
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/api/v1/jobs/history?task_type=email&limit=50" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 6. Retry Failed Task

Retry a failed background task.

**Endpoint:** `POST /jobs/{task_id}/retry`

**Authentication:** Required (Admin only)

**Path Parameters:**

| Parameter | Type | Description    |
| --------- | ---- | -------------- |
| task_id   | UUID | Task identifier |

**Success Response:** `200 OK`

```json
{
  "message": "Task queued for retry",
  "task_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "retry_attempt": 2
}
```

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/jobs/3fa85f64-5717-4562-b3fc-2c963f66afa6/retry" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## Health & Monitoring Endpoints

### 1. Health Check

Basic health check endpoint.

**Endpoint:** `GET /health`

**Authentication:** Not required

**Success Response:** `200 OK`

```json
{
  "status": "healthy",
  "timestamp": "2024-01-20T16:45:00Z",
  "version": "1.0.0",
  "uptime_seconds": 345678
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/health"
```

---

### 2. Detailed Health Check

Comprehensive system health check.

**Endpoint:** `GET /health/detailed`

**Authentication:** Required (Admin only)

**Success Response:** `200 OK`

```json
{
  "status": "healthy",
  "timestamp": "2024-01-20T16:45:00Z",
  "components": {
    "database": {
      "status": "healthy",
      "response_time_ms": 15,
      "pool_size": 10,
      "active_connections": 3
    },
    "redis": {
      "status": "healthy",
      "response_time_ms": 2,
      "memory_usage_mb": 45,
      "connected_clients": 5
    },
    "celery": {
      "status": "healthy",
      "active_workers": 2,
      "queued_tasks": 7,
      "failed_tasks_24h": 3
    },
    "email": {
      "status": "healthy",
      "smtp_connection": "connected",
      "sent_today": 127,
      "failed_today": 2
    }
  },
  "performance": {
    "avg_response_time_ms": 45,
    "requests_per_minute": 120,
    "error_rate_percent": 0.5
  }
}
```

**Unhealthy Response:** `503 Service Unavailable`

```json
{
  "status": "unhealthy",
  "timestamp": "2024-01-20T16:45:00Z",
  "components": {
    "database": {
      "status": "unhealthy",
      "error": "Connection timeout"
    },
    "redis": {
      "status": "healthy"
    },
    "celery": {
      "status": "degraded",
      "active_workers": 1,
      "expected_workers": 2
    }
  }
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/health/detailed" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

### 3. Metrics

Get system metrics.

**Endpoint:** `GET /metrics`

**Authentication:** Required (Admin only)

**Success Response:** `200 OK`

```json
{
  "timestamp": "2024-01-20T16:45:00Z",
  "metrics": {
    "users": {
      "total": 1250,
      "verified": 1100,
      "active_last_7_days": 850,
      "new_today": 15
    },
    "organizations": {
      "total": 320,
      "active": 290,
      "new_today": 3
    },
    "api": {
      "requests_today": 45000,
      "avg_response_time_ms": 45,
      "error_rate_percent": 0.5,
      "rate_limit_hits": 23
    },
    "background_jobs": {
      "processed_today": 450,
      "failed_today": 5,
      "queued": 12,
      "avg_processing_time_ms": 1500
    },
    "database": {
      "size_mb": 2048,
      "table_count": 15,
      "total_records": 150000
    }
  }
}
```

**Example Request:**

```bash
curl -X GET "http://localhost:8000/metrics" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## WebSocket Endpoints

### 1. Real-time Notifications

WebSocket endpoint for real-time notifications.

**Endpoint:** `WS /ws/notifications`

**Authentication:** Required (via query param)

**Connection:**

```javascript
const token = 'your_jwt_token';
const ws = new WebSocket(`ws://localhost:8000/ws/notifications?token=${token}`);

ws.onopen = () => {
  console.log('Connected to notifications');
};

ws.onmessage = (event) => {
  const notification = JSON.parse(event.data);
  console.log('Received:', notification);
};
```

**Message Format:**

```json
{
  "type": "email_verified",
  "timestamp": "2024-01-20T16:45:00Z",
  "data": {
    "user_id": "550e8400-e29b-41d4-a716-446655440000",
    "message": "Email verified successfully"
  }
}
```

**Notification Types:**

- `email_verified` - Email verification completed
- `organization_invite` - Invited to organization
- `task_completed` - Background task completed
- `task_failed` - Background task failed
- `system_alert` - System notification

---

### 2. Task Progress

WebSocket endpoint for monitoring task progress.

**Endpoint:** `WS /ws/tasks/{task_id}`

**Connection:**

```javascript
const taskId = '3fa85f64-5717-4562-b3fc-2c963f66afa6';
const token = 'your_jwt_token';
const ws = new WebSocket(`ws://localhost:8000/ws/tasks/${taskId}?token=${token}`);

ws.onmessage = (event) => {
  const progress = JSON.parse(event.data);
  console.log(`Progress: ${progress.percent}%`);
};
```

**Progress Message:**

```json
{
  "task_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
  "status": "processing",
  "percent": 45,
  "message": "Processing batch 45/100",
  "timestamp": "2024-01-20T16:45:30Z"
}
```

---

## Rate Limiting

### Default Rate Limits

| Endpoint Category   | Limit                 | Window   |
| ------------------- | --------------------- | -------- |
| Authentication      | 5 requests            | 1 minute |
| Registration        | 3 requests            | 5 minutes|
| Email Operations    | 10 requests           | 1 minute |
| General API         | 100 requests          | 1 minute |
| Admin Operations    | 50 requests           | 1 minute |

### Rate Limit Headers

Every response includes rate limit information:

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 95
X-RateLimit-Reset: 1642694400
```

### Rate Limit Exceeded Response

```json
{
  "detail": "Rate limit exceeded. Try again in 45 seconds.",
  "retry_after": 45
}
```

---

## Examples & Use Cases

### Use Case 1: User Registration Flow

Complete user registration with email verification:

```javascript
// 1. Register user
const registerResponse = await fetch('/api/v1/auth/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'SecurePass123!',
    full_name: 'John Doe'
  })
});

const userData = await registerResponse.json();
console.log('User registered:', userData);

// 2. User receives OTP via email (handled by backend)

// 3. Verify email with OTP
const verifyResponse = await fetch('/api/v1/auth/verify-email', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    otp_code: '123456'
  })
});

// 4. Login after verification
const loginResponse = await fetch('/api/v1/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'SecurePass123!'
  })
});

const { access_token } = await loginResponse.json();
localStorage.setItem('token', access_token);
```

---

### Use Case 2: Organization Invitation Flow

Complete flow for inviting users to organization:

```javascript
// 1. Owner creates organization
const createOrgResponse = await fetch('/api/v1/organizations/', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${ownerToken}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    name: 'Acme Corporation'
  })
});

const org = await createOrgResponse.json();
const inviteToken = org.invite_token;

// 2. Share invite link
const inviteLink = `https://app.example.com/register?invite=${inviteToken}`;
console.log('Share this link:', inviteLink);

// 3. New user registers with invite token
const newUserResponse = await fetch('/api/v1/auth/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'newuser@example.com',
    password: 'SecurePass123!',
    full_name: 'Jane Smith',
    invite_token: inviteToken
  })
});

// User is now part of the organization
```

---

### Use Case 3: Background Job Monitoring

Monitor background jobs with real-time updates:

```javascript
// 1. Check overall job status
const statusResponse = await fetch('/api/v1/jobs/status', {
  headers: { 'Authorization': `Bearer ${token}` }
});

const status = await statusResponse.json();
console.log('Queue length:', status.email_tasks.queue_length);

// 2. Pause email tasks during maintenance
await fetch('/api/v1/jobs/pause', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ task_type: 'email' })
});

// 3. Perform maintenance

// 4. Resume email tasks
await fetch('/api/v1/jobs/resume', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ task_type: 'email' })
});

// 5. Monitor task history
const historyResponse = await fetch('/api/v1/jobs/history?limit=10', {
  headers: { 'Authorization': `Bearer ${token}` }
});

const history = await historyResponse.json();
console.log('Recent tasks:', history.tasks);
```

---

### Use Case 4: Health Monitoring Dashboard

Create a health monitoring dashboard:

```javascript
// Fetch detailed health status
async function getSystemHealth() {
  const response = await fetch('/api/v1/health/detailed', {
    headers: { 'Authorization': `Bearer ${adminToken}` }
  });
  
  const health = await response.json();
  
  // Check each component
  if (health.components.database.status !== 'healthy') {
    alert('Database issue detected!');
  }
  
  if (health.components.celery.active_workers < 2) {
    console.warn('Celery workers below expected count');
  }
  
  // Display metrics
  console.log('System Health:', {
    status: health.status,
    database: health.components.database.response_time_ms + 'ms',
    redis: health.components.redis.response_time_ms + 'ms',
    avgResponse: health.performance.avg_response_time_ms + 'ms'
  });
  
  return health;
}

// Poll health every 30 seconds
setInterval(getSystemHealth, 30000);
```

---

### Use Case 5: User Profile Management

Complete user profile update flow:

```javascript
// 1. Get current user info
const meResponse = await fetch('/api/v1/auth/me', {
  headers: { 'Authorization': `Bearer ${token}` }
});

const currentUser = await meResponse.json();

// 2. Update profile
const updateResponse = await fetch(`/api/v1/users/${currentUser.id}`, {
  method: 'PUT',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    full_name: 'John Updated Doe',
    profile: {
      timezone: 'America/New_York',
      language: 'en'
    }
  })
});

// 3. Change password
const passwordResponse = await fetch(`/api/v1/users/${currentUser.id}/change-password`, {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${token}`,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    current_password: 'OldPass123!',
    new_password: 'NewSecurePass456!',
    confirm_password: 'NewSecurePass456!'
  })
});

// 4. Get updated stats
const statsResponse = await fetch(`/api/v1/users/${currentUser.id}/stats`, {
  headers: { 'Authorization': `Bearer ${token}` }
});

const stats = await statsResponse.json();
console.log('Account age:', stats.stats.account_age_days, 'days');
```

---

## SDK Examples

### Python SDK

```python
import requests

class FastAPISaaSClient:
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.token = token
        
    def login(self, email, password):
        response = requests.post(
            f"{self.base_url}/auth/login",
            json={"email": email, "password": password}
        )
        data = response.json()
        self.token = data['access_token']
        return data
    
    def get_users(self, skip=0, limit=100):
        response = requests.get(
            f"{self.base_url}/users/",
            headers={"Authorization": f"Bearer {self.token}"},
            params={"skip": skip, "limit": limit}
        )
        return response.json()
    
    def create_organization(self, name):
        response = requests.post(
            f"{self.base_url}/organizations/",
            headers={"Authorization": f"Bearer {self.token}"},
            json={"name": name}
        )
        return response.json()

# Usage
client = FastAPISaaSClient("http://localhost:8000/api/v1")
client.login("admin@example.com", "SecurePass123!")
users = client.get_users()
```

---

### JavaScript/TypeScript SDK

```typescript
class FastAPISaaSClient {
  private baseUrl: string;
  private token: string | null = null;

  constructor(baseUrl: string) {
    this.baseUrl = baseUrl;
  }

  async login(email: string, password: string) {
    const response = await fetch(`${this.baseUrl}/auth/login`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });
    const data = await response.json();
    this.token = data.access_token;
    return data;
  }

  async getUsers(skip = 0, limit = 100) {
    const response = await fetch(
      `${this.baseUrl}/users/?skip=${skip}&limit=${limit}`,
      {
        headers: { 'Authorization': `Bearer ${this.token}` }
      }
    );
    return await response.json();
  }

  async pauseJobs(taskType: string) {
    const response = await fetch(`${this.baseUrl}/jobs/pause`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${this.token}`,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ task_type: taskType })
    });
    return await response.json();
  }
}

// Usage
const client = new FastAPISaaSClient('http://localhost:8000/api/v1');
await client.login('admin@example.com', 'SecurePass123!');
const users = await client.getUsers();
```

---

## Testing with cURL

### Complete Test Suite

```bash
#!/bin/bash

BASE_URL="http://localhost:8000/api/v1"

# 1. Health Check
echo "=== Health Check ==="
curl -X GET "$BASE_URL/../health"

# 2. Register User
echo "\n=== Register User ==="
REGISTER_RESPONSE=$(curl -X POST "$BASE_URL/auth/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "TestPass123!",
    "full_name": "Test User"
  }')
echo $REGISTER_RESPONSE

# 3. Verify Email (use OTP from email)
echo "\n=== Verify Email ==="
curl -X POST "$BASE_URL/auth/verify-email" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "otp_code": "123456"
  }'

# 4. Login
echo "\n=== Login ==="
LOGIN_RESPONSE=$(curl -X POST "$BASE_URL/auth/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "TestPass123!"
  }')

TOKEN=$(echo $LOGIN_RESPONSE | jq -r '.access_token')

# 5. Get Current User
echo "\n=== Get Current User ==="
curl -X GET "$BASE_URL/auth/me" \
  -H "Authorization: Bearer $TOKEN"

# 6. Get Job Status
echo "\n=== Job Status ==="
curl -X GET "$BASE_URL/jobs/status" \
  -H "Authorization: Bearer $TOKEN"

# 7. List Users
echo "\n=== List Users ==="
curl -X GET "$BASE_URL/users/?limit=10" \
  -H "Authorization: Bearer $TOKEN"
```

---

**Last Updated:** 2024  
**API Version:** v1  
**Base URL:** `/api/v1`
