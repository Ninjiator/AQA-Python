from core.api_client import ApiClient


class UsersClient:
    def __init__(self, api_client : ApiClient):
        self.api = api_client

    def get_all_users(self):
        return self.api.get("/users")

    def get_user(self, user_id):
        return self.api.get(f"/users/{user_id}")

    def add_new_user(self, user_payload):
        return self.api.post("/users", json = user_payload)

    def update_user(self, user_id, user_payload):
        return self.api.put(f"/users/{user_id}", json = user_payload)

    def delete_user(self, user_id):
        return self.api.delete(f"/users{user_id}")