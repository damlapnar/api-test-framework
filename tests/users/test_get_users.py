import pytest
from utils.schema_validator import validate_schema


@pytest.mark.users
@pytest.mark.smoke
class TestGetUsers:
    def test_get_users_returns_200(self, api_client):
        response = api_client.get("/users")
        assert response.status_code == 200

    def test_get_users_returns_list(self, api_client):
        response = api_client.get("/users")
        body = response.json()
        assert "users" in body
        assert isinstance(body["users"], list)
        assert len(body["users"]) > 0

    def test_get_users_second_page(self, api_client):
        response = api_client.get("/users?limit=10&skip=10")
        body = response.json()
        assert body["skip"] == 10
        assert "users" in body

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
        assert body["id"] == 2

    def test_get_nonexistent_user_returns_404(self, api_client):
        response = api_client.get("/users/9999")
        assert response.status_code == 404

    @pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5, 6])
    def test_all_users_are_retrievable(self, api_client, user_id):
        response = api_client.get(f"/users/{user_id}")
        assert response.status_code == 200
        assert response.json()["id"] == user_id
