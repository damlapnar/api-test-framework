import pytest


@pytest.mark.users
@pytest.mark.smoke
class TestCreateUser:
    def test_create_user_returns_201(self, api_client, new_user_payload):
        response = api_client.post("/users", new_user_payload)
        assert response.status_code == 201

    def test_create_user_returns_name_and_job(self, api_client, new_user_payload):
        response = api_client.post("/users", new_user_payload)
        body = response.json()
        assert body["name"] == new_user_payload["name"]
        assert body["job"] == new_user_payload["job"]

    def test_create_user_returns_id(self, api_client, new_user_payload):
        response = api_client.post("/users", new_user_payload)
        body = response.json()
        assert "id" in body
        assert body["id"] is not None

    def test_create_user_returns_created_at(self, api_client, new_user_payload):
        response = api_client.post("/users", new_user_payload)
        body = response.json()
        assert "createdAt" in body

    def test_update_user_returns_200(self, api_client):
        payload = {"name": "Updated Name", "job": "Senior QA Engineer"}
        response = api_client.put("/users/2", payload)
        assert response.status_code == 200
        body = response.json()
        assert body["name"] == payload["name"]
        assert "updatedAt" in body

    def test_delete_user_returns_204(self, api_client):
        response = api_client.delete("/users/2")
        assert response.status_code == 204
