from Tests.api_fake_store_tests.test_products_client_read import TestFakeStore
from core.FakeStore.Models.products_model import ProductModel


class TestProductsClientUpdatePositive(TestFakeStore):
    def test_product_creation(self, authorized_products_client):
        payload = { "id" : 21,
                   "title" : "Product",
                   "price" : 100.5,
                   "description" : "It's a new product created for test",
                   "category" : "electronics",
                   "image" : "https://picsum.photos/id/237/200/300"

        }

        response_create = authorized_products_client.add_new_product(payload)
        assert response_create.status_code == 201, f"Expected status code 201, got {response_create.status_code}"
        ProductModel.model_validate(response_create.json())
        assert response_create.json() == payload

    def test_product_update(self, authorized_products_client):
        payload = {"id" : 1,
                   "title": "Product",
                   "price": 587,
                   "description": "It's a new updated product created for test",
                   "image": "https://picsum.photos/id/500"
                   }
        response = authorized_products_client.update_product(1, payload)
        print(payload)
        print(response.json())
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        assert response.json() == payload

    def test_product_delete(self, authorized_products_client):
        response_get = authorized_products_client.get_product(1)
        response_delete = authorized_products_client.delete_product(1)

        assert response_get.status_code == 200
        assert response_delete.status_code == 200

        ProductModel.model_validate(response_delete.json())

        assert response_delete.json() == response_get.json()
