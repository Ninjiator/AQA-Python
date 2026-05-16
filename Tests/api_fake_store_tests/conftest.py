import pytest

from core.FakeStore.Clients.products_client import ProductsClient
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