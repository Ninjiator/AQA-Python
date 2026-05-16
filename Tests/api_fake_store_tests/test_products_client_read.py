import pytest

from core.FakeStore.Models.products_model import ProductModel


@pytest.mark.fakestore
@pytest.mark.api
class TestsFakeStore:
    pass

class TestsProductsClientRead(TestsFakeStore):

    def test_schema_and_data_of_first_product(self, products_client):
        first_product = products_client.get_product(product_id=1)
        assert first_product.status_code == 200, f"Expected status code 200, got {first_product.status_code}, Product with id 1 is absent"

        model_of_first_product = ProductModel.model_validate(first_product.json())
        assert model_of_first_product.price > 0, "Price of product with id=1 is less than 0"
        assert model_of_first_product.description != "", "Product description is empty"
        assert model_of_first_product.title != "", "Product title is empty"
        assert model_of_first_product.category != "", "Product category is empty"
        assert model_of_first_product.image != "", "Product url is empty"

    def test_get_all_products(self, products_client):
        response = products_client.get_all_products()

        assert response.status_code == 200, f"""Expected status code 200, got {response.status_code},
                                                        Cannot get all products"""
        assert isinstance(response.json(), list), f"Response is not a list - {response.json()}"
        assert len(response.json()) > 0, "List with products from response is empty"



    @pytest.mark.parametrize("sort_type",
                              [("asc"),
                              ("desc")])
    def test_get_products_sort_asc(self, products_client, sort_type):
        response = products_client.get_all_products(sort=sort_type)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        products = response.json()
        products_ids = [product["id"] for product in products]

        sort_flag = False
        if sort_type == "desc":
            sort_flag = True

        assert products_ids == sorted(products_ids, reverse=sort_flag), f"Products are not sorted in {sort_type} order"


    @pytest.mark.parametrize("limit", (1, 5, 10))
    def test_get_products_by_limit(self, products_client, limit):
        response = products_client.get_all_products(limit=limit)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        products_amount = len(response.json())
        assert limit == products_amount, f"Expected amount of products is {limit}, got {products_amount} instead"
        ProductModel.model_validate(response.json()[0])


    def test_get_all_categories(self, products_client):
        response = products_client.get_all_categories()

        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        categories_actual = response.json()

        categories = [category != "" for category in categories_actual]

        assert len(categories_actual) == len(categories), "Part of categories are empty"

    def test_get_products_by_category(self, products_client):
        categories = products_client.get_all_categories().json()

        for category in categories:
            response = products_client.get_products_by_category(category)

            assert response.status_code == 200, (f"Expected status code 200, got {response.status_code}"
                                                 f"for request with category {category}")

            actual_category = response.json()[0]["category"]
            assert actual_category == category, f"Actual category name {actual_category} is not equal expected {category}"
