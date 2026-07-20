import pytest


@pytest.mark.products
@pytest.mark.regression
class TestResources:
    def test_get_products_returns_200(self, api_client):
        response = api_client.get("/products")
        assert response.status_code == 200

    def test_get_products_has_data_array(self, api_client):
        response = api_client.get("/products")
        body = response.json()
        assert "products" in body
        assert isinstance(body["products"], list)
        assert len(body["products"]) > 0

    def test_get_single_product(self, api_client):
        response = api_client.get("/products/2")
        assert response.status_code == 200
        body = response.json()
        assert body["id"] == 2
        assert "title" in body

    def test_get_nonexistent_product_returns_404(self, api_client):
        response = api_client.get("/products/9999")
        assert response.status_code == 404

    def test_products_have_required_fields(self, api_client):
        response = api_client.get("/products")
        products = response.json()["products"]
        for product in products:
            assert "id" in product
            assert "title" in product
            assert "price" in product
            assert "category" in product

    @pytest.mark.smoke
    def test_resources_response_time(self, api_client):
        import time
        start = time.time()
        api_client.get("/products")
        elapsed = (time.time() - start) * 1000
        assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms"
