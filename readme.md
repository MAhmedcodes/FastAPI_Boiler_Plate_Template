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
- Token refresh mechanism
- Email verification (optional)

</td>
<td width="50%">

### 🌐 OAuth Integration

- Google OAuth2 login
- GitHub OAuth2 login
- Automatic profile data extraction
- OAuth state management
- CSRF protection
- Provider-specific adapters

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

</td>
<td width="50%">

### 🏗️ Architecture

- Modular structure
- Repository pattern
- Service layer separation
- Dependency injection
- Environment-based config
- Database migrations (Alembic)

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

| **Category**       | **Technology**     | **Purpose**                       |
| ------------------ | ------------------ | --------------------------------- |
| **Framework**      | FastAPI 0.104+     | High-performance async API        |
| **ORM**            | SQLAlchemy 2.0     | Database abstraction              |
| **Database**       | PostgreSQL 13+     | Relational data storage           |
| **Authentication** | Python-JOSE, PyJWT | JWT token generation & validation |
| **OAuth**          | Authlib 1.2+       | Google & GitHub OAuth integration |
| **Password Hash**  | Passlib + bcrypt   | Secure password hashing           |
| **Rate Limiting**  | SlowAPI            | Request throttling                |
| **Validation**     | Pydantic 2.0       | Request/response validation       |
| **Server**         | Uvicorn            | ASGI server                       |
| **Migrations**     | Alembic            | Database version control          |

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

| Method | Endpoint                | Description            | Rate Limit | Auth Required |
| ------ | ----------------------- | ---------------------- | ---------- | ------------- |
| `POST` | `/auth/login`           | Login with credentials | 5/minute   | ❌            |
| `GET`  | `/auth/google/login`    | Google OAuth redirect  | 10/minute  | ❌            |
| `GET`  | `/auth/google/callback` | Google OAuth callback  | 10/minute  | ❌            |
| `GET`  | `/auth/github/login`    | GitHub OAuth redirect  | 10/minute  | ❌            |
| `GET`  | `/auth/github/callback` | GitHub OAuth callback  | 10/minute  | ❌            |

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
  "message": "User registered successfully"
}
```

</details>

---

### 2️⃣ Login

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

### 3️⃣ Google OAuth Flow

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

### 4️⃣ Access Protected Route

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
    created_at: datetime       # Auto-generated
    oauth_provider: str | None # 'google' | 'github' | None
    oauth_id: str | None       # Unique provider ID
```

**Indexes:**

- `email` (unique)
- `oauth_id` (unique)

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

1. Verify PostgreSQL is running: `pg_isready`
2. Check `DATABASE_URL` in `.env`
3. Ensure database exists: `createdb fastapi_boilerplate_db`

</details>

<details>
<summary><b>❌ Module Import Errors</b></summary>

**Error:**

```
ModuleNotFoundError: No module named 'app'
```

**Solution:**

1. Ensure all directories have `__init__.py`
2. Run from project root directory
3. Check virtual environment is activated

</details>

---

## 🔐 Environment Variables Reference

| Variable                      | Description                            | Required | Default                 |
| ----------------------------- | -------------------------------------- | -------- | ----------------------- |
| `DATABASE_URL`                | PostgreSQL connection string           | ✅       | -                       |
| `SECRET_KEY`                  | JWT signing key (min 32 chars)         | ✅       | -                       |
| `ALGORITHM`                   | JWT algorithm                          | ✅       | `HS256`                 |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Token expiry time                      | ✅       | `30`                    |
| `GOOGLE_CLIENT_ID`            | Google OAuth client ID                 | ⚠️       | -                       |
| `GOOGLE_CLIENT_SECRET`        | Google OAuth secret                    | ⚠️       | -                       |
| `GOOGLE_REDIRECT_URI`         | Google callback URL                    | ⚠️       | -                       |
| `GITHUB_CLIENT_ID`            | GitHub OAuth client ID                 | ⚠️       | -                       |
| `GITHUB_CLIENT_SECRET`        | GitHub OAuth secret                    | ⚠️       | -                       |
| `GITHUB_REDIRECT_URI`         | GitHub callback URL                    | ⚠️       | -                       |
| `ALLOWED_ORIGINS`             | CORS allowed origins (comma-separated) | ✅       | `http://localhost:3000` |

⚠️ = Required only if using OAuth features

---

## 🐳 Docker Deployment

### Using Docker Compose

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# Stop services
docker-compose down
```

### Manual Docker Build

```bash
# Build image
docker build -t fastapi-boilerplate .

# Run container
docker run -p 8000:8000 --env-file .env fastapi-boilerplate
```

---

## 📚 What's Included

✅ **Complete JWT Authentication System** - Register, login, token generation  
✅ **OAuth Integration** - Google and GitHub with automatic profile extraction  
✅ **Security Middleware** - CORS, rate limiting, SQL injection protection  
✅ **Repository Pattern** - Clean separation of data access logic  
✅ **Password Hashing** - Secure bcrypt with automatic length handling  
✅ **Database Models** - User model with OAuth support  
✅ **Request Validation** - Pydantic schemas for type safety  
✅ **API Documentation** - Auto-generated Swagger/ReDoc  
✅ **Environment Configuration** - Flexible settings management  
✅ **Error Handling** - Comprehensive exception handlers

---

## 🚦 Roadmap

### Planned Features

- [ ] Email verification system
- [ ] Password reset functionality
- [ ] Refresh token mechanism
- [ ] User profile endpoints (CRUD)
- [ ] Role-based access control (RBAC)
- [ ] API versioning (v1, v2)
- [ ] Comprehensive logging & monitoring
- [ ] Two-factor authentication (2FA)
- [ ] Session management
- [ ] Rate limiting per user
- [ ] File upload handling
- [ ] Background tasks (Celery)
- [ ] WebSocket support
- [ ] GraphQL integration
- [ ] Microservices architecture

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
