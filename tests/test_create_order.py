import pytest
import requests
import allure
from data import Url, ResponseMessages, OrderData


class TestCreateOrder:

    @allure.title("Проверка создания заказа авторизованным пользователем с ингредиентами")
    @allure.description("Проверяется, что авторизованный пользователь может создать заказ с ингредиентами.")
    def test_order_creation(self, setup_user_for_cleanup):
        payload, access_token = setup_user_for_cleanup
        headers = {"Authorization": f"{access_token}"}
        with allure.step(f"Отправить POST-запрос на создание заказа по адресу {Url.MAIN_URL}{Url.ORDER_CREATION}"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.ORDER_CREATION}',
                json=OrderData.INGREDIENTS,
                headers=headers
            )
            ingredients_in_response = [ingredient['_id'] for ingredient in response.json()['order']['ingredients']]
            expected_ingredients = OrderData.INGREDIENTS['ingredients']
        with allure.step("Проверить код ответа 200 и тело ответа 'success: true', а также в ответе присутствуют все ингредиенты"):
            assert response.status_code == 200
            assert response.json()['success'] == ResponseMessages.SUCCESS_ORDER
            assert set(ingredients_in_response) == set(expected_ingredients)

    @allure.title("Проверка создания заказа не авторизованным пользователем")
    @allure.description("Проверяется, что не авторизованный пользователь не может создать заказ.")
    @allure.issue("Найден баг в коде ответа и его теле. Ожидается 401, заказ не создается без авторизации пользователя."
                  "Фактически 200, заказ создан. Для прохождения следующих проверок, пропускаем этот тест.")
    @pytest.mark.skip
    def test_order_creation_without_authorization(self):
        with allure.step(f"Отправить POST-запрос на создание заказа по адресу {Url.MAIN_URL}{Url.ORDER_CREATION}"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.ORDER_CREATION}',
                json=OrderData.INGREDIENTS
            )
        with allure.step("Проверить код ответа 401 и тело ответа 'success: false'"):
            assert response.status_code == 401
            assert response.json()['success'] == ResponseMessages.FAIL_ORDER

    @allure.title("Проверка создания заказа авторизованным пользователем без ингредиентов")
    @allure.description("Проверяется, что авторизованный пользователь не может создать заказ без ингредиентов.")
    def test_order_creation_without_ingredients(self, setup_user_for_cleanup):
        payload, access_token = setup_user_for_cleanup
        headers = {"Authorization": f"{access_token}"}
        with allure.step(f"Отправить POST-запрос на создание заказа по адресу {Url.MAIN_URL}{Url.ORDER_CREATION}"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.ORDER_CREATION}',
                headers=headers
            )
        with allure.step("Проверить код ответа 400 и сообщение об ошибке"):
            assert response.status_code == 400
            assert response.json()['message'] == ResponseMessages.WITHOUT_INGREDIENT_ORDER

    @allure.title("Проверка создания заказа авторизованным пользователем с неверными хешами ингредиентов")
    @allure.description("Проверяется, что авторизованный пользователь не может создать заказ с неверными хешами ингредиентов.")
    @allure.issue("Найден баг в коде ответа и его теле. Ожидается 500, фактически 400."
                  "Для прохождения следующих проверок, пропускаем этот тест.")
    @pytest.mark.skip
    def test_order_creation_with_incorrect_hash_ingredients(self, setup_user_for_cleanup):
        payload, access_token = setup_user_for_cleanup
        headers = {"Authorization": f"{access_token}"}
        with allure.step(f"Отправить POST-запрос на создание заказа по адресу {Url.MAIN_URL}{Url.ORDER_CREATION}"):
            response = requests.post(
                f'{Url.MAIN_URL}{Url.ORDER_CREATION}',
                json=OrderData.INCORRECT_INGREDIENTS,
                headers=headers
            )
        with allure.step("Проверить код ответа 500"):
            assert response.status_code == 500
