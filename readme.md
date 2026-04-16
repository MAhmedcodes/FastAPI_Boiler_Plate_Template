<div align="center">

# 🚀 FastAPI Authentication Boilerplate

### Professional, Production-Ready FastAPI Template with Complete Authentication System

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00a393?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13+-316192?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org)
[![JWT](https://img.shields.io/badge/JWT-Auth-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white)](https://jwt.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [API Docs](#-api-endpoints) • [Security](#-security-features) • [Contributing](#-contributing)

</div>

---

## 📖 Overview

A **complete, production-ready FastAPI boilerplate** featuring JWT authentication, OAuth2 integration (Google & GitHub), comprehensive security middleware, and modular architecture. Built with industry best practices for scalability and maintainability.

### Why This Boilerplate?

- ✅ **Production-Ready** - Battle-tested security features and error handling
- ✅ **Modular Architecture** - Clean separation of concerns with repository pattern
- ✅ **OAuth Integration** - Google and GitHub login out of the box
- ✅ **Enterprise Security** - Rate limiting, SQL injection protection, CORS
- ✅ **Developer Friendly** - Comprehensive documentation and examples
- ✅ **Type Safety** - Full Pydantic validation and type hints

---

## ✨ Features

<table>
<tr>
<td width="50%">

### 🔐 Authentication & Authorization

- JWT token-based authentication
- User registration with email validation
- Secure password storage (bcrypt)
- OAuth2 password flow compliance
- **Email verification with OTP**
- **6-digit codes, 24-hour expiry**
- **Provider locking** (no cross-provider auth)

</td>
<td width="50%">

### 🌐 OAuth Integration

- Google OAuth2 login
- GitHub OAuth2 login
- Automatic profile data extraction
- OAuth state management
- CSRF protection
- Provider-specific adapters
- **Auto-verification for OAuth users**

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ Security Features

- Rate limiting (5-10 req/min)
- SQL injection protection
- CORS configuration
- Password strength validation
- Secure session management
- XSS prevention
- **OTP expiration & single-use**

</td>
<td width="50%">

### 🏗️ Architecture

- Modular structure
- Repository pattern
- Service layer separation
- Dependency injection
- Environment-based config
- Database migrations (Alembic)
- **Celery background tasks**
- **Docker multi-service setup**

</td>
</tr>
<tr>
<td width="50%">

### 📧 Email System

- **SMTP email delivery (Gmail supported)**
- **Async task processing with Celery**
- **OTP verification emails**
- **Customizable email templates**
- **Retry mechanism (3 attempts)**
- **Email queue with gevent pool**

</td>
<td width="50%">

### 🔄 Background Jobs

- **Celery worker queues (email, cleanup)**
- **Scheduled tasks with Celery Beat**
- **Flower monitoring dashboard**
- **Redis message broker**
- **Gevent pool for email (50 concurrent)**
- **Automatic old OTP cleanup (daily)**

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| **Category**         | **Technology**          | **Purpose**                       |
| -------------------- | ----------------------- | --------------------------------- |
| **Framework**        | FastAPI 0.104+          | High-performance async API        |
| **ORM**              | SQLAlchemy 2.0          | Database abstraction              |
| **Database**         | PostgreSQL 13+          | Relational data storage           |
| **Cache/Queue**      | Redis 7+                | Celery message broker             |
| **Task Queue**       | Celery 5.3+             | Async background jobs             |
| **Authentication**   | Python-JOSE, PyJWT      | JWT token generation & validation |
| **OAuth**            | Authlib 1.2+            | Google & GitHub OAuth integration |
| **Password Hash**    | Passlib + bcrypt        | Secure password hashing           |
| **Email**            | smtplib (built-in)      | SMTP email delivery               |
| **Rate Limiting**    | SlowAPI                 | Request throttling                |
| **Validation**       | Pydantic 2.0            | Request/response validation       |
| **Server**           | Uvicorn                 | ASGI server                       |
| **Migrations**       | Alembic                 | Database version control          |
| **Monitoring**       | Flower                  | Celery task monitoring            |
| **Containerization** | Docker + Docker Compose | Multi-service deployment          |

---

## 📁 Project Structure

```
FastAPI-Boilerplate/
│
├── 📂 src/app/                      # Application source code
│   ├── 📂 core/                     # Core functionality
│   │   ├── 📂 config/               # Configuration & settings
│   │   │   ├── __init__.py
│   │   │   └── settings.py          # Environment variables
│   │   │
│   │   ├── 📂 database/             # Database connection
│   │   │   ├── __init__.py
│   │   │   └── session.py           # SQLAlchemy session
│   │   │
│   │   ├── 📂 dependencies/         # Dependency injection
│   │   │   ├── __init__.py
│   │   │   └── auth.py              # Auth dependencies
│   │   │
│   │   ├── 📂 middleware/           # Custom middleware
│   │   │   ├── __init__.py
│   │   │   ├── cors.py              # CORS configuration
│   │   │   ├── rate_limit.py        # Rate limiting
│   │   │   └── sql_injection.py     # SQL injection protection
│   │   │
│   │   └── 📂 security/             # Security handlers
│   │       ├── 📂 OAuth/            # OAuth providers
│   │       │   ├── google.py
│   │       │   └── github.py
│   │       └── 📂 OAuth2/           # JWT handling
│   │           └── jwt.py
│   │
│   ├── 📂 modules/                  # Feature modules
│   │   │
│   │   ├── 📂 auth/                 # Authentication module
│   │   │   ├── __init__.py
│   │   │   ├── 📂 repository/       # Data access layer
│   │   │   │   └── auth_repo.py
│   │   │   ├── 📂 router/           # API endpoints
│   │   │   │   └── auth_routes.py
│   │   │   ├── 📂 schema/           # Pydantic models
│   │   │   │   └── auth_schema.py
│   │   │   └── 📂 services/         # Business logic
│   │   │       └── auth_service.py
│   │   │
│   │   └── 📂 users/                # Users module
│   │       ├── __init__.py
│   │       ├── 📂 models/           # Database models
│   │       │   └── user_model.py
│   │       ├── 📂 repository/       # Data access layer
│   │       │   └── user_repo.py
│   │       ├── 📂 router/           # API endpoints
│   │       │   └── user_routes.py
│   │       ├── 📂 schema/           # Pydantic models
│   │       │   └── user_schema.py
│   │       └── 📂 services/         # Business logic
│   │           └── user_service.py
│   │
│   └── 📂 shared/                   # Shared utilities
│       └── 📂 utils/
│           └── password.py          # Password hashing
│
├── 📂 alembic/                      # Database migrations
│   ├── versions/
│   └── env.py
│
├── 📂 tests/                        # Test suite
│   ├── 📂 unit/                     # Unit tests
│   └── 📂 integration/              # Integration tests
│
├── 📂 scripts/                      # Utility scripts
│   └── init_db.py
│
├── 📂 docs/                         # Documentation
│   └── api.md
│
├── 📄 main.py                       # Application entry point
├── 📄 .env.example                  # Environment template
├── 📄 requirements.txt              # Dependencies
├── 📄 pyproject.toml                # Project configuration
├── 📄 alembic.ini                   # Alembic config
├── 📄 Dockerfile                    # Docker configuration
├── 📄 docker-compose.yml            # Docker Compose
└── 📄 README.md                     # This file
```

---

## 🚀 Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- **Python** 3.8 or higher ([Download](https://www.python.org/downloads/))
- **PostgreSQL** 13+ ([Download](https://www.postgresql.org/download/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Google OAuth Credentials** ([Get Here](https://console.cloud.google.com/))
- **GitHub OAuth App** ([Create Here](https://github.com/settings/developers))

---

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/fastapi-boilerplate.git
cd fastapi-boilerplate
```

---

### Step 2: Create Virtual Environment

<details open>
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

---

### Step 3: Install Dependencies

```bash
# Install production dependencies
pip install -r requirements.txt

# Or install with development dependencies
pip install -r requirements-dev.txt
```

<details>
<summary>📦 <b>Key Dependencies</b></summary>

```
fastapi>=0.104.0
uvicorn[standard]>=0.24.0
sqlalchemy>=2.0.0
alembic>=1.12.0
pydantic>=2.0.0
pydantic-settings>=2.0.0
python-jose[cryptography]>=3.3.0
passlib[bcrypt]>=1.7.4
authlib>=1.2.0
python-multipart>=0.0.6
slowapi>=0.1.9
psycopg2-binary>=2.9.9
```

</details>

---

### Step 4: Database Setup

```bash
# Create PostgreSQL database
createdb fastapi_boilerplate_db

# Run migrations
alembic upgrade head
```

---

### Step 5: Environment Configuration

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```bash
# ========================================
# DATABASE CONFIGURATION
# ========================================
DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_boilerplate_db

# ========================================
# JWT CONFIGURATION
# ========================================
SECRET_KEY=your_super_secret_key_here_min_32_characters
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# ========================================
# GOOGLE OAUTH CONFIGURATION
# ========================================
GOOGLE_CLIENT_ID=your_google_client_id.apps.googleusercontent.com
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:8000/auth/google/callback

# ========================================
# GITHUB OAUTH CONFIGURATION
# ========================================
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret
GITHUB_REDIRECT_URI=http://localhost:8000/auth/github/callback

# ========================================
# CORS CONFIGURATION
# ========================================
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:8000

# ========================================
# RATE LIMITING
# ========================================
RATE_LIMIT_LOGIN=5/minute
RATE_LIMIT_REGISTER=5/minute
RATE_LIMIT_OAUTH=10/minute
```

---

### Step 6: Generate Secret Key

```bash
# Generate a secure secret key
python -c "import secrets; print(secrets.token_hex(32))"
```

Copy the output to your `.env` file as `SECRET_KEY`.

---

### Step 7: Run Application

```bash
# Development mode (with auto-reload)
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Production mode (with workers)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

✅ **Application running at:** [http://localhost:8000](http://localhost:8000)

📚 **Interactive API Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

📖 **Alternative Docs:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## 📡 API Endpoints

### Authentication Endpoints

| Method | Endpoint                     | Description                  | Rate Limit | Auth Required |
| ------ | ---------------------------- | ---------------------------- | ---------- | ------------- |
| `POST` | `/auth/login`                | Login with credentials       | 5/minute   | ❌            |
| `POST` | `/auth/request-verification` | Request OTP email            | 5/minute   | ✅            |
| `POST` | `/auth/verify-otp`           | Submit OTP to verify account | 5/minute   | ✅            |
| `GET`  | `/auth/google/login`         | Google OAuth redirect        | 10/minute  | ❌            |
| `GET`  | `/auth/google/callback`      | Google OAuth callback        | 10/minute  | ❌            |
| `GET`  | `/auth/github/login`         | GitHub OAuth redirect        | 10/minute  | ❌            |
| `GET`  | `/auth/github/callback`      | GitHub OAuth callback        | 10/minute  | ❌            |

### User Endpoints

| Method | Endpoint          | Description       | Rate Limit | Auth Required |
| ------ | ----------------- | ----------------- | ---------- | ------------- |
| `POST` | `/users/register` | Register new user | 5/minute   | ❌            |
| `GET`  | `/users/me`       | Get current user  | -          | ✅            |

---

## 📝 Request/Response Examples

### 1️⃣ Register User

<details open>
<summary><b>Click to expand</b></summary>

**Request:**

```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john.doe@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "SecurePassword123!"
  }'
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user_id": 1,
  "email": "john.doe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "is_verified": false,
  "message": "User registered successfully. Please verify your email."
}
```

</details>

---

### 2️⃣ Request Email Verification OTP

<details>
<summary><b>Click to expand</b></summary>

**Request:**

```bash
curl -X POST "http://localhost:8000/auth/request-verification" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

**Response:**

```json
{
  "message": "Verification OTP sent to your email"
}
```

**Email Received:**

```
Subject: Verify Your Account

Your verification code is: 847291

This code expires in 24 hours.
```

</details>

---

### 3️⃣ Verify OTP

<details>
<summary><b>Click to expand</b></summary>

**Request:**

```bash
curl -X POST "http://localhost:8000/auth/verify-otp" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"otp_code": "847291"}'
```

**Response:**

```json
{
  "message": "User verified successfully"
}
```

</details>

---

### 4️⃣ Login

<details>
<summary><b>Click to expand</b></summary>

**Request:**

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john.doe@example.com&password=SecurePassword123!"
```

**Response:**

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

</details>

---

### 5️⃣ Google OAuth Flow

<details>
<summary><b>Click to expand</b></summary>

1. **Redirect user to:**

   ```
   GET http://localhost:8000/auth/google/login
   ```

2. **User authenticates with Google**

3. **Google redirects to:**

   ```
   GET http://localhost:8000/auth/google/callback?code=...&state=...
   ```

4. **Response contains JWT token:**
   ```json
   {
     "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
     "token_type": "bearer"
   }
   ```

</details>

---

### 6️⃣ Access Protected Route

<details>
<summary><b>Click to expand</b></summary>

**Request:**

```bash
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

**Response:**

```json
{
  "id": 1,
  "email": "john.doe@example.com",
  "first_name": "John",
  "last_name": "Doe",
  "created_at": "2024-01-15T10:30:00Z",
  "oauth_provider": null
}
```

</details>

---

## 📧 Email Verification & OTP System

### Overview

Complete email verification system with OTP (One-Time Password) for user account verification.

**Key Features:**

- ✅ **6-digit OTP codes** with 24-hour expiration
- ✅ **Synchronous email delivery** via SMTP (Gmail supported)
- ✅ **Provider locking** - Users can only login with registration method
- ✅ **Auto-verification** for OAuth users (Google/GitHub)
- ✅ **Celery background tasks** for email delivery (async processing)

---

### Verification Flow

```mermaid
sequenceDiagram
    participant U as User
    participant A as API
    participant C as Celery
    participant D as Database
    participant E as Email

    U->>A: Register (email/password)
    A->>D: Create user (is_verified=false)
    A->>U: Returns JWT token

    U->>A: POST /auth/request-verification
    A->>D: Generate OTP (expires 24h)
    A->>C: Queue email task
    C->>E: Send OTP via SMTP
    E->>U: OTP received

    U->>A: POST /auth/verify-otp
    A->>D: Validate OTP
    A->>D: Update user (is_verified=true)
    A->>U: Verification confirmed
```

---

### Provider Locking Rules

| Registration Method | Can Login With      | Email Verification Required |
| ------------------- | ------------------- | --------------------------- |
| Email/Password      | Email/Password only | ✅ Yes                      |
| Google OAuth        | Google only         | ❌ No (auto-verified)       |
| GitHub OAuth        | GitHub only         | ❌ No (auto-verified)       |

**Example:**

- User registers with email/password → Can only login with email/password (not Google/GitHub)
- User registers with Google → Can only login with Google (not email/password or GitHub)

---

### Email Configuration (Gmail)

Add to your `.env` file:

```bash
# ========================================
# EMAIL (SMTP) CONFIGURATION
# ========================================
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_16_char_app_password  # NO SPACES!
SMTP_FROM_EMAIL=your_email@gmail.com
SMTP_FROM_NAME=Your App Name
```

**Gmail Setup Steps:**

1. **Enable 2-Step Verification** on your Google Account
   - Go to: [Google Account Security](https://myaccount.google.com/security)

2. **Generate App Password**
   - Go to: [App Passwords](https://myaccount.google.com/apppasswords)
   - Select **"Mail"** and **"Other (Custom name)"**
   - Copy the 16-character password (**remove spaces**)

3. **Add to `.env`**
   ```bash
   SMTP_PASSWORD=abcdabcdabcdabcd  # Example: no spaces
   ```

---

### OTP Email Template

```
Subject: Verify Your Account

Hello {first_name},

Your verification code is: {otp_code}

This code expires in 24 hours.

If you didn't request this, please ignore this email.

Best regards,
{app_name}
```

---

### Database Schema

**User Model Updates:**

```python
class User(Base):
    # ... existing fields
    is_verified: bool = False          # New field
    oauth_provider: str | None         # 'google' | 'github' | None
```

**New OTP Model:**

```python
class OTP(Base):
    __tablename__ = "otps"

    id: int                            # Primary key
    user_id: int                       # Foreign key to users
    otp_code: str                      # 6-digit code
    expires_at: datetime               # 24 hours from creation
    is_used: bool = False              # Prevents reuse
    created_at: datetime
```

---

### Testing Email Verification

**1. Register a user:**

```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test123"
  }'
```

**2. Request OTP (use token from registration):**

```bash
curl -X POST "http://localhost:8000/auth/request-verification" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

**3. Check your email for 6-digit code**

**4. Verify with OTP:**

```bash
curl -X POST "http://localhost:8000/auth/verify-otp" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"otp_code": "123456"}'
```

---

### Test SMTP Connection

**Local:**

```bash
python -c "
import smtplib
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('your_email@gmail.com', 'your_app_password')
print('✅ SMTP Connection Successful!')
smtp.quit()
"
```

**Docker:**

```bash
docker exec -it fastapi_app python -c "
import smtplib
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtp.login('your_email@gmail.com', 'your_app_password')
print('✅ SMTP Connection Successful!')
smtp.quit()
"
```

---

## 🛡️ Security Features

### 1. SQL Injection Protection

Custom middleware automatically blocks malicious SQL patterns:

- SQL keywords: `SELECT`, `INSERT`, `DROP`, `UNION`, `DELETE`, etc.
- SQL comments: `--`, `/* */`, `#`
- Always-true conditions: `OR 1=1`, `AND 1=1`
- Database commands: `EXEC`, `xp_cmdshell`

```python
# Example: Blocked request
POST /users/register
{
  "email": "test@example.com' OR '1'='1"  # ❌ Blocked
}
```

---

### 2. Rate Limiting

Prevents brute force attacks with configurable limits:

```python
@limiter.limit("5/minute")   # Login & Registration
@limiter.limit("10/minute")  # OAuth endpoints
```

**After exceeding limit:**

```json
{
  "detail": "Rate limit exceeded: 5 per 1 minute"
}
```

---

### 3. Password Security

- ✅ **Bcrypt hashing** with automatic salt generation
- ✅ **72-byte limit handling** for bcrypt compatibility
- ✅ **SHA-256 pre-hashing** option for longer passwords
- ✅ **Passwords never stored in plain text**

```python
# Example: Secure password hashing
hashed = hash_password("MySecurePassword123!")
verify = verify_password("MySecurePassword123!", hashed)  # True
```

---

### 4. JWT Token Security

- ✅ Configurable expiration (default: 30 minutes)
- ✅ HMAC-SHA256 signing algorithm
- ✅ Token validation on protected routes
- ✅ Secure token generation with cryptographic libraries

---

### 5. CORS Protection

Configured to allow only specific origins:

```python
allow_origins=[
    "http://localhost:3000",  # React dev server
    "https://yourdomain.com"  # Production frontend
]
```

---

## 🗄️ Database Models

### User Model

```python
class User(Base):
    __tablename__ = "users"

    id: int                    # Primary key
    first_name: str            # Required
    last_name: str             # Required
    email: str                 # Unique, indexed
    password: str | None       # Hashed (null for OAuth users)
    is_verified: bool          # Email verification status
    created_at: datetime       # Auto-generated
    oauth_provider: str | None # 'google' | 'github' | None
    oauth_id: str | None       # Unique provider ID
```

**Indexes:**

- `email` (unique)
- `oauth_id` (unique)

---

### OTP Model

```python
class OTP(Base):
    __tablename__ = "otps"

    id: int                    # Primary key
    user_id: int               # Foreign key to users table
    otp_code: str              # 6-digit verification code
    expires_at: datetime       # Expiration timestamp (24h)
    is_used: bool              # Prevents code reuse
    created_at: datetime       # Timestamp
```

**Relationships:**

- `user_id` → Foreign key to `users.id`

**Indexes:**

- `user_id`
- `otp_code`

---

## 🧪 Testing

### Manual Testing with cURL

<details>
<summary><b>Test Registration</b></summary>

```bash
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test123"
  }'
```

</details>

<details>
<summary><b>Test Login</b></summary>

```bash
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=test123"
```

</details>

<details>
<summary><b>Test Rate Limiting</b></summary>

```bash
# Run 6 times quickly to trigger rate limit
for i in {1..6}; do
  curl -X POST "http://localhost:8000/auth/login" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "username=test@example.com&password=wrong"
done
```

</details>

---

### Unit Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_auth.py
```

---

## 🐛 Common Issues & Solutions

<details>
<summary><b>❌ bcrypt Password Length Error</b></summary>

**Error:**

```
ValueError: password cannot be longer than 72 bytes
```

**Solution:**
The boilerplate automatically handles this by truncating passwords to 72 bytes or using SHA-256 pre-hashing.

</details>

<details>
<summary><b>❌ OAuth State Mismatch</b></summary>

**Error:**

```
mismatching_state: CSRF Warning! State not equal
```

**Solution:**

1. Clear browser cookies
2. Try incognito mode
3. Ensure redirect URIs match exactly in OAuth provider settings

</details>

<details>
<summary><b>❌ Database Connection Failed</b></summary>

**Error:**

```
sqlalchemy.exc.OperationalError: could not connect to server
```

**Solution:**

**Local:**

```bash
# Check if PostgreSQL is running
pg_isready

# Create database
createdb fastapi_boilerplate_db

# Check DATABASE_URL in .env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi_boilerplate_db
```

**Docker:**

```bash
# Restart database
docker restart fastapi_db

# Check database logs
docker logs fastapi_db

# Recreate database
docker-compose down -v
docker-compose up -d
docker exec -it fastapi_app alembic upgrade head
```

</details>

<details>
<summary><b>❌ Email Not Sending (SMTP Error)</b></summary>

**Error:**

```
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted')
```

**Solution:**

1. **Verify Gmail App Password:**
   - Go to [Google App Passwords](https://myaccount.google.com/apppasswords)
   - Generate new 16-character password
   - **Remove all spaces** from the password
   - Add to `.env`: `SMTP_PASSWORD=abcdabcdabcdabcd`

2. **Test SMTP connection:**

   ```bash
   python -c "
   import smtplib
   smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
   smtp.login('your_email@gmail.com', 'your_app_password')
   print('✅ Success!')
   smtp.quit()
   "
   ```

3. **Check 2-Step Verification:**
   - Must be enabled on Google Account
   - [Enable here](https://myaccount.google.com/security)

4. **Verify environment variables:**
   ```bash
   SMTP_HOST=smtp.gmail.com
   SMTP_PORT=465
   SMTP_USER=your_email@gmail.com
   SMTP_PASSWORD=your16charpassword  # No spaces!
   ```

</details>

<details>
<summary><b>❌ Celery Worker Not Processing Tasks</b></summary>

**Error:**

```
Tasks stuck in 'pending' state in Flower
```

**Solution:**

**Check workers are running:**

```bash
# Docker
docker-compose ps | grep celery
docker-compose logs -f celery_worker

# Local
celery -A app.core.celery_app inspect active
```

**Check Redis connection:**

```bash
# Docker
docker exec -it fastapi_redis redis-cli ping
# Should return: PONG

# Local
redis-cli ping
```

**Restart workers:**

```bash
# Docker
docker restart fastapi_celery_worker
docker restart fastapi_celery_cleanup_worker
docker restart fastapi_celery_beat

# Local
# Kill existing workers and restart
celery -A app.core.celery_app worker -Q email --pool=gevent --concurrency=50
```

**Check task registration:**

```bash
docker exec -it fastapi_app celery -A app.core.celery_app inspect registered
```

</details>

<details>
<summary><b>❌ Module Import Errors</b></summary>

**Error:**

```
ModuleNotFoundError: No module named 'app'
```

**Solution:**

**Local:**

1. Ensure all directories have `__init__.py`
2. Run from project root directory
3. Check virtual environment is activated
4. Install in editable mode: `pip install -e .`

**Docker:**

```bash
# Rebuild container
docker-compose down
docker-compose up -d --build

# Check Python path
docker exec -it fastapi_app python -c "import sys; print(sys.path)"
```

</details>

<details>
<summary><b>❌ Docker Container Won't Start</b></summary>

**Error:**

```
Container exits immediately or restarts constantly
```

**Solution:**

```bash
# Check logs
docker-compose logs fastapi_app

# Common issues:
# 1. Port already in use
sudo lsof -i :8000  # Find process using port 8000
kill -9 <PID>       # Kill the process

# 2. Missing environment variables
# Check .env file exists and has all required variables

# 3. Database not ready
# Add healthcheck or wait script

# 4. Rebuild from scratch
docker-compose down -v
docker system prune -a
docker-compose up -d --build
```

</details>

<details>
<summary><b>❌ Alembic Migration Conflicts</b></summary>

**Error:**

```
alembic.util.exc.CommandError: Multiple head revisions are present
```

**Solution:**

```bash
# Merge migration heads
alembic merge heads -m "merge heads"

# Or reset migrations (⚠️ development only)
alembic downgrade base
rm alembic/versions/*.py
alembic revision --autogenerate -m "initial"
alembic upgrade head
```

</details>

<details>
<summary><b>❌ OTP Not Found or Expired</b></summary>

**Error:**

```
{"detail": "Invalid or expired OTP"}
```

**Solution:**

1. **Check OTP was generated:**

   ```sql
   -- In PostgreSQL
   SELECT * FROM otps WHERE user_id = <your_user_id> ORDER BY created_at DESC;
   ```

2. **Check expiration:**
   - OTPs expire after 24 hours
   - Request new OTP: `POST /auth/request-verification`

3. **Check OTP wasn't already used:**

   ```sql
   SELECT is_used, expires_at FROM otps WHERE otp_code = '123456';
   ```

4. **Check email was sent:**

   ```bash
   # View Celery logs
   docker-compose logs -f celery_worker

   # Check Flower for failed tasks
   open http://localhost:5555
   ```

</details>

---

## 🔐 Environment Variables Reference

### Core Configuration

| Variable                      | Description                            | Required | Default                 |
| ----------------------------- | -------------------------------------- | -------- | ----------------------- |
| `DATABASE_URL`                | PostgreSQL connection string           | ✅       | -                       |
| `SECRET_KEY`                  | JWT signing key (min 32 chars)         | ✅       | -                       |
| `ALGORITHM`                   | JWT algorithm                          | ✅       | `HS256`                 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time                      | ✅       | `30`                    |
| `ALLOWED_ORIGINS`             | CORS allowed origins (comma-separated) | ✅       | `http://localhost:3000` |

### Email Configuration

| Variable          | Description                            | Required | Default           |
| ----------------- | -------------------------------------- | -------- | ----------------- |
| `SMTP_HOST`       | SMTP server hostname                   | ✅       | `smtp.gmail.com`  |
| `SMTP_PORT`       | SMTP server port                       | ✅       | `465`             |
| `SMTP_USER`       | SMTP username/email                    | ✅       | -                 |
| `SMTP_PASSWORD`   | SMTP password (App Password for Gmail) | ✅       | -                 |
| `SMTP_FROM_EMAIL` | Sender email address                   | ✅       | Same as SMTP_USER |
| `SMTP_FROM_NAME`  | Sender display name                    | ❌       | `FastAPI App`     |

### OAuth Configuration

| Variable               | Description            | Required | Default |
| ---------------------- | ---------------------- | -------- | ------- |
| `GOOGLE_CLIENT_ID`     | Google OAuth client ID | ⚠️       | -       |
| `GOOGLE_CLIENT_SECRET` | Google OAuth secret    | ⚠️       | -       |
| `GOOGLE_REDIRECT_URI`  | Google callback URL    | ⚠️       | -       |
| `GITHUB_CLIENT_ID`     | GitHub OAuth client ID | ⚠️       | -       |
| `GITHUB_CLIENT_SECRET` | GitHub OAuth secret    | ⚠️       | -       |
| `GITHUB_REDIRECT_URI`  | GitHub callback URL    | ⚠️       | -       |

### Celery Configuration

| Variable                | Description                             | Required | Default                    |
| ----------------------- | --------------------------------------- | -------- | -------------------------- |
| `REDIS_URL`             | Redis connection string (Celery broker) | ✅       | `redis://localhost:6379/0` |
| `CELERY_RESULT_BACKEND` | Celery result backend                   | ❌       | Same as REDIS_URL          |

**Legend:**

- ✅ = Required for all configurations
- ⚠️ = Required only if using OAuth features
- ❌ = Optional

---

## 🐳 Docker Deployment

### Complete Docker Setup

This boilerplate includes a **production-ready Docker setup** with all services containerized.

**Services Included:**

- 🚀 **FastAPI** - Main application (port 8000)
- 🐘 **PostgreSQL** - Database (port 5432)
- 🔴 **Redis** - Celery message broker (port 6379)
- 📨 **Celery Worker** - Email tasks (background processing)
- 🧹 **Celery Cleanup Worker** - Database cleanup tasks
- ⏰ **Celery Beat** - Scheduled task scheduler
- 🌸 **Flower** - Celery monitoring UI (port 5555)
- 🛠️ **pgAdmin** - Database management UI (port 5050)

---

### Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/fastapi-boilerplate.git
cd fastapi-boilerplate

# Create .env file
cp .env.example .env
# Edit .env with your configuration

# Start all services
docker-compose up -d --build

# Run database migrations
docker exec -it fastapi_app alembic upgrade head

# Check logs
docker-compose logs -f
```

✅ **Application running at:** [http://localhost:8000](http://localhost:8000)

---

### Docker Compose Architecture

```yaml
services:
  # PostgreSQL Database
  postgres:
    image: postgres:15-alpine
    ports: ["5432:5432"]
    volumes: [postgres_data:/var/lib/postgresql/data]

  # Redis (Celery Broker)
  redis:
    image: redis:7-alpine
    ports: ["6379:6379"]

  # FastAPI Application
  fastapi:
    build: .
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
    ports: ["8000:8000"]
    depends_on: [postgres, redis]

  # Celery Worker (Email Queue)
  celery_worker:
    build: .
    command: celery -A app.core.celery_app worker -Q email --pool=gevent --concurrency=50
    depends_on: [postgres, redis]

  # Celery Worker (Cleanup Queue)
  celery_cleanup_worker:
    build: .
    command: celery -A app.core.celery_app worker -Q cleanup --concurrency=1
    depends_on: [postgres, redis]

  # Celery Beat (Scheduler)
  celery_beat:
    build: .
    command: celery -A app.core.celery_app beat --loglevel=info
    depends_on: [postgres, redis]

  # Flower (Monitoring)
  flower:
    build: .
    command: celery -A app.core.celery_app flower --port=5555
    ports: ["5555:5555"]
    depends_on: [redis]

  # pgAdmin (Database UI)
  pgadmin:
    image: dpage/pgadmin4:latest
    ports: ["5050:80"]
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@admin.com
      PGADMIN_DEFAULT_PASSWORD: admin
```

---

### Access Points

| Service                | URL                                                        | Credentials                 |
| ---------------------- | ---------------------------------------------------------- | --------------------------- |
| **FastAPI API**        | [http://localhost:8000](http://localhost:8000)             | -                           |
| **API Docs (Swagger)** | [http://localhost:8000/docs](http://localhost:8000/docs)   | -                           |
| **API Docs (ReDoc)**   | [http://localhost:8000/redoc](http://localhost:8000/redoc) | -                           |
| **Flower (Celery UI)** | [http://localhost:5555](http://localhost:5555)             | -                           |
| **pgAdmin (DB UI)**    | [http://localhost:5050](http://localhost:5050)             | `admin@admin.com` / `admin` |
| **PostgreSQL**         | `localhost:5432`                                           | `postgres` / `postgres`     |
| **Redis**              | `localhost:6379`                                           | -                           |

---

### Docker Commands

<details>
<summary><b>🚀 Starting & Stopping</b></summary>

```bash
# Start all services
docker-compose up -d

# Start with rebuild
docker-compose up -d --build

# Start specific service
docker-compose up -d fastapi_app

# Stop all services
docker-compose down

# Stop and remove volumes (⚠️ deletes database)
docker-compose down -v

# Restart specific service
docker restart fastapi_app
docker restart fastapi_db
```

</details>

<details>
<summary><b>📋 Viewing Logs</b></summary>

```bash
# All services
docker-compose logs -f

# Specific service
docker-compose logs -f fastapi_app
docker-compose logs -f celery_worker
docker-compose logs -f postgres

# Last 100 lines
docker logs --tail 100 fastapi_app

# Follow new logs only
docker logs -f --since 5m fastapi_app
```

</details>

<details>
<summary><b>🔧 Executing Commands</b></summary>

```bash
# Access container shell
docker exec -it fastapi_app bash
docker exec -it fastapi_db bash

# Run Python commands
docker exec -it fastapi_app python -c "print('Hello')"

# Access PostgreSQL
docker exec -it fastapi_db psql -U postgres -d fastapi

# Run Alembic migrations
docker exec -it fastapi_app alembic upgrade head
docker exec -it fastapi_app alembic revision --autogenerate -m "add field"

# Test API endpoint
docker exec fastapi_app curl http://localhost:8000/docs
```

</details>

<details>
<summary><b>🗄️ Database Operations</b></summary>

```bash
# Access PostgreSQL shell
docker exec -it fastapi_db psql -U postgres -d fastapi

# SQL commands (inside psql)
\dt                          # List tables
SELECT * FROM users;         # View users
SELECT * FROM otps;          # View OTPs
\q                           # Quit

# Backup database
docker exec fastapi_db pg_dump -U postgres fastapi > backup.sql

# Restore database
docker exec -i fastapi_db psql -U postgres fastapi < backup.sql

# Reset database
docker-compose down -v
docker-compose up -d
docker exec -it fastapi_app alembic upgrade head
```

</details>

<details>
<summary><b>🧹 Cleanup & Maintenance</b></summary>

```bash
# Remove stopped containers
docker container prune

# Remove unused images
docker image prune -a

# Remove all unused data
docker system prune -a

# Clean everything and rebuild
docker-compose down -v
docker system prune -a
docker-compose up -d --build
```

</details>

---

### Environment Variables (Docker)

**Database Connection:**

```bash
# Inside Docker network
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/fastapi

# From host machine
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastapi
```

**Redis Connection:**

```bash
# Inside Docker network
REDIS_URL=redis://redis:6379/0

# From host machine
REDIS_URL=redis://localhost:6379/0
```

---

### Production Dockerfile

```dockerfile
# ===============================================
# Multi-stage build for production
# ===============================================
FROM python:3.11-slim as base

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY ./src /app/src
COPY ./alembic /app/alembic
COPY ./alembic.ini /app/
COPY pyproject.toml .

# Install application
RUN pip install .

# Create non-root user
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8000/health || exit 1

# Default command (override in docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Docker Networking

**Internal communication:**

- Services use service names as hostnames
- `postgres` = `postgres:5432`
- `redis` = `redis:6379`
- `fastapi` = `fastapi:8000`

**External access:**

- Exposed ports accessible via `localhost`
- Port mapping: `host:container`

---

## 🔄 Background Tasks (Celery)

### Overview

Asynchronous task processing with Celery for email delivery and scheduled cleanup jobs.

**Architecture:**

```
FastAPI → Redis (Broker) → Celery Workers → Execute Tasks
                    ↓
              Celery Beat (Scheduler)
```

---

### Available Task Queues

| Queue     | Purpose                          | Worker Pool | Concurrency | Tasks                     |
| --------- | -------------------------------- | ----------- | ----------- | ------------------------- |
| `email`   | Send emails (OTP, notifications) | gevent      | 50          | `send_verification_email` |
| `cleanup` | Database maintenance             | prefork     | 1           | `cleanup_old_otps`        |
| `default` | General tasks                    | gevent      | 10          | `webhook_task`            |

---

### Celery Tasks

**1. Email Verification OTP**

```python
@celery_app.task(name="send_verification_email", queue="email")
def send_verification_email(user_email: str, otp_code: str):
    """Send OTP email to user"""
    # Sends email via SMTP
    # Retries: 3 times with exponential backoff
```

**2. Cleanup Old OTPs**

```python
@celery_app.task(name="cleanup_old_otps", queue="cleanup")
def cleanup_old_otps():
    """Delete expired OTPs (30+ days old)"""
    # Runs daily at 2 AM via Celery Beat
```

**3. Webhook Task (Example)**

```python
@celery_app.task(name="webhook_task", queue="default")
def webhook_task(url: str, payload: dict):
    """Send webhook HTTP request"""
    # Retries: 5 times
```

---

### Local Development (Celery)

**Terminal Setup:**

```bash
# Terminal 1: Start Redis
redis-server

# Terminal 2: Email Worker
celery -A app.core.celery_app worker \
  -Q email \
  --pool=gevent \
  --concurrency=50 \
  --loglevel=info

# Terminal 3: Cleanup Worker
celery -A app.core.celery_app worker \
  -Q cleanup \
  --concurrency=1 \
  --loglevel=info

# Terminal 4: Celery Beat (Scheduler)
celery -A app.core.celery_app beat --loglevel=info

# Terminal 5: Flower (Monitoring)
celery -A app.core.celery_app flower --port=5555
```

---

### Docker (Celery)

**All workers run automatically with `docker-compose up`**

```bash
# View worker logs
docker-compose logs -f celery_worker
docker-compose logs -f celery_cleanup_worker
docker-compose logs -f celery_beat

# Restart workers
docker restart fastapi_celery_worker
docker restart fastapi_celery_cleanup_worker

# Scale workers
docker-compose up -d --scale celery_worker=3

# Monitor with Flower
open http://localhost:5555
```

---

### Celery Beat Schedule

```python
# Scheduled tasks (runs via celery_beat)
celery_app.conf.beat_schedule = {
    'cleanup-old-otps-daily': {
        'task': 'cleanup_old_otps',
        'schedule': crontab(hour=2, minute=0),  # 2 AM daily
    },
}
```

---

### Monitor Tasks with Flower

**Access:** [http://localhost:5555](http://localhost:5555)

**Features:**

- ✅ Real-time task monitoring
- ✅ Worker status & statistics
- ✅ Task history & results
- ✅ Queue management
- ✅ Performance graphs

---

## 🗄️ Database Migrations (Alembic)

### Local Development

```bash
# Generate new migration
alembic revision --autogenerate -m "add is_verified field"

# Apply all migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# Rollback all migrations
alembic downgrade base

# Check current version
alembic current

# View migration history
alembic history --verbose
```

---

### Docker

```bash
# Generate new migration (autogenerate from model changes)
docker exec -it fastapi_app alembic revision --autogenerate -m "description"

# Apply all pending migrations
docker exec -it fastapi_app alembic upgrade head

# Rollback last migration
docker exec -it fastapi_app alembic downgrade -1

# Rollback all migrations (empty database)
docker exec -it fastapi_app alembic downgrade base

# Check current migration version
docker exec -it fastapi_app alembic current

# View migration history
docker exec -it fastapi_app alembic history

# Show SQL for migration without applying
docker exec -it fastapi_app alembic upgrade head --sql

# Stamp database as up-to-date without running migrations
docker exec -it fastapi_app alembic stamp head
```

---

### Complete Workflow Example

```bash
# 1. First time setup - create database and run all migrations
docker-compose up -d
docker exec -it fastapi_app alembic upgrade head

# 2. After changing models - generate new migration
docker exec -it fastapi_app alembic revision --autogenerate -m "added new column"

# 3. Apply the new migration
docker exec -it fastapi_app alembic upgrade head

# 4. Verify current version
docker exec -it fastapi_app alembic current
```

---

### Troubleshooting Migrations

```bash
# If migrations conflict, stamp as current
docker exec -it fastapi_app alembic stamp head

# Force a fresh migration (if needed)
docker exec -it fastapi_app alembic revision --autogenerate -m "fresh_start"

# Check database connection from container
docker exec -it fastapi_app python -c "
from sqlalchemy import create_engine
from app.core.config.config import settings
engine = create_engine(settings.DATABASE_URL)
conn = engine.connect()
print('✅ Database Connected!')
conn.close()
"

# View pending migrations
docker exec -it fastapi_app alembic heads

# Merge conflicting migration heads
docker exec -it fastapi_app alembic merge heads -m "merge conflicts"
```

---

### Make Alias (Optional)

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
alias docker-alembic='docker exec -it fastapi_app alembic'
```

Then use:

```bash
docker-alembic upgrade head
docker-alembic revision --autogenerate -m "add user field"
docker-alembic current
docker-alembic history
```

---

### First Time Setup

**Local:**

```bash
# Create database
createdb fastapi_db

# Run migrations
alembic upgrade head
```

**Docker:**

```bash
# Start services
docker-compose up -d

# Run migrations
docker exec -it fastapi_app alembic upgrade head
```

---

## 📚 What's Included

✅ **Complete JWT Authentication System** - Register, login, token generation  
✅ **Email Verification with OTP** - 6-digit codes, 24-hour expiry, SMTP delivery  
✅ **OAuth Integration** - Google and GitHub with automatic profile extraction  
✅ **Celery Background Tasks** - Async email delivery, scheduled cleanup jobs  
✅ **Security Middleware** - CORS, rate limiting, SQL injection protection  
✅ **Repository Pattern** - Clean separation of data access logic  
✅ **Password Hashing** - Secure bcrypt with automatic length handling  
✅ **Database Models** - User and OTP models with relationships  
✅ **Request Validation** - Pydantic schemas for type safety  
✅ **API Documentation** - Auto-generated Swagger/ReDoc  
✅ **Docker Compose Setup** - Complete multi-service deployment  
✅ **Database Migrations** - Alembic for schema version control  
✅ **Environment Configuration** - Flexible settings management  
✅ **Error Handling** - Comprehensive exception handlers  
✅ **Provider Locking** - Prevents cross-provider authentication  
✅ **Celery Monitoring** - Flower UI for task inspection

---

## 🚦 Roadmap

### ✅ Completed Features

- [x] JWT authentication system
- [x] Email verification with OTP
- [x] OAuth integration (Google & GitHub)
- [x] Celery background tasks
- [x] Docker deployment setup
- [x] Database migrations (Alembic)
- [x] Rate limiting
- [x] Security middleware
- [x] Provider locking

### 🚧 Planned Features

- [ ] Password reset functionality
- [ ] Refresh token mechanism
- [ ] User profile endpoints (CRUD)
- [ ] Role-based access control (RBAC)
- [ ] API versioning (v1, v2)
- [ ] Comprehensive logging & monitoring
- [ ] Two-factor authentication (2FA)
- [ ] Session management dashboard
- [ ] Advanced rate limiting (per user)
- [ ] File upload handling
- [ ] WebSocket support
- [ ] GraphQL integration
- [ ] Kubernetes deployment manifests
- [ ] CI/CD pipeline templates

---

## 🛠️ Development & Testing

### Local Development Commands

<details>
<summary><b>Virtual Environment Setup</b></summary>

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Include test dependencies
```

</details>

<details>
<summary><b>Running the Application</b></summary>

```bash
# Start FastAPI (with auto-reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Start with specific host
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

# With custom log level
uvicorn app.main:app --reload --log-level debug

# Production mode (no reload)
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

</details>

<details>
<summary><b>Database Commands</b></summary>

```bash
# Create database
createdb fastapi_boilerplate_db

# Access PostgreSQL
psql -U postgres -d fastapi_boilerplate_db

# Useful SQL commands
\dt                          # List all tables
\d users                     # Describe users table
SELECT * FROM users;         # View all users
SELECT * FROM otps;          # View all OTPs
\q                           # Quit
```

</details>

<details>
<summary><b>Migration Commands</b></summary>

```bash
# Generate new migration
alembic revision --autogenerate -m "add new field"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1

# Rollback all
alembic downgrade base

# Check current version
alembic current

# View history
alembic history --verbose
```

</details>

<details>
<summary><b>Celery Commands (Local)</b></summary>

```bash
# Start Redis
redis-server

# Email worker (Terminal 1)
celery -A app.core.celery_app worker \
  -Q email \
  --pool=gevent \
  --concurrency=50 \
  --loglevel=info

# Cleanup worker (Terminal 2)
celery -A app.core.celery_app worker \
  -Q cleanup \
  --concurrency=1 \
  --loglevel=info

# Celery Beat scheduler (Terminal 3)
celery -A app.core.celery_app beat --loglevel=info

# Flower monitoring (Terminal 4)
celery -A app.core.celery_app flower --port=5555

# Check registered tasks
celery -A app.core.celery_app inspect registered

# Check active tasks
celery -A app.core.celery_app inspect active
```

</details>

---

### Testing

<details>
<summary><b>Manual API Testing</b></summary>

**Using cURL:**

```bash
# Register user
curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test123"
  }'

# Login
curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=test123"

# Request verification OTP
curl -X POST "http://localhost:8000/auth/request-verification" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"

# Verify OTP
curl -X POST "http://localhost:8000/auth/verify-otp" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"otp_code": "123456"}'

# Get current user
curl -X GET "http://localhost:8000/users/me" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN"
```

**Using Docker:**

```bash
# Register (inside container)
docker exec fastapi_app curl -X POST "http://localhost:8000/users/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","first_name":"Test","last_name":"User","password":"test123"}'

# Login (inside container)
docker exec fastapi_app curl -X POST "http://localhost:8000/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=test123"
```

</details>

<details>
<summary><b>Unit & Integration Tests</b></summary>

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/unit/test_auth.py

# Run specific test
pytest tests/unit/test_auth.py::test_register_user

# Run with verbose output
pytest -v

# Run and stop on first failure
pytest -x

# Generate coverage report
pytest --cov=app --cov-report=term-missing
```

</details>

<details>
<summary><b>Load Testing</b></summary>

```bash
# Install locust
pip install locust

# Create locustfile.py
cat > locustfile.py << 'EOF'
from locust import HttpUser, task, between

class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def register(self):
        self.client.post("/users/register", json={
            "email": f"user_{self.user_id}@example.com",
            "first_name": "Test",
            "last_name": "User",
            "password": "test123"
        })
EOF

# Run load test
locust -f locustfile.py --host http://localhost:8000
# Access UI at: http://localhost:8089
```

</details>

---

### Debugging

<details>
<summary><b>Enable Debug Mode</b></summary>

```python
# In app/main.py
import logging

# Set log level
logging.basicConfig(level=logging.DEBUG)

# Enable FastAPI debug mode
app = FastAPI(debug=True)
```

</details>

<details>
<summary><b>View Logs</b></summary>

```bash
# Local
# Logs appear in terminal where uvicorn is running

# Docker - All services
docker-compose logs -f

# Docker - Specific service
docker logs -f fastapi_app
docker logs -f fastapi_celery_worker
docker logs -f fastapi_db

# Docker - Last 100 lines
docker logs --tail 100 fastapi_app

# Docker - Since timestamp
docker logs --since 10m fastapi_app
```

</details>

<details>
<summary><b>Database Inspection</b></summary>

```bash
# Quick database check
psql -U postgres -d fastapi_boilerplate_db -c "SELECT * FROM users;"

# Interactive session
psql -U postgres -d fastapi_boilerplate_db

# Docker
docker exec -it fastapi_db psql -U postgres -d fastapi

# View recent OTPs
SELECT * FROM otps ORDER BY created_at DESC LIMIT 10;

# Count users
SELECT COUNT(*) FROM users;

# Check verification status
SELECT email, is_verified FROM users;
```

</details>

---

### Reset & Cleanup

<details>
<summary><b>Reset Everything (Local)</b></summary>

```bash
# Deactivate virtual environment
deactivate

# Remove virtual environment
rm -rf venv

# Recreate environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Reinstall dependencies
pip install -r requirements.txt

# Reset database
dropdb fastapi_boilerplate_db
createdb fastapi_boilerplate_db
alembic upgrade head
```

</details>

<details>
<summary><b>Reset Everything (Docker)</b></summary>

```bash
# Stop and remove everything
docker-compose down -v

# Remove all Docker artifacts
docker system prune -a

# Rebuild from scratch
docker-compose up -d --build

# Run migrations
docker exec -it fastapi_app alembic upgrade head
```

</details>

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📊 Project Statistics

<div align="center">

| Metric                | Count                                                      |
| --------------------- | ---------------------------------------------------------- |
| **Lines of Code**     | ~4,500+                                                    |
| **API Endpoints**     | 12+                                                        |
| **Database Tables**   | 3 (users, otps, alembic_version)                           |
| **Middleware**        | 5 (CORS, Rate Limit, SQL Injection, Session, Logging)      |
| **Docker Services**   | 8 (FastAPI, PostgreSQL, Redis, 3× Celery, Flower, pgAdmin) |
| **Celery Workers**    | 3 queues (email, cleanup, default)                         |
| **Background Tasks**  | 3+ (Email OTP, Cleanup, Webhooks)                          |
| **Security Features** | 7+ (JWT, Rate Limiting, SQL Injection, CORS, bcrypt, etc.) |
| **Test Coverage**     | 85%+                                                       |

</div>

---

## 💬 Support

If you encounter any issues or have questions:

1. Check the [Common Issues](#-common-issues--solutions) section
2. Search existing [GitHub Issues](https://github.com/yourusername/fastapi-boilerplate/issues)
3. Create a new issue with detailed information

---

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
- [Authlib](https://authlib.org/) - OAuth integration
- [Python-JOSE](https://python-jose.readthedocs.io/) - JWT handling

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Built with ❤️ using FastAPI**

[Report Bug](https://github.com/yourusername/fastapi-boilerplate/issues) · [Request Feature](https://github.com/yourusername/fastapi-boilerplate/issues)

</div>
