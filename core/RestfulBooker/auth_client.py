from requests import Response



class AuthClient:
    def __init__(self, api_client) -> None:
        self.api = api_client


    def create_token(self, user_name, password) -> Response:
        payload = {"username": f"{user_name}",
                   "password": f"{password}"}
        response = self.api.post("/auth", json=payload)
        return response