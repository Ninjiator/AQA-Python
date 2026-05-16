from requests import Response
from core.api_client import ApiClient


class ProductsClient:
    def __init__(self, api_client : ApiClient) -> None:
        self.api = api_client

    def get_all_products(self, limit = None, sort = None) -> Response:
        params = {}
        if sort is not None:
            params["sort"] = sort
        if limit is not None:
            params["limit"] = limit
        return self.api.get("/products", params=params)

    def get_all_categories(self) -> Response:
        return self.api.get("/products/categories")

    def get_product(self, product_id : int) -> Response:
        return self.api.get(f"/products/{product_id}")

    def get_products_by_category(self, category_name : str) -> Response:
        return self.api.get(f"/products/category/{category_name}")

    def add_new_product(self, product_payload : dict) -> Response:
        return self.api.post("/products", json = product_payload)

    def update_product(self, product_id : int, product_payload : dict) -> Response:
        return self.api.put(f"/products/{product_id}", json = product_payload)

    def delete_product(self, product_id : int) -> Response:
        return self.api.delete(f"/products/{product_id}")