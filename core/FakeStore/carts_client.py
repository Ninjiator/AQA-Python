from core.api_client import ApiClient


class CartsClient:
    def __init__(self, api_client : ApiClient):
        self.api = api_client

    def get_all_carts(self):
        return self.api.get("/carts")

    def get_cart(self, cart_id):
        return self.api.get(f"/carts/{cart_id}")

    def add_new_cart(self, cart_payload):
        return self.api.post("/carts", json = cart_payload)

    def update_cart(self, cart_id, cart_payload):
        return self.api.put(f"/carts/{cart_id}", json = cart_payload)

    def delete_cart(self, cart_id):
        return self.api.delete(f"/carts{cart_id}")
