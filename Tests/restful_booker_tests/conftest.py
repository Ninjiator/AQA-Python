import pytest
import requests
from utils.settings import d_settings


@pytest.fixture(scope="session")
def base_url():
    return d_settings.RESFUL_BOOKER_URL

@pytest.fixture(scope="function")
def booking_payload():
     body = {"firstname":"Martin",
            "lastname":"King",
            "totalprice":2100,
            "depositpaid":True,
            "bookingdates":{"checkin":"2026-02-10","checkout":"2026-02-16"},
            "additionalneeds":"Breakfast"}
     return body


@pytest.fixture(scope="function")
def create_booking_id(base_url, booking_payload):
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200, f"Booking creation is failed with code {response.status_code} {response.text}"

    body = response.json()
    assert "bookingid" in body, f"No bookingid: {body}"
    return body["bookingid"]

@pytest.fixture()
def auth_token():
    payload = {"username": "admin",
            "password": "password123"}
    response = requests.post(f"https://restful-booker.herokuapp.com/auth", json=payload)

    assert response.status_code == 200, f"Auth is failed with credentials: {body}, status code received {response.status_code}, "
    body = response.json()
    return body["token"]