from app.core.security.OAuth2 import oauth2
from fastapi import HTTPException


class TestJWT:

    def test_create_access_token(self):
        token = oauth2.create_access_token({"id": 1, "org_id": 1})
        assert isinstance(token, str)
        assert token is not None

    def test_verify_valid_token(self):
        token = oauth2.create_access_token({"id": 1, "org_id": 1})

        exception = HTTPException(status_code=401, detail="Invalid token")

        user = oauth2.verify_token(token, exception)

        assert user.id == 1
        assert user.organization_id == 1
