from utils.settings import d_settings
import requests



class BookingClient:
    def __init__(self):
        self.base_url = d_settings.RESTFUL_BOOKER_URL
        self.session = requests.Session()


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
        return self._request('POST',f"/booking", json = booking_payload)

    def delete_booking(self, booking_id, cookies_token=None):
        return self._request("DELETE", f"/booking/{booking_id}",
                             cookies = cookies_token)

    def update_booking(self, booking_id, booking_payload, cookies_token=None):
        return self._request("PUT", f"/booking/{booking_id}",
                             cookies = cookies_token, json = booking_payload)

    def patch_booking(self, booking_id, booking_payload, cookies_token = None):
        return self._request("PATCH", f"/booking/{booking_id}",
                             cookies = cookies_token, json = booking_payload)