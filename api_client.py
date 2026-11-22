import requests


class CourierAPIClient:
    def __init__(self, base_url, auth_token):
        # Принимаю base_url и auth_token через конструктор — 
        # так их легко подменить в тестах и не зависеть от глобальных переменных.
        self.base_url = base_url
        self.auth_token = auth_token

    def _get_auth_header(self):
        # Выношу формирование заголовка в отдельный приватный метод, 
        # чтобы не дублировать код в трёх методах.
        if not self.auth_token:
            raise ValueError("AUTH_TOKEN не задан")
        return {"Authorization": f"Bearer {self.auth_token}"}

    def get_courier_by_id(self, courier_id):
        url = f"{self.base_url}/couriers/{courier_id}"
        headers = self._get_auth_header()
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()

    def create_courier(self, data):
        url = f"{self.base_url}/couriers"
        headers = self._get_auth_header()
        headers["Content-Type"] = "application/json"
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete_courier(self, courier_id):
        url = f"{self.base_url}/couriers/{courier_id}"
        headers = self._get_auth_header()
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()