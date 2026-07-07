import requests
import os
from dotenv import load_dotenv

load_dotenv()


class APIClient:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or os.getenv("BASE_URL", "https://dummyjson.com")
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def set_auth_token(self, token: str):
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def get(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.get(f"{self.base_url}{endpoint}", **kwargs)

    def post(self, endpoint: str, payload: dict = None, **kwargs) -> requests.Response:
        return self.session.post(f"{self.base_url}{endpoint}", json=payload, **kwargs)

    def put(self, endpoint: str, payload: dict = None, **kwargs) -> requests.Response:
        return self.session.put(f"{self.base_url}{endpoint}", json=payload, **kwargs)

    def patch(self, endpoint: str, payload: dict = None, **kwargs) -> requests.Response:
        return self.session.patch(f"{self.base_url}{endpoint}", json=payload, **kwargs)

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        return self.session.delete(f"{self.base_url}{endpoint}", **kwargs)
