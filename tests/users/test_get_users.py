import pytest
from utils.schema_validator import validate_schema


@pytest.mark.users
@pytest.mark.smoke
class TestGetUsers:
    def test_get_users_returns_200(self, api_client):
        response = api_client.get("/users?page=1")
        assert response.status_code == 200

    def test_get_users_returns_list(self, api_client):
        response = api_client.get("/users?page=1")
        body = response.json()
        assert "data" in body
        assert isinstance(body["data"], list)
        assert len(body["data"]) > 0

    def test_get_users_page_2(self, api_client):
        response = api_client.get("/users?page=2")
        body = response.json()
        assert body["page"] == 2

    def test_get_single_user_returns_200(self, api_client):
        response = api_client.get("/users/2")
        assert response.status_code == 200

    def test_get_single_user_schema(self, api_client):
        response = api_client.get("/users/2")
        body = response.json()
        validate_schema(body, "user")

    def test_get_single_user_correct_id(self, api_client):
        response = api_client.get("/users/2")
        body = response.json()
        assert body["data"]["id"] == 2

    def test_get_nonexistent_user_returns_404(self, api_client):
        response = api_client.get("/users/9999")
        assert response.status_code == 404

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
    def test_all_users_are_retrievable(self, api_client, user_id):
        response = api_client.get(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["data"]["id"] == user_id
