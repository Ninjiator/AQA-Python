from requests import Response
from core.api_client import ApiClient




class BookingClient:
    def __init__(self, api_client : ApiClient) -> None:
        self.api = api_client

    def get_all_bookings(self) -> Response:
        return self.api.get("booking")

    def get_booking(self, booking_id) -> Response:
        return self.api.get(f"booking/{booking_id}")

    def create_booking(self, booking_payload) -> Response:
        return self.api.post("booking",
                             json = booking_payload)

    def delete_booking(self, booking_id) -> Response:
        return self.api.delete(f"booking/{booking_id}")

    def update_booking(self, booking_id, booking_payload) -> Response:
        return self.api.put(f"booking/{booking_id}", json = booking_payload)

    def patch_booking(self, booking_id, booking_payload) -> Response:
        return self.api.patch(f"booking/{booking_id}",json = booking_payload)