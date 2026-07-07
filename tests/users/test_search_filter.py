import pytest


@pytest.mark.users
@pytest.mark.regression
class TestSearchAndFilter:
    def test_search_users_by_name(self, api_client):
        response = api_client.get("/users/search?q=Emily")
        assert response.status_code == 200
        body = response.json()
        assert "users" in body
        assert len(body["users"]) > 0
        assert any("Emily" in u.get("firstName", "") for u in body["users"])

    def test_search_returns_empty_for_unknown(self, api_client):
        response = api_client.get("/users/search?q=xyznonexistent123")
        assert response.status_code == 200
        body = response.json()
        assert body["total"] == 0

    def test_limit_restricts_result_count(self, api_client):
        response = api_client.get("/users?limit=3")
        assert response.status_code == 200
        body = response.json()
        assert len(body["users"]) == 3

    def test_skip_offsets_results(self, api_client):
        r1 = api_client.get("/users?limit=1&skip=0")
        r2 = api_client.get("/users?limit=1&skip=1")
        id1 = r1.json()["users"][0]["id"]
        id2 = r2.json()["users"][0]["id"]
        assert id1 != id2

    def test_sort_by_age_ascending(self, api_client):
        response = api_client.get("/users?sortBy=age&order=asc&limit=10")
        assert response.status_code == 200
        ages = [u["age"] for u in response.json()["users"]]
        assert ages == sorted(ages)

    def test_sort_by_age_descending(self, api_client):
        response = api_client.get("/users?sortBy=age&order=desc&limit=10")
        assert response.status_code == 200
        ages = [u["age"] for u in response.json()["users"]]
        assert ages == sorted(ages, reverse=True)

    def test_response_contains_total_count(self, api_client):
        response = api_client.get("/users")
        body = response.json()
        assert "total" in body
        assert body["total"] > 0
        assert body["total"] >= len(body["users"])

    def test_filter_users_by_key_returns_valid_structure(self, api_client):
        response = api_client.get("/users?select=id,firstName,email&limit=5")
        assert response.status_code == 200
        users = response.json()["users"]
        for user in users:
            assert "id" in user
            assert "firstName" in user
