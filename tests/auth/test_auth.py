import pytest


@pytest.mark.auth
@pytest.mark.smoke
class TestAuthentication:
    def test_login_with_valid_credentials(self, api_client):
        response = api_client.post("/auth/login", {
            "username": "emilys",
            "password": "emilyspass",
        })
        assert response.status_code == 200
        body = response.json()
        assert "accessToken" in body
        assert len(body["accessToken"]) > 0

    def test_login_with_invalid_credentials(self, api_client):
        response = api_client.post("/auth/login", {
            "username": "invalid_user",
            "password": "wrongpassword",
        })
        assert response.status_code in (400, 401)
        body = response.json()
        assert "message" in body

    def test_login_without_password(self, api_client):
        response = api_client.post("/auth/login", {
            "username": "emilys",
        })
        assert response.status_code in (400, 401)

    def test_login_returns_refresh_token(self, api_client):
        response = api_client.post("/auth/login", {
            "username": "emilys",
            "password": "emilyspass",
        })
        assert response.status_code == 200
        body = response.json()
        assert "refreshToken" in body
        assert len(body["refreshToken"]) > 0

    def test_login_returns_user_info(self, api_client):
        response = api_client.post("/auth/login", {
            "username": "emilys",
            "password": "emilyspass",
        })
        body = response.json()
        assert "id" in body
        assert "username" in body
        assert body["username"] == "emilys"

    def test_authenticated_request(self, api_client):
        login_resp = api_client.post("/auth/login", {
            "username": "emilys",
            "password": "emilyspass",
        })
        token = login_resp.json()["accessToken"]
        response = api_client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
        assert response.status_code == 200
        body = response.json()
        assert "username" in body
