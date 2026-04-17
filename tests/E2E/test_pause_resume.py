import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestPauseResume:

    def test_pause_resume_welcome_email(self):
        # Pause task
        pause_response = client.post(
            "/jobs/pause",
            json={"task_name": "welcome_email"}
        )
        assert pause_response.status_code == 200
        assert pause_response.json()["is_paused"] is True

        # Check paused tasks
        paused_response = client.get("/jobs/paused")
        assert paused_response.status_code == 200
        tasks = paused_response.json()["tasks"]
        welcome_task = next(
            (t for t in tasks if t["task_name"] == "welcome_email"), None)
        assert welcome_task["is_paused"] is True  # type: ignore

        # Resume task
        resume_response = client.post(
            "/jobs/resume",
            json={"task_name": "welcome_email"}
        )
        assert resume_response.status_code == 200
        assert resume_response.json()["is_paused"] is False
