from Tests.ui_hillel_auto_tests.test_registration_form_positive import Authentication
from utils.settings import d_settings
import requests
from core.RestfulBooker.Authentification import Authentification



class BookingClient:
    def __init__(self):
        self.base_url = d_settings.RESTFUL_BOOKER_URL
        self.session = requests.Session()
        self.auth = Authentification()

    def _request(self, method, endpoint, auth = False, **kwargs):
        if auth:
            kwargs["cookies"] = self.auth.get_cached_auth_cookies()

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
        return self._request("DELETE", f"/booking/{booking_id}", auth = auth)


    def update_booking(self, booking_id, booking_payload, auth = False):
        return self._request("PUT", f"/booking/{booking_id}", auth = auth, json = booking_payload)

    def patch_booking(self, booking_id, booking_payload, auth = False):
        return self._request("PATCH", f"/booking/{booking_id}", auth = auth, json = booking_payload)