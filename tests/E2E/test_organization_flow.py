import uuid


class TestOrganizationFlow:

    def test_create_and_get_organizations(self, client):

        org1 = client.post(
            "/organizations/create",
            json={"name": f"Org-{uuid.uuid4()}"}
        )
        assert org1.status_code == 200
        org1_data = org1.json()

        org2 = client.post(
            "/organizations/create",
            json={"name": f"Org-{uuid.uuid4()}"}
        )
        assert org2.status_code == 200

        get_res = client.get("/organizations/")
        assert get_res.status_code == 200
        data = get_res.json()
        assert data["count"] >= 2

        join_res = client.post(
            "/organizations/join",
            json={"organization_id": org1_data["id"]}
        )
        assert join_res.status_code == 200
