import uuid


class TestAuthFlow:

    def test_full_auth_flow(self, client):
        email = f"{uuid.uuid4()}@test.com"

        org_res = client.post(
            "/organizations/create",
            json={"name": f"Org-{uuid.uuid4()}"}
        )
        assert org_res.status_code == 200
        org = org_res.json()

        reg_res = client.post("/users/register", json={
            "email": email,
            "first_name": "E2E",
            "last_name": "User",
            "password": "test123",
            "invite_token": org["invite_token"]
        })
        assert reg_res.status_code == 200
        token = reg_res.json()["access_token"]

        login_res = client.post("/auth/login", data={
            "username": email,
            "password": "test123",
            "organization_id": org["id"]
        })
        assert login_res.status_code == 200

        me_res = client.get(
            "/users/me",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert me_res.status_code == 200
        assert me_res.json()["email"] == email

        logout_res = client.post(
            "/users/logout",
            headers={"Authorization": f"Bearer {token}"}
        )
        assert logout_res.status_code == 200
