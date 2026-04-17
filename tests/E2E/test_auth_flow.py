import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestAuthFlow:

    def test_full_auth_flow(self):
        # 1. Create organization
        org_response = client.post(
            "/organizations/create",
            json={"name": "Test E2E Org"}
        )
        assert org_response.status_code == 200
        org_data = org_response.json()
        invite_token = org_data["invite_token"]

        # 2. Register user
        register_response = client.post(
            "/users/register",
            json={
                "email": "e2e@test.com",
                "first_name": "E2E",
                "last_name": "Test",
                "password": "test123",
                "invite_token": invite_token
            }
        )
        assert register_response.status_code == 200
        token = register_response.json()["access_token"]

        # 3. Login
        login_response = client.post(
            "/auth/login",
            data={
                "username": "e2e@test.com",
                "password": "test123",
                "organization_id": org_data["id"]
            }
        )
        assert login_response.status_code == 200

        # 4. Get current user
        me_response = client.get(
            "/users/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert me_response.status_code == 200
        assert me_response.json()["email"] == "e2e@test.com"

        # 5. Logout
        logout_response = client.post(
            "/users/logout",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert logout_response.status_code == 200
