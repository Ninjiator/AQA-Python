import pytest

from utils.settings import d_settings


@pytest.fixture(scope="session")
def base_url():
    return d_settings.FAKE_STORE_URL

@pytest.fixture()