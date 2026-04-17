from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

# base schema of users


class UserBase(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str

# using to create the user


class UserCreate(UserBase):
    password: Optional[str] = None
    invite_token: str

# showing the Current User


class CurrentUser(UserBase):
    id: int
    organization_id: int


# User Response Class


class UserOut(UserBase):
    id: int
    organization_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Login Schema


class Login(BaseModel):
    email: EmailStr
    password: str
    organization_id: int

# Registration Response Schema


class RegisterResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    email: str
    first_name: str
    last_name: str
    organization_id: int
    message: str

    class Config:
        from_attributes = True
