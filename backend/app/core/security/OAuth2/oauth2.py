from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.modules.Auth.schema import schema
from app.core.config.config import settings
from app.core.dependencies.dependencies import get_db
from app.modules.Users.models import model

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_TIME = settings.access_token_expire_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='users/login')


def create_access_token(data: dict):
    """Create access token with organization_id"""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + \
        timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded


def verify_token(token: str, token_exception):
    """Verify token and return token data"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        org_id = payload.get("org_id")

        if user_id is None:
            raise token_exception

        token_data = schema.TokenData(id=user_id, organization_id=org_id)
    except JWTError:
        raise token_exception
    return token_data


def current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get current user with organization context"""
    token_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="User is not authorized",
        headers={"WWW-Authenticate": "Bearer"}
    )

    token_meta = verify_token(token, token_exception)

    user = db.query(model.User).filter(model.User.id == token_meta.id).first()

    if not user:
        raise token_exception

    return user
