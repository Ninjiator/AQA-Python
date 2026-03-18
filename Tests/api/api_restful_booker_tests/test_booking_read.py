import pytest
import requests
from datetime import date

@pytest.mark.api
class TestsBooking:
    pass


class TestBookingRead(TestsBooking):
    def test_get_all_bookings(self, base_url):
        response = requests.get(f"{base_url}/booking")
        assert response.status_code == 200, "Expected status code 200, list with bookings unexist"

        response_body = response.json()

        assert isinstance(response_body, list), "Response type is not a list"
        assert len(response_body) > 0, "Body list with data is empty"
        assert "bookingid" in response_body[0], "booking id's is absent"

    def test_get_booking(self, base_url, create_booking_id):
        response = requests.get(f"{base_url}/booking/{create_booking_id}")
        assert response.status_code == 200, "Expected status code 200"
        body = response.json()

        assert "firstname" in body, "first name data is absent in response body "
        assert "lastname" in body, "last name data is absent in response body "

        checkin_date = date.fromisoformat(body["bookingdates"]["checkin"])
        checkout_date = date.fromisoformat(body["bookingdates"]["checkout"])

        assert checkin_date < checkout_date, f"booking checkout date - {checkout_date} is earlier than booking checkin date - {checkin_date}"

    @pytest.mark.parametrize("booking_id", [
        (0),
        (-1),
        ("id"),
        (999999999999999999999999999999)])
    def test_get_booking_negative(self, base_url, booking_id):
        response = requests.get(f"{base_url}/booking/{booking_id}")
        assert response.status_code == 404, "booking ID with invalid format exist"
