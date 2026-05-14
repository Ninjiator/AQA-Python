import requests


class ApiClient:
    def __init__(self, base_url : str, timeout : tuple[float, float] = (3, 10) ) -> None:
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = timeout

    def get(self, endpoint : str, **kwargs):
        self.session.get(f"{self.base_url}/{endpoint}", timeout=self.timeout,  **kwargs)

    def post(self, endpoint: str, **kwargs):
        self.session.post(f"{self.base_url}/{endpoint}", timeout=self.timeout, **kwargs)

    def put(self, endpoint : str, **kwargs):
        self.session.put(f"{self.base_url}/{endpoint}", timeout=self.timeout,  **kwargs)

    def patch(self, endpoint : str, **kwargs):
        self.session.get(f"{self.base_url}/{endpoint}", timeout=self.timeout,  **kwargs)

    def delete(self, endpoint : str, **kwargs):
        self.session.get(f"{self.base_url}/{endpoint}", timeout=self.timeout,  **kwargs)
