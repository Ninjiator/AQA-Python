import pytest

@pytest.mark.fakestore
@pytest.mark.api
class TestsFakeStore:
    pass

class TestsProductsClientRead(TestsFakeStore):

    def test_get_all_products(self, products_client):
        response = products_client.get_all_products()

        assert response.status_code == 200, f"Cannot received response with all products"
        assert isinstance(response.json(), list), f"Response is not a list - {response.json()}"
        assert len(response.json()) > 0, "List with all products from response is empty"




