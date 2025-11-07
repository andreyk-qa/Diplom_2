import pytest
import requests
import allure
from data import Url, ResponseMessages


class TestLoginUser:

    @allure.title("Проверка авторизации пользователя")
    @allure.description("Проверяется, что при передаче данных зарегистрированного пользователя, пользователь успешно авторизуется. По окончанию проверки задействуется код очистки данных.")
    def test_successful_authorization_user(self, setup_user_for_cleanup):
        payload, _ = setup_user_for_cleanup
        with allure.step(f"Отправить POST-запрос на авторизацию пользователя по адресу {Url.MAIN_URL}{Url.LOGIN_USER} с почтой '{payload['email']}' и паролем"):
            response_auth = requests.post(
                f'{Url.MAIN_URL}{Url.LOGIN_USER}',
                json={"email": payload["email"], "password": payload["password"]}
            )
        with allure.step("Проверить код ответа 200 и тело ответа 'success: true'"):
            assert response_auth.status_code == 200
            assert response_auth.json()['success'] == ResponseMessages.USER_LOGIN_SUCCESS

    @allure.title("Проверка авторизации пользователя с указанием неправильного обязательного поля (почта/пароль)")
    @allure.description(
        "Проверяется, что при передаче неверного обязательного поля (почта/пароль), система возвращает код 401.")
    @pytest.mark.parametrize("wrong_field", ["email", "password"])
    def test_authorization_user_with_wrong_required_fields(self, setup_user_for_cleanup, wrong_field):
        payload, _ = setup_user_for_cleanup
        auth_data = {
            "email": payload["email"],
            "password": payload["password"]
        }
        auth_data[wrong_field] += "w"
        with allure.step(
                f"Отправить POST-запрос на авторизацию пользователя по адресу {Url.MAIN_URL}{Url.LOGIN_USER} с неверным полем '{wrong_field}'"):
            response_auth = requests.post(
                f'{Url.MAIN_URL}{Url.LOGIN_USER}',
                json=auth_data
            )
        with allure.step("Проверить код ответа 401 и сообщение об ошибке"):
            assert response_auth.status_code == 401
            assert response_auth.json()['message'] == ResponseMessages.USER_DATA_INCORRECT
