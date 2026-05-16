import pytest
from faker import Faker

from core.RestfulBooker.auth_client import AuthClient
from core.RestfulBooker.booking_client import BookingClient
from core.api_client import ApiClient
from utils.settings import d_settings


@pytest.fixture(scope="session")
def base_url() -> str:
    return d_settings.RESTFUL_BOOKER_URL

@pytest.fixture()
def api_client(base_url):
    api_client = ApiClient(base_url)
    return api_client

@pytest.fixture()
def auth_client(api_client):
    return AuthClient(api_client)


@pytest.fixture()
def booking_client(api_client):
    return BookingClient(api_client)

@pytest.fixture(scope="session")
def auth_token(base_url):
    api_client = ApiClient(base_url)
    auth_client = AuthClient(api_client)

    response = auth_client.create_token(d_settings.USERNAME_RESTFUL_BOOKER, d_settings.PASS_RESTFUL_BOOKER)
    assert response.status_code == 200
    return response.json()["token"]


@pytest.fixture()
def authorized_api_client(base_url, auth_token):
    api_client = ApiClient(base_url)

    api_client.session.cookies.set("token", auth_token)
    return api_client


@pytest.fixture()
def authorized_booking_client(authorized_api_client):
    return BookingClient(authorized_api_client)


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
def create_booking_id(authorized_booking_client, b_payload):
    response =  authorized_booking_client.create_booking(b_payload)
    assert response.status_code == 200, f"Booking creation is failed with code {response.status_code} {response.text}"

    body = response.json()
    assert "bookingid" in body, f"No bookingid: {body}"
    yield body["bookingid"]
    authorized_booking_client.delete_booking(body["bookingid"])
