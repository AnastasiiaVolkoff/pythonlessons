import requests
from config import BASE_URL, TOKEN


class YougileAPI:
    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }

    def _request(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        response = requests.request(
            method, url, json=data, headers=self.headers
        )
        return response.json()

    def create_project(self, title: str, users: list = None):
        payload = {"title": title}
        if users:
            payload["users"] = users
        return self._request("POST", "/projects", payload)

    def get_project(self, project_id: str):
        return self._request("GET", f"/projects/{project_id}")

    def update_project(self, project_id: str, data: dict):
        return self._request("PUT", f"/projects/{project_id}", data)

    def delete_project(self, project_id: str):
        return self._request("DELETE", f"/projects/{project_id}")
