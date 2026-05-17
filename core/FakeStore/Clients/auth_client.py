from core.api_client import ApiClient


class AuthClient:
    def __init__(self, api_client : ApiClient):
        self.api = api_client

    def create_token(self, user_name, password):
        payload = {"username": f"{user_name}",
                   "password": f"{password}"}
        response = self.api.post("/auth/login", json = payload)

        return response