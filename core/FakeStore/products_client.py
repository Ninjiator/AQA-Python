from core.api_client import ApiClient


class ProductsClient:
    def __init__(self, api_client : ApiClient) -> None:
        self.api = api_client

    def get_all_products(self):
        return self.api.get("/products")

    def get_product(self, product_id):
        return self.api.get(f"/products/{product_id}")

    def add_new_product(self, product_payload):
        return self.api.post("/products", json = product_payload)

    def update_product(self, product_id, product_payload):
        return self.api.put(f"/products/{product_id}", json = product_payload)

    def delete_product(self, product_id):
        return self.api.delete(f"/products/{product_id}")