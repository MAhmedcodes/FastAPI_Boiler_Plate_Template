from pydantic import BaseModel
from typing import Optional

# JWT Token Schema


class Token(BaseModel):
    access_token: str
    token_type: str
    organization_id: Optional[int] = None


class TokenData(BaseModel):
    id: Optional[int] = None
    organization_id: Optional[int] = None


class OAuthResponse(Token):
    user_id: int
    email: str
    message: str

    class config:
        from_attributes = True
