import pytest
from app.core.security.OAuth2 import oauth2
from app.core.config.config import settings


class TestJWT:

    def test_create_access_token(self):
        data = {"id": 1, "org_id": 1}
        token = oauth2.create_access_token(data)
        assert token is not None
        assert isinstance(token, str)

    def test_verify_valid_token(self):
        data = {"id": 1, "org_id": 1}
        token = oauth2.create_access_token(data)

        from fastapi import HTTPException
        exception = HTTPException(status_code=401, detail="Invalid token")

        result = oauth2.verify_token(token, exception)
        assert result.id == 1
        assert result.organization_id == 1
