import pytest


@pytest.mark.users
@pytest.mark.regression
class TestUpdateUser:
    def test_patch_user_updates_job(self, api_client):
        payload = {"job": "Lead QA Engineer"}
        response = api_client.patch("/users/2", payload)

        assert response.status_code == 200
        body = response.json()
        assert body["job"] == payload["job"]
        assert "updatedAt" in body

    def test_put_user_updates_all_fields(self, api_client):
        payload = {"name": "Damla", "job": "SDET"}
        response = api_client.put("/users/2", payload)

        assert response.status_code == 200
        body = response.json()
        assert body["name"] == payload["name"]
        assert body["job"] == payload["job"]

    def test_response_time_under_threshold(self, api_client):
        response = api_client.get("/users/2")
        assert response.elapsed.total_seconds() < 2.0, "Response time exceeded 2s threshold"
