import pytest
from faker import Faker
from utils.api_client import APIClient

fake = Faker()


@pytest.fixture(scope="session")
def api_client():
    return APIClient()


@pytest.fixture(scope="session")
def auth_token(api_client):
    response = api_client.post("/auth/login", {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30,
    })
    assert response.status_code == 200
    return response.json()["accessToken"]


@pytest.fixture(scope="session")
def authenticated_client(api_client, auth_token):
    api_client.set_auth_token(auth_token)
    return api_client


@pytest.fixture
def new_user_payload():
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "age": fake.random_int(min=18, max=65),
        "email": fake.email(),
    }
