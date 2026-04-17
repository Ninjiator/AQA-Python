import requests
from utils.settings import d_settings

class Authentification:
    def __init__(self) -> None:
        self.auth_url = d_settings.RESTFUL_BOOKER_AUTH_URL
        self._auth_token = None


    def get_cached_auth_cookies(self) -> dict:
        if self._auth_token:
            return self._auth_token
        else:
            return self._get_auth_cookies()

    def _get_auth_cookies(self) -> dict:
        payload = {"username": f"{d_settings.USERNAME_RESTFUL_BOOKER}",
                   "password": f"{d_settings.PASS_RESTFUL_BOOKER}"}
        response = requests.post(self.auth_url, json=payload)

        assert response.status_code == 200, f"Auth is failed, re-check credentials in secrets"
        body = response.json()
        return {"token": body["token"]}