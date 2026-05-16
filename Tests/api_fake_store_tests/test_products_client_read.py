import pytest
from core.FakeStore.Models.products_model import ProductModel


@pytest.mark.fakestore
@pytest.mark.api
class TestFakeStore:
    pass

@pytest.mark.positive
class TestProductsClientReadPositive(TestFakeStore):

    def test_product_schema(self, products_client):
        first_product = products_client.get_product(1)
        assert first_product.status_code == 200, f"Expected status code 200, got {first_product.status_code}, Product with id 1 is absent"

        ProductModel.model_validate(first_product.json())

    def test_products_data(self, products_client):
        products_request = products_client.get_all_products()
        assert products_request.status_code == 200, f"Expected status code 200, got {products_request.status_code}, Product with id 1 is absent"
        products = products_request.json()

        for product in products:
            product_model = ProductModel.model_validate(product)
            assert product_model.id > 0, f"Negative id in {product}"
            assert product_model.price > 0, f"Price of product with id {product_model.id} is less than 0"
            assert product_model.description != "", f"Product description is empty for {product_model.id}"
            assert product_model.title != "", f"Product title is empty for {product_model.id}"
            assert product_model.category != "", f"Product category is empty for {product_model.id}"
            assert product_model.image != "", f"Product url is empty for {product_model.id}"

    def test_get_all_products(self, products_client):
        response = products_client.get_all_products()
        body = response.json()

        assert response.status_code == 200, f"""Expected status code 200, got {response.status_code},
                                                        Cannot get all products"""
        assert isinstance(body, list), f"Response is not a list - {body}"
        assert len(body) > 0, "List with products from response is empty"

    @pytest.mark.parametrize("sort_type",
                              [("asc"),
                              ("desc")])
    def test_get_products_sorted(self, products_client, sort_type):
        response = products_client.get_all_products(sort=sort_type)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        products = response.json()
        products_ids = [product["id"] for product in products]
        assert len(products_ids) > 0
        is_reverse= False
        if sort_type == "desc":
            is_reverse = True
        assert products_ids == sorted(products_ids, reverse=is_reverse), f"Products are not sorted in {sort_type} order"


    @pytest.mark.parametrize("limit", (1, 5, 10))
    def test_get_products_by_limit(self, products_client, limit):
        response = products_client.get_all_products(limit=limit)
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        products_amount = len(response.json())
        assert products_amount == limit, f"Expected amount of products is {limit}, got {products_amount} instead"


    def test_get_all_categories(self, products_client):
        response = products_client.get_all_categories()
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        categories_body = response.json()
        categories = [len(category) > 0 for category in categories_body]

        assert len(categories_body) == len(categories), "Part of categories are empty"

    def test_get_products_by_category(self, products_client):
        categories_response = products_client.get_all_categories()
        categories_list = categories_response.json()

        assert categories_response.status_code == 200, f"Expected status code 200, got {categories_response.status_code}"
        assert len(categories_list) > 0, f"Categories are absent"

        for category in categories_list:
            products_response = products_client.get_products_by_category(category)
            products_in_one_category = products_response.json()
            assert products_response.status_code == 200
            assert len(products_in_one_category) > 0, f"Category {category} does not contain products"
            for product in products_in_one_category:
                assert product["category"] == category, f'Actual category name: {product["category"]} in product {product} is not equal expected category name {category}'



# @pytest.mark.negative
# class TestProductsClientReadNegative(TestFakeStore):
#
#     @pytest.mark.parametrize("product_id", [-1,"1",1.0,9999999, "one"])
#     def test_get_product_with_incorrect_id(self, products_client):
#         response = products_client.get_product("")
#
#         assert response.status_code == 200, f"Expected status code 404, got {response.status_code}"
#         assert response.json() is None
#
#     @pytest.mark.parametrize("fake_category", ["films", "random"])
#     def test_get_product_by_nonexistent_category(self, products_client, fake_category):
#         response = products_client.get_products_by_category(fake_category)
#
#         assert response.status_code == 404
#
#     @pytest.mark.parametrize("limit", (-100, 500, "two"))
#     def test_get_products_by_limit(self, products_client, limit):
#         response = products_client.get_all_products(limit=limit)
#         assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
#         products_amount = len(response.json())
#         assert products_amount == limit, f"Expected amount of products is {limit}, got {products_amount} instead"