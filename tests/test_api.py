from __future__ import annotations
import allure
import pytest
from utils.fakers import random_number, random_string, random_email


@allure.feature('Work with users API')
class TestUsersAPI:

    @allure.title('GET LIST USERS from page {page}')
    @pytest.mark.parametrize('page', [random_number(1, 2), random_number(3, 100)])
    def test_get_list_users(self, users_api, page: int):
        with allure.step(f"Send GET-request to get list of users from page {page}"):
            list_users = users_api.list_users(page)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_list_users(list_users)

    @allure.title('GET SINGLE USER with id {user_id}')
    @pytest.mark.parametrize('user_id', [random_number(1, 12), random_number(13, 100)])
    def test_get_single_user_with_api(self, users_api, user_id: int):
        with allure.step(f"Send GET-request to get user's data with id {user_id}"):
            single_user = users_api.single_users(user_id)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_single_users(single_user, user_id)

    @allure.title('CREATE USER {name}')
    @pytest.mark.parametrize('name, job', [(random_string(6, 10), random_string(6, 10)), (random_string(6, 10), None),
                                           (None, random_string(6, 10)), (None, None)])
    def test_create_user_with_api(self, users_api, name: str, job: str):
        with allure.step("Send POST-request to create user"):
            create_user = users_api.create_user(name, job)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_create_user(create_user, name, job)

    @allure.title('UPDATE USER with id {user_id} with method {method}')
    @pytest.mark.parametrize('user_id, method, name, job',
                             [(random_number(1, 10), "PUT", random_string(6, 10), random_string(10, 15)),
                              (random_number(1, 10), "PATCH", random_string(6, 10), random_string(10, 15))])
    def test_update_user_with_api(self, users_api, user_id: int, method: str, name: str, job: str):
        with allure.step(f"Send {method}-request to update user's data"):
            update_user = users_api.update_user(method, user_id, name, job)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_update_user(update_user)

    @allure.title('DELETE USER with id {user_id}')
    @pytest.mark.parametrize('user_id', [random_number(1, 10)])
    def test_delete_user_with_api(self, users_api, user_id: int):
        with allure.step(f"Send DELETE-request to delete user with id {user_id}"):
            delete_user = users_api.delete_user(user_id)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_delete_user(delete_user)

    @allure.title('REGISTER USER with email {email} and password {password}')
    @pytest.mark.parametrize('email, password', [("eve.holt@reqres.in", random_string(8, 10)), (random_email(), None),
                                                 (None, random_string(8, 10)), (None, None)])
    def test_register_user_with_api(self, users_api, email: str | None, password: str | None):
        with allure.step("Send POST-request to register user"):
            register_user = users_api.register_user(email, password)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_register_user(register_user, email,
                                                                                          password)

    @allure.title('LOGIN USER with email {email} and password {password}')
    @pytest.mark.parametrize('email, password', [("eve.holt@reqres.in", random_string(8, 10)), (random_email(), None),
                                                 (None, random_string(8, 10)), (None, None)])
    def test_login_user_with_api(self, users_api, email: str | None, password: str | None):
        with allure.step("Send POST-request to login user"):
            login_user = users_api.login_user(email, password)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_login_user(login_user, email, password)

    @pytest.mark.parametrize('delay', [random_number(5, 10)])
    @allure.title('DELAYED RESPONSE {delay}')
    def test_delayed_response_with_api(self, users_api, delay: int):
        with allure.step(f"Send GET-request to get list of users with delay {delay}"):
            get_list_users_with_delay = users_api.delayed_response(delay)

        with allure.step("Check correct status-code and body of answer"):
            users_api.should_be_valid_response_status_and_body_from_request_list_users(get_list_users_with_delay)
