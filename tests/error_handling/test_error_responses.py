import pytest


@pytest.mark.regression
class TestErrorResponses:
    def test_invalid_user_id_returns_404(self, api_client):
        response = api_client.get("/users/99999")
        assert response.status_code == 404
        body = response.json()
        assert "message" in body

    def test_invalid_product_id_returns_404(self, api_client):
        response = api_client.get("/products/99999")
        assert response.status_code == 404

    def test_missing_auth_credentials_returns_400(self, api_client):
        response = api_client.post("/auth/login", {})
        assert response.status_code in (400, 401)

    def test_wrong_password_returns_error(self, api_client):
        response = api_client.post("/auth/login",
            {"username": "emilys", "password": "wrongpassword"})
        assert response.status_code in (400, 401)
        assert "message" in response.json()

    def test_response_time_under_threshold(self, api_client):
        response = api_client.get("/users/1")
        assert response.elapsed.total_seconds() < 5.0

    def test_get_users_returns_json_content_type(self, api_client):
        response = api_client.get("/users")
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type
