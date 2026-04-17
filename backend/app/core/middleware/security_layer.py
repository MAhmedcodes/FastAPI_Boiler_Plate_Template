from fastapi import FastAPI, Request, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
# creates a limit, error response
from slowapi import Limiter, _rate_limit_exceeded_handler
# get user ip for limitng a specific user
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded  # exception when limit is hit
# base class to create custom middleware
from starlette.middleware.base import BaseHTTPMiddleware
import re  # python regix module to detect sql injection patterns

# Rate limiter setup
limiter = Limiter(key_func=get_remote_address)


def setup_security(app: FastAPI):
    """Setup all security middlewares"""

    # 1. CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        # Update with your frontend URLs
        allow_origins=["http://localhost:3000", "any other url we need"],
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
        allow_headers=["*"],
        expose_headers=["*"],
        max_age=3600,  # Browser caches CORS preflight response for 1 hour
    )

    # 2. Rate Limiting
    app.state.limiter = limiter
    app.add_exception_handler(
        RateLimitExceeded, _rate_limit_exceeded_handler)  # type: ignore

    # 3. SQL Injection Protection Middleware
    app.add_middleware(SQLInjectionProtectionMiddleware)

    return app


class SQLInjectionProtectionMiddleware(BaseHTTPMiddleware):
    """Protect against SQL injection attacks"""

    # Common SQL injection patterns
    SQL_PATTERNS = [
        r"(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER|CREATE|TRUNCATE)\b)",
        r"(--)",
        r"(;.*--)",
        r"(\bOR\b.*=.*)",
        r"(\bAND\b.*=.*)",
        r"('.*\bor\b.*'.*=)",
        r"(/\*.*\*/)",
        r"(\bEXEC\b.*\()",
        r"(\bXP_\w+\b)",
    ]

    async def dispatch(self, request: Request, call_next):
        # Skip SQL injection check for OAuth callbacks (they have encoded tokens)
        if "/callback" in request.url.path:
            return await call_next(request)

        # Skip for GET requests with query params (OAuth uses GET with query params)
        if request.method == "GET" and len(request.query_params) > 0:
            # Check if it looks like an OAuth callback (has 'code' parameter)
            if 'code' in request.query_params:
                return await call_next(request)

        # Check query parameters
        for param_name, param_value in request.query_params.items():
            if self.is_suspicious(str(param_value)):
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail="Invalid request parameters")

        # Check request body if it's JSON
        if request.method in ["POST", "PUT", "PATCH"]:
            try:
                body = await request.json()
                if self.check_dict_for_sql_patterns(body):
                    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                        detail="Invalid request data")
            except:
                pass  # Not JSON, continue

        response = await call_next(request)
        return response

    def is_suspicious(self, value: str) -> bool:
        """Check if string contains SQL injection patterns"""
        if not isinstance(value, str):
            return False

        value_upper = value.upper()
        for pattern in self.SQL_PATTERNS:
            if re.search(pattern, value_upper, re.IGNORECASE):
                return True
        return False

    def check_dict_for_sql_patterns(self, data) -> bool:
        """Recursively check dictionary for SQL patterns"""
        if isinstance(data, dict):
            for key, value in data.items():
                if self.check_dict_for_sql_patterns(value):
                    return True
        elif isinstance(data, list):
            for item in data:
                if self.check_dict_for_sql_patterns(item):
                    return True
        elif isinstance(data, str):
            if self.is_suspicious(data):
                return True
        return False
