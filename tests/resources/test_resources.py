import pytest


@pytest.mark.regression
class TestResources:
    def test_get_resources_returns_200(self, api_client):
        response = api_client.get("/unknown")
        assert response.status_code == 200

    def test_get_resources_has_data_array(self, api_client):
        response = api_client.get("/unknown")
        body = response.json()
        assert "data" in body
        assert isinstance(body["data"], list)
        assert len(body["data"]) > 0

    def test_get_single_resource(self, api_client):
        response = api_client.get("/unknown/2")
        assert response.status_code == 200
        body = response.json()
        assert body["data"]["id"] == 2
        assert "name" in body["data"]

    def test_get_nonexistent_resource_returns_404(self, api_client):
        response = api_client.get("/unknown/9999")
        assert response.status_code == 404

    def test_resources_have_required_fields(self, api_client):
        response = api_client.get("/unknown")
        resources = response.json()["data"]
        for resource in resources:
            assert "id" in resource
            assert "name" in resource
            assert "year" in resource
            assert "color" in resource

    @pytest.mark.smoke
    def test_resources_response_time(self, api_client):
        import time
        start = time.time()
        api_client.get("/unknown")
        elapsed = (time.time() - start) * 1000
        assert elapsed < 800, f"Response too slow: {elapsed:.0f}ms"
