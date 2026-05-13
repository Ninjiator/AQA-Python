from requests import Response

from utils.settings import d_settings
import requests
from core.RestfulBooker.auth_client import Authentication



class BookingClient:
    def __init__(self) -> None:
        self.base_url = d_settings.RESTFUL_BOOKER_URL
        self.session = requests.Session()
        self.auth = Authentication()

    def _request(self, method : str, endpoint : str, auth : bool = False, **kwargs) -> Response:
        if auth:
            kwargs["cookies"] = self.auth.get_cached_auth_cookies()

        return self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            **kwargs
        )


    def get_all_bookings(self) -> Response:
        return self._request("GET", "/booking")

    def get_booking(self, booking_id) -> Response:
        return self._request("GET", f"/booking/{booking_id}")

    def create_booking(self, booking_payload) -> Response:
        return self._request('POST',f"/booking",
                             json = booking_payload)

    def delete_booking(self, booking_id, *, auth = False) -> Response:
        return self._request("DELETE", f"/booking/{booking_id}", auth = auth)

    def update_booking(self, booking_id, booking_payload, auth = False) -> Response:
        return self._request("PUT", f"/booking/{booking_id}", auth = auth, json = booking_payload)

    def patch_booking(self, booking_id, booking_payload, auth = False) -> Response:
        return self._request("PATCH", f"/booking/{booking_id}", auth = auth, json = booking_payload)