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
- ✅ Test database isolation
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
├── 📂 app/                          # Application source code
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
├── 📂 migrations/                   # Alembic database migrations
│
├── 📂 tests/                        # Test suite
│   ├── 📂 Unit/                     # Unit tests
│   ├── 📂 E2E/                      # End-to-end tests
│   ├── conftest.py                  # Pytest fixtures
│   └── pytest.ini                   # Pytest config
│
├── 📂 scripts/                      # Utility scripts
├── 📂 docs/                         # Documentation
├── .env.example                     # Environment template
├── .gitignore                       # Git ignore
├── alembic.ini                      # Alembic config
├── docker-compose.yml               # Docker Compose
├── Dockerfile                       # Docker image
├── pyproject.toml                   # Project config
├── requirements.txt                 # Dependencies
├── requirements-dev.txt             # Dev dependencies
└── README.md                        # This file
```

---

## 🚀 Installation & Setup

### Prerequisites

- **Python** 3.8+ ([Download](https://www.python.org/downloads/))
- **PostgreSQL** 13+ ([Download](https://www.postgresql.org/download/))
- **Redis** 7+ ([Download](https://redis.io/download))
- **Git** ([Download](https://git-scm.com/downloads))
- **Google OAuth Credentials** ([Get Here](https://console.cloud.google.com/))
- **GitHub OAuth App** ([Create Here](https://github.com/settings/developers))

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/fastapi-saas-boilerplate.git
cd fastapi-saas-boilerplate
```

### Step 2: Create Virtual Environment

<details>
<summary><b>🪟 Windows</b></summary>

```bash
python -m venv venv
venv\Scripts\activate
```

</details>

<details>
<summary><b>🍎 macOS / 🐧 Linux</b></summary>

```bash
python3 -m venv venv
source venv/bin/activate
```

</details>

### Step 3: Install Dependencies

```bash
# Production dependencies
pip install -r requirements.txt

# Or with dev dependencies for testing
pip install -r requirements-dev.txt
```

### Step 4: Database Setup

```bash
# Create database
createdb fastapi_saas_db

# Run migrations
alembic upgrade head
```

### Step 5: Environment Configuration

```bash
# Copy environment template
cp .env.example .env

# Generate secret key
python -c "import secrets; print(secrets.token_hex(32))"
```

Edit `.env` with your configuration:

```bash
# ========================================
# DATABASE
# ========================================
DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_saas_db

# ========================================
# JWT
# ========================================
SECRET_KEY=your_32_char_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ========================================
# GOOGLE OAUTH
# ========================================
GOOGLE_CLIENT_ID=your_client_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback

# ========================================
# GITHUB OAUTH
# ========================================
GITHUB_CLIENT_ID=your_client_id
GITHUB_CLIENT_SECRET=your_client_secret
GITHUB_REDIRECT_URI=http://localhost:8000/auth/github/callback

# ========================================
# REDIS (Celery)
# ========================================
REDIS_BROKER_URL=redis://localhost:6379/0
REDIS_RESULT_BACKEND=redis://localhost:6379/1

# ========================================
# EMAIL (Gmail)
# ========================================
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=465
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_16_char_app_password
SMTP_FROM_EMAIL=your_email@gmail.com
SMTP_FROM_NAME=Your App Name

# ========================================
# CORS
# ========================================
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000
```

### Step 6: Run Application

```bash
# Development mode (with auto-reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Production mode (with workers)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

✅ **API:** [http://localhost:8000](http://localhost:8000)  
📚 **Swagger Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)  
📖 **ReDoc:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 🏢 Multi-Tenancy & SaaS Architecture

### Overview

Complete SaaS multi-tenant system where users belong to organizations. Same email can exist across different organizations.

**Key Features:**

- Organization-based data isolation
- Invite token system for secure joining
- Same email across multiple organizations
- OAuth support for multiple org scenarios
- JWT includes organization context
- Organization-scoped operations

### Multi-Tenancy Rules

| Rule                         | Implementation                               |
| ---------------------------- | -------------------------------------------- |
| Same email across orgs       | Composite unique: `(email, organization_id)` |
| Email unique within org      | Same composite constraint                    |
| Users can join multiple orgs | Separate accounts per org                    |
| OAuth in multiple orgs       | Separate OAuth records per org               |
| Organization isolation       | All queries filtered by org_id               |

### Database Models

**Organization:**

```python
class Organization(Base):
    __tablename__ = "organizations"

    id: int                 # Primary key
    name: str               # Organization name
    invite_token: str       # Unique UUID for invites
    created_at: datetime    # Creation timestamp
```

**User (Multi-Tenant):**

```python
class User(Base):
    __tablename__ = "users"

    id: int                     # Primary key
    email: str                  # NOT unique globally
    first_name: str
    last_name: str
    password: str | None        # Null for OAuth
    is_verified: bool           # Email verification status
    organization_id: int        # FK to organizations
    oauth_provider: str | None  # 'google' | 'github'
    oauth_id: str | None        # Provider-specific ID
    created_at: datetime

    # Composite unique constraint
    __table_args__ = (
        UniqueConstraint('email', 'organization_id'),
    )
```

### Organization Workflow

```bash
# 1. Create organization
POST /organizations/create
{
  "name": "Acme Corp"
}
Response: {
  "id": 1,
  "name": "Acme Corp",
  "invite_token": "abc123-def456-ghi789",
  "created_at": "2024-01-15T10:00:00Z"
}

# 2. Register user with invite token
POST /users/register
{
  "email": "john@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "password": "SecurePass123!",
  "invite_token": "abc123-def456-ghi789"
}

# 3. OAuth login with invite (user clicks invite link)
GET /auth/google/login?invite_token=abc123-def456-ghi789
# System validates token, creates user in organization

# 4. Login to specific organization
POST /auth/login
{
  "username": "john@example.com",
  "password": "SecurePass123!",
  "organization_id": 1
}
```

---

## 📡 API Endpoints

### Organization Endpoints

| Method | Endpoint                | Description          | Auth |
| ------ | ----------------------- | -------------------- | ---- |
| `POST` | `/organizations/create` | Create organization  | ❌   |
| `GET`  | `/organizations/`       | List organizations   | ❌   |
| `POST` | `/organizations/join`   | Get org invite token | ❌   |

### Authentication Endpoints

| Method | Endpoint                     | Description            | Rate Limit | Auth |
| ------ | ---------------------------- | ---------------------- | ---------- | ---- |
| `POST` | `/auth/login`                | Login with credentials | 5/min      | ❌   |
| `POST` | `/auth/request-verification` | Request OTP email      | 5/min      | ✅   |
| `POST` | `/auth/verify-otp`           | Verify with OTP code   | 5/min      | ✅   |
| `GET`  | `/auth/google/login`         | Google OAuth redirect  | 10/min     | ❌   |
| `GET`  | `/auth/google/callback`      | Google callback        | 10/min     | ❌   |
| `GET`  | `/auth/github/login`         | GitHub OAuth redirect  | 10/min     | ❌   |
| `GET`  | `/auth/github/callback`      | GitHub callback        | 10/min     | ❌   |

### User Endpoints

| Method | Endpoint          | Description             | Auth |
| ------ | ----------------- | ----------------------- | ---- |
| `POST` | `/users/register` | Register with invite    | ❌   |
| `GET`  | `/users/me`       | Get current user        | ✅   |
| `POST` | `/users/logout`   | Logout/invalidate token | ✅   |

### Job Control Endpoints

| Method | Endpoint                | Description          |
| ------ | ----------------------- | -------------------- |
| `GET`  | `/jobs/workers`         | Get Celery workers   |
| `GET`  | `/jobs/active`          | Get running tasks    |
| `POST` | `/jobs/trigger/cleanup` | Trigger cleanup task |
| `GET`  | `/jobs/task/{task_id}`  | Get task status      |
| `POST` | `/jobs/pause`           | Pause task type      |
| `POST` | `/jobs/resume`          | Resume paused task   |
| `GET`  | `/jobs/paused`          | Get paused tasks     |

---

## 📧 Email System

### Overview

Complete email system with SMTP delivery, async processing, and organization context.

**Features:**

- OTP verification emails with 6-digit codes
- Welcome emails with organization name
- Daily reminder emails for inactive users
- Customizable email templates
- Async delivery via Celery
- Retry mechanism (3 attempts)
- Gevent pool (50 concurrent)

### Email Types

| Email        | Trigger                    | Variables                      |
| ------------ | -------------------------- | ------------------------------ |
| **OTP**      | User requests verification | first_name, otp_code, org_name |
| **Welcome**  | User verifies OTP          | first_name, email, org_name    |
| **Reminder** | Daily scheduled task       | first_name, org_name           |

### Gmail Configuration

```bash
# 1. Enable 2-Step Verification
#    Settings → Security → 2-Step Verification

# 2. Generate App Password
#    Settings → App passwords (select Mail & Other)

# 3. Add to .env
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=abcdabcdabcdabcd  # 16-char password, no spaces

# 4. Test connection
python -c "
import smtplib
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('your_email@gmail.com', 'your_app_password')
print('✅ SMTP Success!')
smtp.quit()
"
```

---

## 🔄 Background Jobs (Celery)

### Overview

Asynchronous task processing with Celery, Redis broker, Celery Beat scheduler, and Flower monitoring.

**Architecture:**

```
FastAPI → Redis (Broker) → Celery Workers → Tasks
                    ↓
              Celery Beat (Scheduler)
                    ↓
              Flower (Monitoring)
```

### Task Queues

| Queue               | Purpose          | Workers | Concurrency | Tasks                   |
| ------------------- | ---------------- | ------- | ----------- | ----------------------- |
| `email_queue`       | Send emails      | gevent  | 50          | OTP, Welcome, Reminder  |
| `maintenance_queue` | Database cleanup | prefork | 1           | Cleanup expired results |

### Available Tasks

| Task                           | Type      | Schedule      | Purpose                         |
| ------------------------------ | --------- | ------------- | ------------------------------- |
| `send_verification_email`      | Async     | On-demand     | Send OTP code                   |
| `send_welcome_email`           | Async     | On-demand     | Send welcome after verification |
| `send_reminder_email`          | Scheduled | Daily 9 AM    | Inactive user reminders         |
| `cleanup_expired_task_results` | Scheduled | Every 15 days | Delete old results              |

### Pause/Resume System

Control task execution without code changes:

```bash
# Pause a task type
POST /jobs/pause
{
  "task_name": "welcome_email"
}

# Resume a paused task
POST /jobs/resume
{
  "task_name": "welcome_email"
}

# Check paused tasks
GET /jobs/paused
```

### Local Development

```bash
# Terminal 1: Redis
redis-server

# Terminal 2: Email Worker
celery -A app.core.celery.celery_app worker \
  -Q email_queue \
  --pool=gevent \
  --concurrency=50 \
  --loglevel=info

# Terminal 3: Cleanup Worker
celery -A app.core.celery.celery_app worker \
  -Q maintenance_queue \
  --concurrency=1 \
  --loglevel=info

# Terminal 4: Celery Beat (Scheduler)
celery -A app.core.celery.celery_app beat --loglevel=info

# Terminal 5: Flower (Monitor)
celery -A app.core.celery.celery_app flower --port=5555
# Access at http://localhost:5555
```

### Docker

```bash
# All workers run automatically
docker-compose up -d

# View logs
docker-compose logs -f celery_email_worker
docker-compose logs -f celery_beat

# Flower UI
open http://localhost:5555
```

---

## 🛡️ Security Features

### 1. SQL Injection Protection

Custom middleware blocks malicious SQL patterns:

- SQL keywords: SELECT, INSERT, DROP, UNION, DELETE
- SQL comments: --, /\*\*/, #
- Conditions: OR 1=1, AND 1=1
- Commands: EXEC, xp_cmdshell

### 2. Rate Limiting

Configurable rate limits prevent brute force:

```bash
# Login: 5 requests/minute
# Register: 5 requests/minute
# OAuth: 10 requests/minute
```

### 3. Password Security

- Argon2 & Bcrypt hashing with automatic salt
- 72-byte limit handling
- SHA-256 pre-hashing option
- Passwords never stored in plain text

### 4. JWT Security

- Configurable expiration (default: 30 minutes)
- HMAC-SHA256 signing
- Organization ID in payload
- Secure cryptographic generation

### 5. CORS Protection

```python
allow_origins=[
    "http://localhost:3000",  # Dev
    "https://yourdomain.com"  # Prod
]
```

### 6. Multi-Tenant Isolation

- Organization-scoped queries
- JWT includes organization_id
- Composite unique constraints
- Data access layer enforcement

---

## 🧪 Testing

### Test Structure

```
tests/
├── conftest.py           # Shared fixtures
├── Unit/                 # Isolated, mocked tests
│   └── test_*.py
└── E2E/                  # Real API calls
    └── test_*.py
```

### Running Tests

```bash
# All tests
pytest

# Unit only
pytest tests/Unit/

# E2E only
pytest tests/E2E/

# With coverage
pytest --cov=app --cov-report=html

# Specific test
pytest tests/E2E/test_auth_flow.py -v
```

### Coverage Report

```bash
# Generate HTML report
pytest --cov=app --cov-report=html
open htmlcov/index.html
```

---

## 🐳 Docker Deployment

### Services

- 🚀 **FastAPI** (port 8000)
- 🐘 **PostgreSQL** (port 5432)
- 🔴 **Redis** (port 6379)
- 📨 **Celery Email Worker**
- 🧹 **Celery Cleanup Worker**
- ⏰ **Celery Beat**
- 🌸 **Flower** (port 5555)
- 🛠️ **pgAdmin** (port 5050)

### Quick Start

```bash
# Clone
git clone https://github.com/yourusername/fastapi-saas-boilerplate.git
cd fastapi-saas-boilerplate

# Setup
cp .env.example .env
# Edit .env with your settings

# Run
docker-compose up -d --build

# Migrate
docker exec -it fastapi_app alembic upgrade head

# Check
docker-compose logs -f
```

### Access Points

| Service        | URL                         | Credentials             |
| -------------- | --------------------------- | ----------------------- |
| **API**        | http://localhost:8000       | -                       |
| **Swagger**    | http://localhost:8000/docs  | -                       |
| **ReDoc**      | http://localhost:8000/redoc | -                       |
| **Flower**     | http://localhost:5555       | -                       |
| **pgAdmin**    | http://localhost:5050       | admin@admin.com / admin |
| **PostgreSQL** | localhost:5432              | postgres / postgres     |
| **Redis**      | localhost:6379              | -                       |

### Common Commands

```bash
# Start
docker-compose up -d

# Rebuild
docker-compose up -d --build

# Stop
docker-compose down

# Logs
docker-compose logs -f

# Specific service
docker-compose logs -f fastapi_app
docker-compose logs -f celery_email_worker

# Execute command
docker exec -it fastapi_app bash
docker exec -it fastapi_app alembic upgrade head
```

---

## 🗄️ Database Migrations (Alembic)

### Commands

```bash
# Generate migration
alembic revision --autogenerate -m "add field"

# Apply all
alembic upgrade head

# Rollback one
alembic downgrade -1

# Check current
alembic current

# View history
alembic history --verbose
```

### Docker

```bash
# Generate
docker exec -it fastapi_app alembic revision --autogenerate -m "description"

# Apply
docker exec -it fastapi_app alembic upgrade head

# Rollback
docker exec -it fastapi_app alembic downgrade -1
```

---

## 🐛 Troubleshooting

### Email Not Sending

**Solution:**

1. Generate new Gmail App Password (no spaces)
2. Enable 2-Step Verification on Google Account
3. Test connection: `python -c "import smtplib; smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465); smtp.login('email@gmail.com', 'password'); print('✅ OK')"`

### Celery Tasks Not Processing

**Solution:**

```bash
# Check workers running
docker-compose ps | grep celery

# Check Redis
docker exec -it fastapi_redis redis-cli ping

# Restart workers
docker restart fastapi_celery_email_worker
docker restart fastapi_celery_cleanup_worker
```

### Organization Invite Token Invalid

**Solution:**

1. Verify token exists: `SELECT * FROM organizations WHERE invite_token = 'token';`
2. Check token format (should be UUID)
3. Ensure no extra spaces
4. Case-sensitive

### Database Connection Failed

**Solution (Local):**

```bash
# Check PostgreSQL
pg_isready

# Create database
createdb fastapi_saas_db

# Verify DATABASE_URL in .env
```

**Solution (Docker):**

```bash
# Restart database
docker restart fastapi_db

# Check logs
docker logs fastapi_db

# Recreate
docker-compose down -v
docker-compose up -d
docker exec -it fastapi_app alembic upgrade head
```

### Module Import Errors

**Solution (Local):**

1. Activate virtual environment
2. Install in editable mode: `pip install -e .`
3. Check `__init__.py` files exist

**Solution (Docker):**

```bash
# Rebuild
docker-compose down
docker-compose up -d --build

# Check Python path
docker exec -it fastapi_app python -c "import sys; print(sys.path)"
```

---

## 📚 What's Included

✅ Multi-tenant SaaS architecture  
✅ JWT + OAuth2 authentication  
✅ Email verification with OTP  
✅ Organization management  
✅ Celery background tasks  
✅ Pause/Resume task control  
✅ Security middleware stack  
✅ Repository pattern  
✅ Password hashing (Argon2/bcrypt)  
✅ Database models (User, Org, OTP, TaskControl)  
✅ Request validation (Pydantic)  
✅ Auto-generated API docs  
✅ Docker Compose setup  
✅ Alembic migrations  
✅ Complete test suite  
✅ Flower monitoring  
✅ Organization-aware emails  
✅ Daily reminders

---

## 🚦 Roadmap

### ✅ Completed

- [x] Multi-tenant SaaS architecture
- [x] Organization management
- [x] JWT authentication
- [x] Email verification OTP
- [x] OAuth (Google & GitHub)
- [x] Celery background jobs
- [x] Pause/Resume control
- [x] Docker setup
- [x] Database migrations
- [x] Rate limiting
- [x] Security middleware
- [x] Test suite
- [x] Welcome/reminder emails

### 🚧 Planned

- [ ] Password reset
- [ ] Refresh tokens
- [ ] User profile CRUD
- [ ] Role-based access control (RBAC)
- [ ] Organization members management
- [ ] Organization settings
- [ ] Automated invite emails
- [ ] API versioning
- [ ] Logging & monitoring
- [ ] Two-factor authentication (2FA)
- [ ] Session dashboard
- [ ] Advanced rate limiting (per org)
- [ ] File uploads
- [ ] WebSocket support
- [ ] Kubernetes manifests
- [ ] CI/CD templates
- [ ] Usage analytics

---

## 📊 Statistics

| Metric                | Count   |
| --------------------- | ------- |
| **Lines of Code**     | ~8,000+ |
| **API Endpoints**     | 20+     |
| **Database Tables**   | 5+      |
| **Middleware**        | 5+      |
| **Docker Services**   | 8       |
| **Celery Queues**     | 2       |
| **Background Tasks**  | 4+      |
| **Security Features** | 10+     |
| **Test Coverage**     | 85%+    |
| **Test Files**        | 8+      |

---

## 🤝 Contributing

Contributions welcome! Steps:

1. Fork repository
2. Create feature branch: `git checkout -b feature/Amazing`
3. Commit changes: `git commit -m 'Add Amazing'`
4. Push: `git push origin feature/Amazing`
5. Open Pull Request

---

## 📄 License

MIT License - See [LICENSE](LICENSE) file

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Validation
- [Authlib](https://authlib.org/) - OAuth
- [Python-JOSE](https://python-jose.readthedocs.io/) - JWT
- [Celery](https://docs.celeryq.dev/) - Task queue
- [Redis](https://redis.io/) - Cache/broker
- [Pytest](https://pytest.org/) - Testing

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Built with ❤️ for SaaS Applications**

[Report Bug](https://github.com/yourusername/fastapi-saas-boilerplate/issues) • [Request Feature](https://github.com/yourusername/fastapi-saas-boilerplate/issues)

</div>
