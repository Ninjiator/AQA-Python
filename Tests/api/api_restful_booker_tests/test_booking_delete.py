import requests

from Tests.api.api_restful_booker_tests.test_booking_read import TestsBooking


class TestDeleteBooking(TestsBooking):
    def test_delete_booking(self, base_url, auth_cookie_token, create_booking_id):
        response = requests.delete(f"{base_url}/booking/{create_booking_id}", cookies=auth_cookie_token)
        assert response.status_code == 201, f"Booking id - {create_booking_id} is not deleted"

        response = requests.get(f"{base_url}/booking/{create_booking_id}")
        assert response.status_code == 404, f"Booking id - {create_booking_id} still exist"

    def test_delete_booking_without_token_negative(self, base_url, create_booking_id):
        response = requests.delete(f"{base_url}/booking/{create_booking_id}")
        assert response.status_code == 403, f"Booking id - {create_booking_id} was deleted without auth token"


