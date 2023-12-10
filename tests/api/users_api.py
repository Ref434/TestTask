from __future__ import annotations

import json
from typing import NoReturn

from tests.baseclasses.response import Response
from utils.global_enums import APIPoint
from utils.pydantic_schemas.user import (DefaultRegister, DefaultLogin, DefaultUpdateUser,
                                         DefaultListUsers, DefaultSingleUser, DefaultCreateUser,
                                         DefaultCreateUserWithoutJob, DefaultCreateUserWithoutData,
                                         DefaultCreateUserWithoutName)


class UsersAPI:

    def __init__(self, api_reqres) -> None:
        self.api_reqres = api_reqres

    def list_users(self, page: int) -> Response:
        response = self.api_reqres.get_request(APIPoint.LIST_USERS, params={'page': page})
        return Response(response)

    def single_users(self, user_id: int) -> Response:
        response = self.api_reqres.get_request(f"{APIPoint.SINGLE_USER}{user_id}")
        return Response(response)

    def create_user(self, name: str, job: str) -> Response:
        response = self.api_reqres.post_request(APIPoint.CREATE_USER, data=json.dumps({"name": name, "job": job}),
                                                headers={'Content-Type': 'application/json'})
        return Response(response)

    def update_user(self, method: str, user_id: int, name: str, job: str) -> Response:
        if method == "PUT":
            response = self.api_reqres.put_request(f"{APIPoint.EDIT_USER}{user_id}",
                                                   data=json.dumps({"name": name, "job": job}),
                                                   headers={'Content-Type': 'application/json'})
        else:
            response = self.api_reqres.patch_request(f"{APIPoint.EDIT_USER}{user_id}",
                                                     data=json.dumps({"name": name, "job": job}),
                                                     headers={'Content-Type': 'application/json'})
        return Response(response)

    def delete_user(self, user_id: int) -> Response:
        response = self.api_reqres.delete_request(f"{APIPoint.EDIT_USER}{user_id}")
        return Response(response)

    def register_user(self, email: str | None, password: str | None) -> Response:
        if email is None and password is not None:
            payload = json.dumps({"password": password})
        elif email is not None and password is None:
            payload = json.dumps({"email": email})
        else:
            payload = json.dumps({"email": email, "password": password})
        response = self.api_reqres.post_request(APIPoint.REGISTER, data=payload,
                                                headers={'Content-Type': 'application/json'})
        return Response(response)

    def login_user(self, email: str | None, password: str | None) -> Response:
        if email is None and password is not None:
            payload = json.dumps({"password": password})
        elif email is not None and password is None:
            payload = json.dumps({"email": email})
        else:
            payload = json.dumps({"email": email, "password": password})
        response = self.api_reqres.post_request(APIPoint.LOGIN, data=payload,
                                                headers={'Content-Type': 'application/json'})
        return Response(response)

    def delayed_response(self, delay: int) -> Response:
        response = self.api_reqres.get_request(APIPoint.DELAYED, params={'delay': delay})
        return Response(response)

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_list_users(list_users) -> NoReturn:
        assert list_users.response_status == 200
        list_users.validate(DefaultListUsers)

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_single_users(single_user, user_id: int) -> NoReturn:
        if user_id <= 12:
            assert single_user.response_status == 200
            single_user.validate(DefaultSingleUser)
        else:
            assert single_user.response_status == 404

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_create_user(create_user, name: str | None,
                                                                          job: str | None) -> NoReturn:
        assert create_user.response_status == 201
        if name is None and job is None:
            create_user.validate(DefaultCreateUserWithoutData)
        elif name is None and job is not None:
            create_user.validate(DefaultCreateUserWithoutName)
        elif name is not None and job is None:
            create_user.validate(DefaultCreateUserWithoutJob)
        else:
            create_user.validate(DefaultCreateUser)

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_update_user(update_user) -> NoReturn:
        assert update_user.response_status == 200
        update_user.validate(DefaultUpdateUser)

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_delete_user(delete_user) -> NoReturn:
        assert delete_user.response_status == 204

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_register_user(register_user, email: str | None,
                                                                            password: str | None) -> NoReturn:
        if email is None or password is None:
            assert register_user.response_status == 400
            assert register_user.response_json["error"] == "Missing password" or register_user.response_json[
                "error"] == "Missing email or username"
        else:
            assert register_user.response_status == 200
            register_user.validate(DefaultRegister)

    @staticmethod
    def should_be_valid_response_status_and_body_from_request_login_user(login_user, email: str | None,
                                                                         password: str | None) -> NoReturn:
        if email is None or password is None:
            assert login_user.response_status == 400
            assert login_user.response_json["error"] == "Missing password" or login_user.response_json[
                "error"] == "Missing email or username"
        else:
            assert login_user.response_status == 200
            login_user.validate(DefaultLogin)
