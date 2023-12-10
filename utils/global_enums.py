from enum import Enum


class APIPoint(str, Enum):
    LIST_USERS = 'api/users'
    SINGLE_USER = 'api/users/'
    CREATE_USER = 'api/users'
    EDIT_USER = 'api/users/'
    REGISTER = 'api/register'
    LOGIN = 'api/login'
    DELAYED = 'api/users'

    def __str__(self) -> str:
        return self.value
