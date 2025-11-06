import pytest
import requests
import allure
from data import Url, ResponseMessages


class TestCreateUser:

    @allure.title("Проверка создания пользователя")
    @allure.description("Проверяется, что при передаче соответствующих требованиям данных, пользователь успешно создается. По окончанию проверки задействуется код очистки данных.")
    def test_successful_creation_user(self, register_new_user, cleanup_user):
        payload = register_new_user
        with allure.step(f"Отправить POST-запрос на создание курьера по адресу {Url.MAIN_URL}{Url.CREATE_USER} с почтой '{payload['email']}'"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.CREATE_USER}',
                json=payload
            )
        with allure.step("Проверить код ответа 200 и тело ответа 'success: true'"):
            assert response.status_code == 200
            assert response.json()['success'] == ResponseMessages.USER_CREATED_SUCCESS
        cleanup_user(payload)

    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    @allure.description("Проверяется, что при использовании данных уже созданного ранее пользователя, система не даст создать его повторно.")
    def test_repeated_creation_user(self, setup_user_for_cleanup):
        payload = setup_user_for_cleanup
        with allure.step(f"Отправить повторный POST-запрос на создание пользователя по адресу {Url.MAIN_URL}{Url.CREATE_USER} с почтой '{payload['email']}'"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.CREATE_USER}',
                json=setup_user_for_cleanup
            )
        with allure.step("Проверить код ответа 403 и сообщение об ошибке"):
            assert response.status_code == 403
            assert response.json()['message'] == ResponseMessages.USER_LOGIN_ALREADY

    @allure.title("Проверка создания пользователя без заполнения одного из обязательных полей (почта/пароль/имя)")
    @allure.description("Проверяется, что при отсутствии обязательного поля (почта/пароль/имя), система возвращает код 403.")
    @pytest.mark.parametrize("missing_field, default_value", [("email", "test_email"), ("password", "test_pass"), ("name", "test_name")])
    def test_creation_user_without_required_fields(self, register_new_user, missing_field, default_value):
        payload = register_new_user
        payload.pop(missing_field, default_value)
        with allure.step(f"Отправить POST-запрос на создание пользователя по адресу {Url.MAIN_URL}{Url.CREATE_USER} без поля '{missing_field}'"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.CREATE_USER}',
                json=payload
            )
        with allure.step("Проверить код ответа 403 и сообщение об ошибке"):
            assert response.status_code == 403
            assert response.json()['message'] == ResponseMessages.USER_NOT_ENOUGH_DATA
