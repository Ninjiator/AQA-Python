from utils.settings import d_settings
import requests



class BookingClient:
    def __init__(self):
        self.base_url = d_settings.RESTFUL_BOOKER_URL
        self.auth_url = d_settings.RESTFUL_BOOKER_AUTH_URL
        self.session = requests.Session()
        self._auth_token = None


    def _request(self, method, endpoint, **kwargs):
        return self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            **kwargs
        )

    def _get_cached_auth_cookies(self):
        if self._auth_token:
            return self._auth_token
        else:
            return self._get_auth_cookies()

    def _get_auth_cookies(self):
        payload = {"username": f"{d_settings.USERNAME_RESTFUL_BOOKER}",
                   "password": f"{d_settings.PASS_RESTFUL_BOOKER}"}
        response = requests.post(self.auth_url, json=payload)

        assert response.status_code == 200, f"Auth is failed, re-check credentials in secrets"
        body = response.json()
        return {"token": body["token"]}

    def get_all_bookings(self):
        return self._request("GET", "/booking")

    def get_booking(self, booking_id):
        return self._request("GET", f"/booking/{booking_id}")

    def create_booking(self, booking_payload):
        return self._request('POST',f"/booking",
                             json = booking_payload)

    def delete_booking(self, booking_id, auth = True):
        if auth:
            return self._request("DELETE", f"/booking/{booking_id}",
                                 cookies = self._get_cached_auth_cookies())
        else:
            return self._request("DELETE", f"/booking/{booking_id}")

    def update_booking(self, booking_id, booking_payload, auth = True):
        if auth:
            return self._request("PUT", f"/booking/{booking_id}",
                             cookies = self._get_cached_auth_cookies(), json = booking_payload)
        else:
            return self._request("PUT", f"/booking/{booking_id}", json=booking_payload)

    def patch_booking(self, booking_id, booking_payload, auth = True):
        if auth:
            return self._request("PATCH", f"/booking/{booking_id}",
                             cookies = self._get_cached_auth_cookies(), json = booking_payload)
        else:
            return self._request("PATCH", f"/booking/{booking_id}",
                                 json=booking_payload)