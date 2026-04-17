class TestJobControl:

    def test_get_workers(self, client):
        res = client.get("/jobs/workers")
        assert res.status_code == 200
        assert "workers" in res.json()

    def test_trigger_cleanup(self, client):
        res = client.post("/jobs/trigger/cleanup")

        assert res.status_code == 200
        data = res.json()
        assert "task_id" in data
        assert data["status"] == "started"

    def test_get_active_tasks(self, client):
        res = client.get("/jobs/active")
        assert res.status_code == 200
        assert "active_tasks" in res.json()
