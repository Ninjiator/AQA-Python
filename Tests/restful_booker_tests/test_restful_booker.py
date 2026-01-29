import requests
from datetime import date


def test_get_booking(base_url):
    response = requests.get(f"{base_url}/booking")
    assert response.status_code == 200, "Expected status code 200"
    body = response.json()

    assert isinstance(body, list), "Response type is not a list"
    assert len(body) > 0, "Body list with data is empty"
    assert "bookingid" in body[0], "booking id's is absent"

def test_get_booking_by_id(base_url, create_booking_id):
    response = requests.get(f"{base_url}/booking/{create_booking_id}")
    assert response.status_code == 200, "Expected status code 200"
    body = response.json()

    assert "firstname" in body, "first name data is absent in response body "
    assert "lastname" in body, "last name data is absent in response body "

    checkin_date = date.fromisoformat(body["bookingdates"]["checkin"])
    checkout_date = date.fromisoformat(body["bookingdates"]["checkout"])

    assert checkin_date < checkout_date, f"booking checkout date - {checkout_date} is earlier than booking checkin date - {checkin_date}"

def test_change_booking_info(base_url, create_booking_id, auth_token):
    response = requests.put(f"{base_url}/booking/{create_booking_id}")
