from fastapi import FastAPI, Request

from app.core.config.config import settings
from app.modules.Auth.router import oauth, oauth2
from app.modules.Users.router import user
from app.core.middleware.security_layer import setup_security, limiter
from slowapi.middleware import SlowAPIMiddleware
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI(
    title="FastApI Boiler Plate Code",
    description="A ready to go boiler plate code including auth, jobs and services",
    version="1.0.0") 

#setting up the security layer (CORS, Rate Limiting, SQL Injection Protection)
setup_security(app)

# REQUIRED for OAuth (Authlib)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.secret_key
)

# Add rate limiting middleware
app.add_middleware(SlowAPIMiddleware)

#routers
app.include_router(oauth.router)
app.include_router(oauth2.router)
app.include_router(user.router) 

@app.get("/")
@limiter.limit("5/minute")  # Rate limit for root endpoint
async def root(request: Request):
    return {"Message" : "Welcome To fastapi"}
