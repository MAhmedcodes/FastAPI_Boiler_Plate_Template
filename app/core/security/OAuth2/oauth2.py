from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.modules.Auth.schema import schema
from app.core.config.config import settings
from app.core.dependencies.dependencies import get_db
from app.modules.Auth.repository.auth_repository import AuthRepository

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_TIME = settings.access_token_expire_minutes

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='users/login')

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=(ACCESS_TOKEN_EXPIRE_TIME))
    to_encode.update({"exp": expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

def verify_token(token: str, tokenexcpetion):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        verify_id = payload.get("id")
        if verify_id == None:
            raise tokenexcpetion
        token_data = schema.TokenData(id=verify_id)
    except JWTError:
        raise tokenexcpetion
    return token_data

def current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    tokenexcpetion = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                   detail="User is not authorized", headers=({"WWW-Authenticate": "Bearer"}))
    token_meta = verify_token(token, tokenexcpetion)
    if token_meta.id is None:
        raise tokenexcpetion
    auth_repo = AuthRepository(db)
    user = auth_repo.get_user_by_id(int(token_meta.id))
    return user
