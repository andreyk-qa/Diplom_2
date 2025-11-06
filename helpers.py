import requests
import random
import string
from data import Url


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def get_user_access_token(payload):
    try:
        login_response = requests.post(
            f'{Url.MAIN_URL}{Url.LOGIN_USER}',
            json={"email": payload["email"], "password": payload["password"], "name": payload["name"]},
        )
        if login_response.status_code == 200 and "accessToken" in login_response.json():
            return login_response.json()["accessToken"]
    except Exception:
        return None
    return None

def delete_user(access_token):
    if access_token:
        requests.delete(f'{Url.MAIN_URL}{Url.USER}')
