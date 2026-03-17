import requests
from datetime import date
import pytest

@pytest.mark.api
class TestRestFulBooker:
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
        assert "application/json" not in response.headers.get("Content-Type",
                                                              ""), "booking ID with invalid format has a Content-type application/json"
        if response.headers.get("Content-Type", "").startswith("application/json"):
            body = response.json()
            assert "firstname" not in body, "First name data is present in booking ID with invalid format"

    def test_update_booking(self, base_url, create_booking_id, auth_cookie_token):
        booking_payload = {
            "firstname": "Updated",
            "lastname": "User",
            "totalprice": 999,
            "depositpaid": True,
            "bookingdates": {"checkin": "2026-03-01", "checkout": "2026-03-10"},
            "additionalneeds": "Dinner"}
        response = requests.put(f"{base_url}/booking/{create_booking_id}", cookies=auth_cookie_token,
                                json=booking_payload)
        put_body = response.json()

        assert booking_payload["firstname"] in put_body[
            'firstname'], f"First Name - {booking_payload["firstname"]} was not updated in put_body"
        assert booking_payload["lastname"] in put_body[
            'lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated in put_body"

        get_response = requests.get(f"{base_url}/booking/{create_booking_id}")
        assert get_response.status_code == 200

        get_body = get_response.json()

        assert booking_payload["firstname"] in get_body[
            'firstname'], f"First Name - {booking_payload["firstname"]} was not updated after put request"
        assert booking_payload["lastname"] in get_body[
            'lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated after put request"

        assert response.status_code == 200, f"Access forbidden, verify auth cookies"

    def test_update_booking_without_valid_token(self, base_url, create_booking_id):
        booking_payload = {
            "firstname": "Updated",
            "lastname": "User",
            "totalprice": 999,
            "depositpaid": True,
            "bookingdates": {"checkin": "2026-03-01", "checkout": "2026-03-10"},
            "additionalneeds": "Dinner"}

        response = requests.put(f"{base_url}/booking/{create_booking_id}", json=booking_payload)
        assert response.status_code in (403, 401), f"Access is given without auth cookies"

    def test_patch_booking(self, base_url, create_booking_id, auth_cookie_token):
        booking_payload = {
            "firstname": "Mikie",
            "lastname": "Howard"}
        response = requests.patch(f"{base_url}/booking/{create_booking_id}", cookies=auth_cookie_token,
                                  json=booking_payload)
        assert response.status_code == 200, "Patch request is failed"
        patch_body = response.json()

        assert booking_payload["firstname"] in patch_body[
            'firstname'], f"First Name - {booking_payload["firstname"]} was not updated in patch_body"
        assert booking_payload["lastname"] in patch_body[
            'lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated in patch_body"

        get_response = requests.get(f"{base_url}/booking/{create_booking_id}")
        get_body = get_response.json()

        assert booking_payload["firstname"] in get_body[
            'firstname'], f"First Name - {booking_payload["firstname"]} was not updated after patch request"
        assert booking_payload["lastname"] in get_body[
            'lastname'], f"lastname Name - {booking_payload["lastname"]} was not updated after patch request"

    def test_delete_booking(self, base_url, auth_cookie_token, create_booking_id):
        response = requests.delete(f"{base_url}/booking/{create_booking_id}", cookies=auth_cookie_token)
        assert response.status_code == 201, f"Booking id - {create_booking_id} is not deleted"

        response = requests.get(f"{base_url}/booking/{create_booking_id}")
        assert response.status_code == 404, f"Booking id - {create_booking_id} still exist"

    def test_delete_booking_without_token_negative(self, base_url, create_booking_id):
        response = requests.delete(f"{base_url}/booking/{create_booking_id}")
        assert response.status_code == 403, f"Booking id - {create_booking_id} was deleted without auth token"

    # def test_create_bookings(self, base_url)

