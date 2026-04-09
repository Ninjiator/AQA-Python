from Tests.ui_hillel_auto_tests.test_registration_form_positive import Authentication
from utils.settings import d_settings
import requests
from core.RestfulBooker.Authentification import Authentification



class BookingClient:
    def __init__(self):
        self.base_url = d_settings.RESTFUL_BOOKER_URL
        self.session = requests.Session()
        self.auth = Authentification()

    def _request(self, method, endpoint, **kwargs):
        return self.session.request(
            method=method,
            url=f"{self.base_url}{endpoint}",
            **kwargs
        )

    def get_all_bookings(self):
        return self._request("GET", "/booking")

    def get_booking(self, booking_id):
        return self._request("GET", f"/booking/{booking_id}")

    def create_booking(self, booking_payload):
        return self._request('POST',f"/booking",
                             json = booking_payload)

    def delete_booking(self, booking_id, *, auth = False):
        if auth:
            return self._request("DELETE", f"/booking/{booking_id}",
                                 cookies = self.auth.get_cached_auth_cookies())
        else:
            return self._request("DELETE", f"/booking/{booking_id}")

    def update_booking(self, booking_id, booking_payload, auth = False):
        if auth:
            return self._request("PUT", f"/booking/{booking_id}",
                             cookies = self.auth.get_cached_auth_cookies(), json = booking_payload)
        else:
            return self._request("PUT", f"/booking/{booking_id}", json=booking_payload)

    def patch_booking(self, booking_id, booking_payload, auth = False):
        if auth:
            return self._request("PATCH", f"/booking/{booking_id}",
                             cookies = self.auth.get_cached_auth_cookies(), json = booking_payload)
        else:
            return self._request("PATCH", f"/booking/{booking_id}",
                                 json=booking_payload)