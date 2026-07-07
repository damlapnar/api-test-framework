import pytest


@pytest.mark.users
@pytest.mark.regression
class TestDeleteUser:
    def test_delete_user_returns_200(self, api_client):
        response = api_client.delete("/users/5")
        assert response.status_code == 200

    def test_delete_user_marks_as_deleted(self, api_client):
        response = api_client.delete("/users/6")
        body = response.json()
        assert body.get("isDeleted") is True

    def test_delete_response_has_timestamp(self, api_client):
        response = api_client.delete("/users/7")
        body = response.json()
        assert "deletedOn" in body

    def test_delete_response_time(self, api_client):
        import time
        start = time.time()
        api_client.delete("/users/8")
        elapsed = (time.time() - start) * 1000
        assert elapsed < 3000, f"Delete too slow: {elapsed:.0f}ms"
