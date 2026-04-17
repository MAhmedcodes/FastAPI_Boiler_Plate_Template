import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestOrganizationFlow:

    def test_create_and_get_organizations(self):
        # Create organization
        create_response = client.post(
            "/organizations/create",
            json={"name": "Test Org 1"}
        )
        assert create_response.status_code == 200
        org1 = create_response.json()
        assert "invite_token" in org1

        # Create another organization
        create_response2 = client.post(
            "/organizations/create",
            json={"name": "Test Org 2"}
        )
        assert create_response2.status_code == 200
        org2 = create_response2.json()

        # Get all organizations
        get_response = client.get("/organizations/")
        assert get_response.status_code == 200
        data = get_response.json()
        assert data["count"] >= 2

        # Join organization
        join_response = client.post(
            "/organizations/join",
            json={"organization_id": org1["id"]}
        )
        assert join_response.status_code == 200
        join_data = join_response.json()
        assert join_data["invite_token"] == org1["invite_token"]
