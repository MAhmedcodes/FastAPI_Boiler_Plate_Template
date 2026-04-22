<div align="center">

# 🚀 FastAPI SaaS Authentication Boilerplate

### Production-Ready Multi-Tenant FastAPI Template with Complete Authentication, Email Verification & Background Jobs

[![FastAPI](https://img.shields.io/badge/FastAPI-0.135+-00a393?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![Redis](https://img.shields.io/badge/Redis-7+-DC382D?style=for-the-badge&logo=redis&logoColor=white)](https://redis.io)
[![Celery](https://img.shields.io/badge/Celery-5.6+-37814A?style=for-the-badge&logo=celery&logoColor=white)](https://docs.celeryq.dev)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [API Docs](#-api-endpoints) • [Architecture](#-architecture) • [Multi-Tenancy](#-multi-tenancy--saas) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

A **complete, production-ready FastAPI boilerplate** featuring:

- 🏢 **Multi-tenant SaaS architecture** with organization management
- 🔐 **Comprehensive authentication** - JWT, OAuth2 (Google & GitHub), Email verification with OTP
- 📧 **Email system** - SMTP delivery, OTP codes, organization-aware templates
- ⚙️ **Background jobs** - Celery with pause/resume control, scheduled tasks
- 🛡️ **Enterprise security** - Rate limiting, SQL injection protection, CORS, password hashing
- 🏗️ **Modular architecture** - Repository pattern, service layer, dependency injection
- 🧪 **Complete testing** - Unit & E2E test suite with mocked services
- 🐳 **Docker ready** - Multi-service containerization with 8 services

**Perfect for:** SaaS applications, multi-tenant platforms, scalable APIs, production deployments

---

## ✨ Features

### 🔐 Authentication & Authorization

- ✅ JWT token-based authentication with configurable expiration
- ✅ User registration with email validation
- ✅ Secure password storage (Argon2 & bcrypt)
- ✅ OAuth2 password flow compliance
- ✅ Email verification with 6-digit OTP (24-hour expiry)
- ✅ Provider locking (email/password, Google, GitHub)
- ✅ Multi-organization support with invite tokens

### 🏢 Multi-Tenancy & SaaS

- ✅ Organization-based tenant isolation
- ✅ Invite token system for joining organizations
- ✅ Same email across multiple organizations
- ✅ Cross-organization user management
- ✅ OAuth support for multi-org scenarios
- ✅ Organization context in all operations

### 🌐 OAuth Integration

- ✅ Google OAuth2 login with auto-profile extraction
- ✅ GitHub OAuth2 login with auto-profile extraction
- ✅ OAuth state management & CSRF protection
- ✅ Multi-org OAuth support
- ✅ Auto-verification for OAuth users
- ✅ Invite token OAuth flow

### 📧 Email System

- ✅ SMTP email delivery (Gmail supported)
- ✅ Async task processing with Celery
- ✅ OTP verification emails
- ✅ Welcome emails with organization context
- ✅ Daily reminder emails for inactive users
- ✅ Customizable email templates
- ✅ Retry mechanism (3 attempts)
- ✅ Email queue with gevent pool (50 concurrent)

### 🔄 Background Jobs

- ✅ Celery worker queues (email, maintenance)
- ✅ Scheduled tasks with Celery Beat
- ✅ Pause/Resume control per task type
- ✅ Flower monitoring dashboard
- ✅ Redis message broker
- ✅ Automatic cleanup (15+ day old tasks)
- ✅ Daily reminder scheduling

### 🛡️ Security Features

- ✅ Rate limiting (5-10 req/min, configurable)
- ✅ SQL injection protection middleware
- ✅ CORS configuration with origin validation
- ✅ Password strength validation
- ✅ Secure session management
- ✅ XSS prevention
- ✅ OTP expiration & single-use validation
- ✅ Multi-tenant data isolation

### 🏗️ Architecture & Code Quality

- ✅ Modular structure with clean separation
- ✅ Repository pattern for data access
- ✅ Service layer for business logic
- ✅ Dependency injection setup
- ✅ Environment-based configuration
- ✅ Database migrations (Alembic)
- ✅ Type hints throughout (Pydantic)
- ✅ Custom error handlers

### 🧪 Testing Infrastructure

- ✅ Complete test suite (Unit + E2E)
- ✅ Pytest with fixtures
- ✅ Test database isolation (automatically deleted after tests)
- ✅ Mocked external services
- ✅ Coverage reporting
- ✅ Shared conftest configuration

---

## 🛠️ Tech Stack

| Category        | Technology              | Purpose                     |
| --------------- | ----------------------- | --------------------------- |
| **Framework**   | FastAPI 0.135+          | High-performance async API  |
| **ORM**         | SQLAlchemy 2.0          | Database abstraction layer  |
| **Database**    | PostgreSQL 13+          | Relational data storage     |
| **Cache/Queue** | Redis 7+                | Celery message broker       |
| **Tasks**       | Celery 5.6+             | Async background jobs       |
| **Auth**        | Python-JOSE, Authlib    | JWT & OAuth2 handling       |
| **Hashing**     | Argon2, Bcrypt, Passlib | Secure password storage     |
| **Email**       | smtplib, SMTP           | Email delivery              |
| **Rate Limit**  | SlowAPI, Limits         | Request throttling          |
| **Validation**  | Pydantic 2.12+          | Request/response validation |
| **Server**      | Uvicorn                 | ASGI server                 |
| **Migrations**  | Alembic                 | Database versioning         |
| **Monitoring**  | Flower                  | Celery task monitoring      |
| **Testing**     | Pytest, Pytest-Cov      | Unit & E2E testing          |
| **Container**   | Docker, Docker Compose  | Multi-service deployment    |

---

## 📁 Project Structure

```
fastapi-saas-boilerplate/
│
├── 📂 app/                          # Backend - FastAPI application
│   ├── 📂 core/                     # Core functionality
│   │   ├── 📂 celery/               # Celery configuration & tasks
│   │   ├── 📂 config/               # Settings & configuration
│   │   ├── 📂 database/             # Database connection & session
│   │   ├── 📂 dependencies/         # Dependency injection
│   │   ├── 📂 errors/               # Custom error handlers
│   │   ├── 📂 middleware/           # Custom middleware (CORS, rate limit, etc.)
│   │   └── 📂 security/             # Auth handlers (OAuth, JWT)
│   │
│   ├── 📂 modules/                  # Feature modules
│   │   ├── 📂 auth/                 # Authentication module
│   │   │   ├── models/              # OTP model
│   │   │   ├── repository/          # Data access
│   │   │   ├── router/              # API endpoints
│   │   │   ├── schema/              # Pydantic models
│   │   │   └── services/            # Business logic
│   │   │
│   │   ├── 📂 jobs/                 # Background jobs module
│   │   │   ├── models/              # Task control model
│   │   │   ├── repository/          # Job data access
│   │   │   ├── router/              # Job management routes
│   │   │   ├── schema/              # Job schemas
│   │   │   └── services/            # Job control services
│   │   │
│   │   ├── 📂 organizations/        # Multi-tenant organization
│   │   │   ├── models/              # Organization models
│   │   │   ├── repository/          # Organization data access
│   │   │   ├── router/              # Organization routes
│   │   │   ├── schema/              # Organization schemas
│   │   │   └── services/            # Organization logic
│   │   │
│   │   └── 📂 users/                # Users module
│   │       ├── models/              # User database model
│   │       ├── repository/          # User data access
│   │       ├── router/              # User API endpoints
│   │       ├── schema/              # User schemas
│   │       └── services/            # User business logic
│   │
│   ├── 📂 shared/                   # Shared utilities
│   │   ├── 📂 constants/            # Application constants
│   │   ├── 📂 utils/                # Utility functions
│   │   └── 📂 validator/            # Custom validators
│   │
│   ├── 📂 templates/                # Email templates
│   │   └── 📂 emails/               # Email templates
│   │
│   └── main.py                      # Application entry point
│
├── 📂 frontend/                     # Frontend - React application
│   ├── 📂 public/                   # Static assets
│   ├── 📂 src/
│   │   ├── 📂 api/                  # API integration layer
│   │   ├── 📂 components/           # Reusable components
│   │   ├── 📂 pages/                # Page components
│   │   ├── 📂 context/              # React Context (auth, org)
│   │   ├── 📂 utils/                # Utility functions
│   │   ├── App.jsx                  # Root component
│   │   └── index.js                 # Entry point
│   │
│   ├── package.json                 # Frontend dependencies
│   └── vite.config.js               # Vite configuration
│
├── 📂 tests/                        # Test suite
│   ├── conftest.py                  # Shared test fixtures
│   ├── test_auth.py                 # Authentication tests
│   ├── test_organizations.py        # Organization tests
│   ├── test_jobs.py                 # Job control tests
│   └── test_users.py                # User tests
│
├── 📂 migrations/                   # Alembic migrations
│   └── versions/                    # Migration versions
│
├── .env.example                     # Environment template
├── docker-compose.yml               # Docker orchestration
├── Dockerfile                       # Backend container
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

---

## 🏗️ Architecture

### System Architecture Diagram

```mermaid
graph TB
    subgraph "Client Layer"
        A[React Frontend]
    end

    subgraph "API Layer"
        B[FastAPI Application]
        C[Uvicorn Server]
    end

    subgraph "Authentication"
        D[JWT Handler]
        E[OAuth2 Provider]
        F[OTP Service]
    end

    subgraph "Data Layer"
        G[PostgreSQL]
        H[Redis Cache]
    end

    subgraph "Background Processing"
        I[Celery Workers]
        J[Celery Beat Scheduler]
        K[Flower Monitor]
    end

    subgraph "External Services"
        L[SMTP Server]
        M[Google OAuth]
        N[GitHub OAuth]
    end

    A -->|HTTP/REST| B
    B --> C
    B --> D
    B --> E
    B --> F
    B --> G
    B --> H
    B --> I
    I --> H
    J --> I
    I --> L
    E --> M
    E --> N
    K -.->|Monitor| I

    style A fill:#61dafb
    style B fill:#009688
    style G fill:#336791
    style H fill:#dc382d
    style I fill:#37814a
```

### Multi-Tenant Data Flow

```mermaid
sequenceDiagram
    participant U as User
    participant F as Frontend
    participant A as API
    participant DB as Database
    participant R as Redis
    participant C as Celery

    U->>F: Register/Login
    F->>A: POST /auth/register
    A->>DB: Create User + Organization
    A->>C: Queue OTP Email
    C->>U: Send Email
    A-->>F: Return Tokens

    U->>F: Verify Email
    F->>A: POST /auth/verify-email
    A->>DB: Mark Email Verified
    A->>R: Cache User Session
    A-->>F: Success

    U->>F: Create Organization
    F->>A: POST /organizations/
    A->>DB: Create Organization
    A->>DB: Link User to Org
    A-->>F: Organization Data

    U->>F: Invite User to Org
    F->>A: POST /organizations/{id}/invite
    A->>DB: Create Invite Token
    A->>C: Queue Invite Email
    C->>U: Send Invite
    A-->>F: Invite Token
```

### Request Lifecycle

```mermaid
graph LR
    A[HTTP Request] --> B[CORS Middleware]
    B --> C[Rate Limiter]
    C --> D[SQL Injection Check]
    D --> E[Route Handler]
    E --> F{Auth Required?}
    F -->|Yes| G[JWT Validation]
    F -->|No| H[Process Request]
    G --> H
    H --> I[Service Layer]
    I --> J[Repository Layer]
    J --> K[Database]
    K --> J
    J --> I
    I --> L[Response]
    L --> M[JSON Serialization]
    M --> N[HTTP Response]
```

---

## 🚀 Installation

### Prerequisites

- Python 3.8+
- PostgreSQL 13+
- Redis 7+
- Node.js 16+ (for frontend)
- Docker & Docker Compose (optional)

### Option 1: Local Development Setup

#### 1. Clone Repository

```bash
git clone https://github.com/yourusername/fastapi-saas-boilerplate.git
cd fastapi-saas-boilerplate
```

#### 2. Backend Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your configuration
nano .env
```

#### 3. Environment Configuration

Update `.env` file with your settings:

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/saas_db

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# OAuth (Optional)
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-secret
GITHUB_CLIENT_ID=your-github-client-id
GITHUB_CLIENT_SECRET=your-github-secret

# Email (Gmail Example)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
SENDER_EMAIL=your-email@gmail.com

# Redis
REDIS_URL=redis://localhost:6379/0

# Celery
CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/0

# Frontend URL
FRONTEND_URL=http://localhost:5173
```

#### 4. Database Setup

```bash
# Start PostgreSQL and Redis (if not running)
# Then run migrations
alembic upgrade head
```

#### 5. Start Backend Services

```bash
# Terminal 1: FastAPI server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Terminal 2: Celery worker
celery -A app.core.celery.celery_app worker --loglevel=info

# Terminal 3: Celery beat (scheduler)
celery -A app.core.celery.celery_app beat --loglevel=info

# Terminal 4: Flower (monitoring - optional)
celery -A app.core.celery.celery_app flower --port=5555
```

#### 6. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

**Access Points:**

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Flower Dashboard: http://localhost:5555

### Option 2: Docker Deployment

#### 1. Clone & Configure

```bash
git clone https://github.com/yourusername/fastapi-saas-boilerplate.git
cd fastapi-saas-boilerplate
cp .env.example .env
# Edit .env with your settings
```

#### 2. Start All Services

```bash
docker-compose up -d
```

This starts 8 services:

- `backend` - FastAPI application
- `frontend` - React application
- `postgres` - PostgreSQL database
- `redis` - Redis cache/broker
- `celery-worker` - Background task processor
- `celery-beat` - Task scheduler
- `flower` - Celery monitoring
- `nginx` - Reverse proxy (optional)

#### 3. Run Migrations

```bash
docker-compose exec backend alembic upgrade head
```

#### 4. Access Services

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Flower: http://localhost:5555

#### 5. View Logs

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f backend
docker-compose logs -f celery-worker
```

#### 6. Stop Services

```bash
docker-compose down        # Stop containers
docker-compose down -v     # Stop and remove volumes (deletes data)
```

---

## 🏢 Multi-Tenancy & SaaS

### Organization Model

Each organization is a **tenant** with isolated data:

```python
class Organization(Base):
    id: UUID                    # Unique identifier
    name: str                   # Organization name
    created_at: datetime        # Creation timestamp
    invite_token: str           # Join token
    users: List[User]           # Associated users
```

### Multi-Organization User Flow

```mermaid
graph TD
    A[User Signs Up] --> B{Invite Token?}
    B -->|Yes| C[Join Existing Org]
    B -->|No| D[Create New Org]
    C --> E[Add to Organization]
    D --> F[Become Org Owner]
    E --> G[Email Verification]
    F --> G
    G --> H{Email Verified?}
    H -->|Yes| I[Access Dashboard]
    H -->|No| J[Pending Verification]
    J --> K[Receive OTP Email]
    K --> L[Enter OTP]
    L --> I
```

### Key Concepts

1. **Same Email, Multiple Orgs**: A user with `user@example.com` can exist in Organization A and Organization B
2. **Invite Tokens**: Each organization has a unique invite token for new members
3. **OAuth Multi-Org**: OAuth users can join multiple organizations
4. **Data Isolation**: Users see only data from their current organization context

### Usage Examples

#### Create Organization

```bash
POST /api/v1/organizations/
{
  "name": "Acme Corp"
}

Response:
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Acme Corp",
  "invite_token": "acmecorp-a1b2c3",
  "created_at": "2024-01-15T10:30:00"
}
```

#### Join with Invite Token

```bash
POST /api/v1/auth/register
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "full_name": "John Doe",
  "invite_token": "acmecorp-a1b2c3"
}
```

#### List User's Organizations

```bash
GET /api/v1/organizations/my-organizations

Response:
[
  {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Acme Corp",
    "role": "owner"
  },
  {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "name": "Beta Inc",
    "role": "member"
  }
]
```

---

## 📡 API Endpoints

### Authentication

| Method | Endpoint                    | Description             | Auth Required |
| ------ | --------------------------- | ----------------------- | ------------- |
| POST   | `/api/v1/auth/register`     | Register new user       | No            |
| POST   | `/api/v1/auth/login`        | Login with credentials  | No            |
| POST   | `/api/v1/auth/verify-email` | Verify email with OTP   | No            |
| POST   | `/api/v1/auth/resend-otp`   | Resend verification OTP | No            |
| GET    | `/api/v1/auth/me`           | Get current user info   | Yes           |
| POST   | `/api/v1/auth/logout`       | Logout user             | Yes           |

### OAuth

| Method | Endpoint                       | Description           | Auth Required |
| ------ | ------------------------------ | --------------------- | ------------- |
| GET    | `/api/v1/auth/google/login`    | Initiate Google OAuth | No            |
| GET    | `/api/v1/auth/google/callback` | Google OAuth callback | No            |
| GET    | `/api/v1/auth/github/login`    | Initiate GitHub OAuth | No            |
| GET    | `/api/v1/auth/github/callback` | GitHub OAuth callback | No            |

### Organizations

| Method | Endpoint                                 | Description              | Auth Required |
| ------ | ---------------------------------------- | ------------------------ | ------------- |
| POST   | `/api/v1/organizations/`                 | Create organization      | Yes           |
| GET    | `/api/v1/organizations/`                 | List all organizations   | Yes           |
| GET    | `/api/v1/organizations/{id}`             | Get organization details | Yes           |
| PUT    | `/api/v1/organizations/{id}`             | Update organization      | Yes           |
| DELETE | `/api/v1/organizations/{id}`             | Delete organization      | Yes           |
| GET    | `/api/v1/organizations/my-organizations` | Get user's organizations | Yes           |
| POST   | `/api/v1/organizations/{id}/invite`      | Generate invite token    | Yes           |

### Users

| Method | Endpoint             | Description      | Auth Required |
| ------ | -------------------- | ---------------- | ------------- |
| GET    | `/api/v1/users/`     | List users       | Yes           |
| GET    | `/api/v1/users/{id}` | Get user details | Yes           |
| PUT    | `/api/v1/users/{id}` | Update user      | Yes           |
| DELETE | `/api/v1/users/{id}` | Delete user      | Yes           |

### Background Jobs

| Method | Endpoint               | Description             | Auth Required |
| ------ | ---------------------- | ----------------------- | ------------- |
| POST   | `/api/v1/jobs/pause`   | Pause background tasks  | Yes           |
| POST   | `/api/v1/jobs/resume`  | Resume background tasks | Yes           |
| GET    | `/api/v1/jobs/status`  | Get task status         | Yes           |
| GET    | `/api/v1/jobs/cleanup` | Trigger cleanup job     | Yes           |

### Health & Monitoring

| Method | Endpoint  | Description          | Auth Required |
| ------ | --------- | -------------------- | ------------- |
| GET    | `/health` | Health check         | No            |
| GET    | `/docs`   | API documentation    | No            |
| GET    | `/redoc`  | Alternative API docs | No            |

---

## 📧 Email Configuration

### Gmail Setup (Recommended)

1. **Enable 2-Factor Authentication** in your Google account
2. **Generate App Password**:
   - Go to: https://myaccount.google.com/apppasswords
   - Select "Mail" and your device
   - Copy the 16-character password
3. **Update `.env`**:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-16-char-app-password
SENDER_EMAIL=your-email@gmail.com
```

### Email Templates

Located in `app/templates/emails/`:

- `otp_email.html` - Email verification OTP
- `welcome_email.html` - Welcome message after registration
- `reminder_email.html` - Daily inactive user reminder

### Customization

Edit HTML templates to match your brand:

```html
<!-- app/templates/emails/otp_email.html -->
<div style="font-family: Arial, sans-serif;">
  <h1>Verify Your Email</h1>
  <p>Your verification code is: <strong>{{ otp_code }}</strong></p>
  <p>Valid for 24 hours.</p>
</div>
```

---

## ⚙️ Background Jobs

### Task Types

1. **Email Queue** (`email_queue`)
   - OTP verification emails
   - Welcome emails
   - Organization invite emails
   - Retry: 3 attempts with exponential backoff

2. **Maintenance Queue** (`maintenance_queue`)
   - Database cleanup (15+ day old tasks)
   - Scheduled daily reminders
   - System health checks

### Celery Workers

```bash
# Start worker with specific queue
celery -A app.core.celery.celery_app worker -Q email_queue --loglevel=info

# Start all queues
celery -A app.core.celery.celery_app worker --loglevel=info
```

### Scheduled Tasks (Celery Beat)

```python
# Daily cleanup at 2 AM
@celery_app.task
def cleanup_old_tasks():
    """Delete tasks older than 15 days"""
    # Implementation in app/core/celery/tasks/maintenance.py

# Daily reminder at 10 AM
@celery_app.task
def send_daily_reminders():
    """Send reminders to inactive users"""
    # Implementation in app/core/celery/tasks/email.py
```

### Pause/Resume Control

```bash
# Pause email tasks
POST /api/v1/jobs/pause
{
  "task_type": "email"
}

# Resume email tasks
POST /api/v1/jobs/resume
{
  "task_type": "email"
}

# Check status
GET /api/v1/jobs/status
```

### Flower Monitoring

Access Celery task dashboard:

```bash
# Local: http://localhost:5555
# Docker: http://localhost:5555

# View:
# - Active tasks
# - Completed tasks
# - Failed tasks
# - Worker status
# - Task history
```

---

## 🔐 Security Features

### Password Security

- **Argon2** hashing (primary)
- **Bcrypt** fallback support
- Minimum 8 characters
- Requires: uppercase, lowercase, number, special character

### Rate Limiting

```python
# Default limits
- Login: 5 requests/minute
- Register: 3 requests/minute
- Email sending: 10 requests/minute
- API endpoints: 100 requests/minute
```

Configure in `app/core/middleware/rate_limiter.py`

### SQL Injection Protection

Custom middleware checks all requests for SQL injection patterns:

```python
# Blocked patterns
UNION, SELECT, DROP, INSERT, UPDATE, DELETE, --, /*
```

### CORS Configuration

```python
# Allowed origins (production)
origins = [
    "https://yourdomain.com",
    "https://app.yourdomain.com"
]

# Development
origins = ["http://localhost:5173"]
```

### JWT Token Management

```python
# Access token: 30 minutes (default)
# Refresh token: 7 days (optional)
# Algorithm: HS256
# Secret: Environment variable SECRET_KEY
```

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py

# Run with verbose output
pytest -v

# Run and show print statements
pytest -s
```

### Test Database

- **Automatic Setup**: Test database created before each test session
- **Isolation**: Each test runs in a transaction that's rolled back
- **Cleanup**: Test database is automatically deleted after all tests complete
- **Mocked Services**: Email, OAuth, and external APIs are mocked

### Test Structure

```python
# tests/conftest.py - Shared fixtures
@pytest.fixture
def test_db():
    """Create test database and clean up after"""
    # Setup
    yield db
    # Teardown - database deleted here

@pytest.fixture
def test_client():
    """FastAPI test client"""
    return TestClient(app)

# tests/test_auth.py - Authentication tests
def test_register_user(test_client):
    response = test_client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "password": "SecurePass123!",
        "full_name": "Test User"
    })
    assert response.status_code == 201
```

### Coverage Report

```bash
# Generate HTML coverage report
pytest --cov=app --cov-report=html

# Open in browser
open htmlcov/index.html
```

---

## 🐳 Docker Services

### Service Overview

| Service       | Port | Description                  |
| ------------- | ---- | ---------------------------- |
| backend       | 8000 | FastAPI application          |
| frontend      | 3000 | React application            |
| postgres      | 5432 | PostgreSQL database          |
| redis         | 6379 | Redis cache & message broker |
| celery-worker | -    | Background task processor    |
| celery-beat   | -    | Task scheduler               |
| flower        | 5555 | Celery monitoring dashboard  |
| nginx         | 80   | Reverse proxy (optional)     |

### Docker Commands

```bash
# Start all services
docker-compose up -d

# View logs
docker-compose logs -f backend
docker-compose logs -f celery-worker

# Restart a service
docker-compose restart backend

# Execute command in container
docker-compose exec backend alembic upgrade head
docker-compose exec backend pytest

# Stop all services
docker-compose down

# Remove volumes (deletes data)
docker-compose down -v

# Rebuild containers
docker-compose up -d --build
```

### Production Deployment

```yaml
# docker-compose.prod.yml
services:
  backend:
    environment:
      - ENVIRONMENT=production
      - DEBUG=false
    deploy:
      replicas: 3
      restart_policy:
        condition: on-failure
```

---

## 🔧 Troubleshooting

### Common Issues

#### 1. Database Connection Error

```
Error: could not connect to server: Connection refused
```

**Solution:**

```bash
# Check PostgreSQL is running
sudo service postgresql status

# Verify connection details in .env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

#### 2. Redis Connection Error

```
Error: Error 111 connecting to localhost:6379. Connection refused.
```

**Solution:**

```bash
# Start Redis
sudo service redis-server start

# Verify Redis is running
redis-cli ping  # Should return PONG
```

#### 3. Celery Worker Not Processing Tasks

```bash
# Check worker status
celery -A app.core.celery.celery_app inspect active

# Restart worker
# Kill existing workers
pkill -f 'celery worker'

# Start fresh worker
celery -A app.core.celery.celery_app worker --loglevel=info
```

#### 4. Email Not Sending

**Check:**

- SMTP credentials in `.env`
- Gmail App Password (not regular password)
- Celery worker is running
- Check Flower dashboard for failed tasks

#### 5. Migration Errors

```bash
# Reset migrations (CAUTION: deletes data)
alembic downgrade base
alembic upgrade head

# Create new migration
alembic revision --autogenerate -m "description"
```

#### 6. Frontend Not Connecting to Backend

**Check:**

- Backend is running on port 8000
- CORS origins include frontend URL
- `VITE_API_URL` in frontend `.env`

#### 7. Docker Build Failures

```bash
# Clean Docker cache
docker system prune -a

# Rebuild without cache
docker-compose build --no-cache

# Check logs
docker-compose logs backend
```

---

## 🗺️ Roadmap

### Completed ✅

- [x] Multi-tenant architecture
- [x] JWT authentication
- [x] OAuth2 (Google & GitHub)
- [x] Email verification with OTP
- [x] Background job processing
- [x] Rate limiting & security
- [x] Docker deployment
- [x] Complete test suite
- [x] API documentation

### In Progress 🚧

- [ ] Password reset functionality
- [ ] User profile management
- [ ] Advanced role-based access control (RBAC)
- [ ] Organization settings & preferences

### Planned 📋

- [ ] Two-factor authentication (2FA)
- [ ] Webhooks support
- [ ] API key management
- [ ] Audit logging
- [ ] File upload service
- [ ] Notification system (push, SMS)
- [ ] Stripe payment integration
- [ ] Team member roles & permissions
- [ ] Activity dashboard
- [ ] Analytics & reporting

### Future Enhancements 🔮

- [ ] GraphQL API support
- [ ] Kubernetes deployment configs
- [ ] CI/CD pipeline templates
- [ ] Mobile app (React Native)
- [ ] Multi-language support (i18n)
- [ ] Advanced monitoring & alerting
- [ ] Data export/import tools
- [ ] SSO (SAML, LDAP)

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Development Setup

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests (`pytest`)
5. Commit changes (`git commit -m 'Add amazing feature'`)
6. Push to branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

### Code Standards

- Follow PEP 8 style guide
- Add type hints to all functions
- Write docstrings for modules, classes, and functions
- Maintain test coverage above 80%
- Update documentation for new features

### Testing Requirements

All PRs must:

- Pass all existing tests
- Add tests for new features
- Maintain or improve code coverage
- Pass linting checks

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - Database toolkit
- [Celery](https://docs.celeryq.dev/) - Distributed task queue
- [Alembic](https://alembic.sqlalchemy.org/) - Database migrations
- [Pydantic](https://docs.pydantic.dev/) - Data validation
- [Authlib](https://authlib.org/) - OAuth integration

---

## 📞 Support

- **Documentation**: [API Docs](http://localhost:8000/docs)
- **Issues**: [GitHub Issues](https://github.com/yourusername/fastapi-saas-boilerplate/issues)
- **Email**: support@yourdomain.com

---

<div align="center">

**Built with ❤️ using FastAPI**

⭐ Star this repo if you find it helpful!

</div>
