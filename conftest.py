import pytest
import requests
from data import Url
from helpers import generate_random_string, get_user_access_token, delete_user


@pytest.fixture
def register_new_user():
    payload = {
        "email": f"{generate_random_string(10)}@yandex.ru",
        "password": generate_random_string(10),
        "name": generate_random_string(10)
    }
    return payload

@pytest.fixture
def cleanup_user(request):
    users_to_delete = []
    def finalizer():
        for payload in users_to_delete:
            user_token = get_user_access_token(payload)
            delete_user(user_token)
    request.addfinalizer(finalizer)
    def _register_for_cleanup(payload):
        users_to_delete.append(payload)
    return _register_for_cleanup

@pytest.fixture
def setup_user_for_cleanup(register_new_user):
    payload = register_new_user
    user_token = None
    requests.post(f'{Url.MAIN_URL}{Url.CREATE_USER}', json=payload)
    try:
        user_token = get_user_access_token(payload)
        yield payload
    finally:
        delete_user(user_token)
