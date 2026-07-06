import pytest


@pytest.mark.users
@pytest.mark.regression
class TestDeleteUser:
    def test_delete_user_returns_204(self, api_client):
        response = api_client.delete("/users/2")
        assert response.status_code == 204

    def test_delete_user_has_empty_body(self, api_client):
        response = api_client.delete("/users/2")
        assert response.text == ""

    def test_delete_non_existent_user(self, api_client):
        response = api_client.delete("/users/9999")
        assert response.status_code == 204

    def test_delete_response_time(self, api_client):
        import time
        start = time.time()
        api_client.delete("/users/2")
        elapsed = (time.time() - start) * 1000
        assert elapsed < 1000, f"Delete too slow: {elapsed:.0f}ms"
