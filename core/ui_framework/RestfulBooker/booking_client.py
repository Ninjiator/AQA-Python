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

    def delete_booking(self, booking_id, token):
        return self._request("DELETE", f"/booking/{booking_id}", cookies = token)

    def delete_booking_no_auth(self, booking_id):
        return self._request("DELETE", f"/booking/{booking_id}")