import pytest
from datetime import date

@pytest.mark.restfulbooker
@pytest.mark.api
class TestsBooking:
    pass


class TestBookingRead(TestsBooking):
    def test_get_all_bookings(self, booking_client):
        response = booking_client.get_all_bookings()
        assert response.status_code == 200, "Expected status code 200, list with bookings unexist"

        assert isinstance(response.json(), list), "Response type is not a list"
        assert len(response.json()) > 0, "Body list with data is empty"
        assert "bookingid" in response.json()[0], "booking id's is absent"


    def test_get_booking(self, create_booking_id, booking_client):
        response = booking_client.get_booking(create_booking_id)
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
    def test_get_booking_negative(self, booking_client, booking_id):
        response = booking_client.get_booking(booking_id)
        assert response.status_code == 404, "booking ID with invalid format exist"
