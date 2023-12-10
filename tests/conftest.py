import allure
import pytest
import requests

from tests.api.users_api import UsersAPI
from requests import Response
class ApiClient:

    def __init__(self, base_address) -> None:
        self.base_address: str = base_address

    @allure.step('Making GET request to "{path}"')
    def get_request(self, path="/", params=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.get(url=url, params=params, headers=headers)

    @allure.step('Making POST request to "{path}"')
    def post_request(self, path="/", params=None, data=None, json=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.post(url=url, params=params, data=data, json=json, headers=headers)

    @allure.step('Making DELETE request to "{path}"')
    def delete_request(self, path="/", params=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.delete(url=url, params=params, headers=headers)

    @allure.step('Making PUT request to "{path}"')
    def put_request(self, path="/", params=None, data=None, json=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.put(url=url, params=params, data=data, json=json, headers=headers)

    @allure.step('Making PATCH request to "{path}"')
    def patch_request(self, path="/", params=None, data=None, json=None, headers=None) -> Response:
        url: str = f"{self.base_address}{path}"
        return requests.patch(url=url, params=params, data=data, json=json, headers=headers)


@pytest.fixture
def api_reqres() -> ApiClient:
    return ApiClient(base_address="https://reqres.in/")

@pytest.fixture
def users_api(api_reqres) -> UsersAPI:
    return UsersAPI(api_reqres)

