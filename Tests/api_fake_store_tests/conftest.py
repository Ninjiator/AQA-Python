import pytest

from core.FakeStore.Clients.products_client import ProductsClient
from core.RestfulBooker.auth_client import AuthClient
from core.api_client import ApiClient
from utils.settings import d_settings


@pytest.fixture(scope="session")
def base_url():
    return d_settings.FAKE_STORE_URL

@pytest.fixture()
def api_client(base_url):
    return ApiClient(base_url)

@pytest.fixture()
def products_client(api_client):
    return ProductsClient(api_client)

@pytest.fixture()
def auth_client(api_client):
    return AuthClient(api_client)

@pytest.fixture(scope="session")
def auth_token(base_url):
    api_client = ApiClient(base_url)
    auth_client = AuthClient(api_client)

    response = auth_client.create_token(d_settings.USERNAME_FAKESTORE, d_settings.PASSWORD_FAKESTORE)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    return response.json()["token"]

@pytest.fixture()
def authorized_api_client(base_url, auth_token):
    api_client = ApiClient(base_url)
    api_client.session.cookies.set(auth_token)
    return api_client

@pytest.fixture()
def authorized_products_client(authorized_api_client):
    return ProductsClient(authorized_api_client)