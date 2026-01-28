import requests
from utils.settings import d_settings
from datetime import date

BASE_URL = d_settings.RESFUL_BOOKER_URL
EXISTED_BOOKING_ID = d_settings.RESFUL_BOOKER_BOOKING_ID

def test_get_booking():
    response = requests.get(f"{BASE_URL}/booking")
    assert response.status_code == 200, "Expected status code 200"
    body = response.json()

    assert isinstance(body, list), "Response type is not a list"
    assert len(body) > 0, "Body list with data is empty"
    assert "bookingid" in body[0], "booking id's is absent"

def test_get_booking_by_id():
    response = requests.get(f"{BASE_URL}/booking/{EXISTED_BOOKING_ID}")
    assert response.status_code == 200, "Expected status code 200"
    body = response.json()
    print(response.text)

    assert "firstname" in body, "first name data is absent in response body "
    assert "lastname" in body, "last name data is absent in response body "

    checkin_date = date.fromisoformat(body["bookingdates"]["checkin"])
    checkout_date = date.fromisoformat(body["bookingdates"]["checkout"])

    assert checkin_date < checkout_date, "booking checkout is earlier than booking checkin"


