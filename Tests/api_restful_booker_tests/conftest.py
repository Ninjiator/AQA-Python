import pytest
import requests
from faker import Faker

from core.RestfulBooker.booking_client import BookingClient
from utils.settings import d_settings


@pytest.fixture(scope="session")
def base_url():
    return d_settings.RESTFUL_BOOKER_URL

@pytest.fixture()
def b_payload():
    faker = Faker()
    body = {"firstname":f"{faker.first_name()}",
            "lastname":f"{faker.last_name()}",
            "totalprice": 1000,
            "depositpaid":True,
            "bookingdates":{"checkin":"2026-02-10","checkout":"2026-02-16"},
            "additionalneeds":"Breakfast"}
    return body


@pytest.fixture()
def create_booking_id(booking_client, b_payload):
    response =  booking_client.create_booking(b_payload)
    assert response.status_code == 200, f"Booking creation is failed with code {response.status_code} {response.text}"

    body = response.json()
    assert "bookingid" in body, f"No bookingid: {body}"
    return body["bookingid"]

@pytest.fixture()
def auth_cookie_token():
    payload = {"username": "admin",
            "password": "password123"}
    response = requests.post(d_settings.RESTFUL_BOOKER_AUTH_URL, json=payload)

    assert response.status_code == 200, f"Auth is failed with credentials: {payload}, status code received {response.status_code}, "
    body = response.json()
    return {"token": body["token"]}

@pytest.fixture()
def booking_client():
    client = BookingClient()
    yield client
    client.session.close()