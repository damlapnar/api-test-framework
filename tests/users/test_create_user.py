import pytest


@pytest.mark.users
@pytest.mark.smoke
class TestCreateUser:
    def test_create_user_returns_201(self, api_client, new_user_payload):
        response = api_client.post("/users/add", new_user_payload)
        assert response.status_code == 201

    def test_create_user_returns_name(self, api_client, new_user_payload):
        response = api_client.post("/users/add", new_user_payload)
        body = response.json()
        assert body["firstName"] == new_user_payload["firstName"]
        assert body["lastName"] == new_user_payload["lastName"]

    def test_create_user_returns_id(self, api_client, new_user_payload):
        response = api_client.post("/users/add", new_user_payload)
        body = response.json()
        assert "id" in body
        assert body["id"] is not None

    def test_create_user_returns_email(self, api_client, new_user_payload):
        response = api_client.post("/users/add", new_user_payload)
        body = response.json()
        assert "email" in body

    def test_update_user_returns_200(self, api_client):
        payload = {"firstName": "UpdatedFirst", "lastName": "UpdatedLast"}
        response = api_client.put("/users/2", payload)
        assert response.status_code == 200
        body = response.json()
        assert body["firstName"] == payload["firstName"]

    def test_delete_user_returns_200(self, api_client):
        response = api_client.delete("/users/2")
        assert response.status_code == 200
        body = response.json()
        assert body.get("isDeleted") is True
