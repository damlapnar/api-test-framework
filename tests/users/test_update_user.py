import pytest


@pytest.mark.users
@pytest.mark.regression
class TestUpdateUser:
    def test_patch_user_updates_field(self, api_client):
        payload = {"firstName": "PatchedName"}
        response = api_client.patch("/users/2", payload)
        assert response.status_code == 200
        body = response.json()
        assert body["firstName"] == payload["firstName"]

    def test_put_user_updates_all_fields(self, api_client):
        payload = {"firstName": "Damla", "lastName": "Pinar", "age": 30}
        response = api_client.put("/users/2", payload)
        assert response.status_code == 200
        body = response.json()
        assert body["firstName"] == payload["firstName"]
        assert body["lastName"] == payload["lastName"]

    def test_response_time_under_threshold(self, api_client):
        response = api_client.get("/users/2")
        assert response.elapsed.total_seconds() < 5.0, "Response time exceeded 5s threshold"
