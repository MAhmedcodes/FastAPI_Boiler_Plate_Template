import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestJobControl:

    def test_get_workers(self):
        response = client.get("/jobs/workers")
        assert response.status_code == 200
        assert "workers" in response.json()

    def test_trigger_cleanup(self):
        response = client.post("/jobs/trigger/cleanup")
        assert response.status_code == 200
        data = response.json()
        assert "task_id" in data
        assert data["status"] == "started"

    def test_get_active_tasks(self):
        response = client.get("/jobs/active")
        assert response.status_code == 200
        assert "active_tasks" in response.json()
