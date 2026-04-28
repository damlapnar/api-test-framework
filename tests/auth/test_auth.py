import pytest


@pytest.mark.auth
@pytest.mark.smoke
class TestAuthentication:
    def test_login_with_valid_credentials(self, api_client):
        response = api_client.post("/login", {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        assert response.status_code == 200
        body = response.json()
        assert "token" in body
        assert len(body["token"]) > 0

    def test_login_with_invalid_credentials(self, api_client):
        response = api_client.post("/login", {
            "email": "invalid@test.com",
            "password": "wrongpassword"
        })
        assert response.status_code == 400
        body = response.json()
        assert "error" in body

    def test_login_without_password(self, api_client):
        response = api_client.post("/login", {
            "email": "eve.holt@reqres.in"
        })
        assert response.status_code == 400
        body = response.json()
        assert body["error"] == "Missing password"

    def test_register_with_valid_data(self, api_client):
        response = api_client.post("/register", {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        })
        assert response.status_code == 200
        body = response.json()
        assert "id" in body
        assert "token" in body

    def test_register_without_password(self, api_client):
        response = api_client.post("/register", {
            "email": "sydney@fife"
        })
        assert response.status_code == 400
        assert "error" in response.json()

    def test_login_response_contains_token_string(self, api_client):
        response = api_client.post("/login", {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        })
        token = response.json().get("token", "")
        assert isinstance(token, str) and len(token) > 0
