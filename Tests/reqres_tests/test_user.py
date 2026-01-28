import requests
from utils.settings import d_settings

BASE_URL = d_settings.REQRES_URL

def test_get_users_page_1():
    response = requests.get(f"{BASE_URL}/users", params={"page": 1})
    assert response.status_code == 200, "Expected status code 200"

    body = response.json()
    assert body["page"] == 1, "Incorrect page number"
    assert len(body["data"]) > 0, "Zero data received from response body"
