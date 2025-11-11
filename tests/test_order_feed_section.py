import pytest
import allure
from locators.order_feed_section_locators import OrderFeedSectionLocators


class TestOrderFeedSectionPage:

    @allure.title("Проверка увеличения счетчика 'Выполнено за все время' при создании нового заказа")
    @allure.description("При создании нового заказа счетчик 'Выполнено за все время' должен увеличиться")
    def test_total_orders_counter_increases_after_order_creation(self, main_page, order_page, registered_user):
        with allure.step("Получить данные зарегистрированного пользователя"):
            user_data = registered_user

        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open_main_page()
            order_page.login_user_via_ui(user_data["email"], user_data["password"])
            assert main_page.is_constructor_header_displayed()

        with allure.step("Перейти в ленту заказов и сохранить начальные значения счетчиков"):
            main_page.open_feed_page()
            initial_total = order_page.get_total_orders_count()
            initial_today = order_page.get_today_orders_count()

        with allure.step("Вернуться в конструктор и добавить ингредиенты"):
            main_page.click_constructor_button()
            main_page.add_ingredient_to_constructor()
            assert main_page.is_ingredient_counter_equal_to(2)

        with allure.step("Создать заказ и дождаться окна заказа"):
            order_page.create_order()
            order_page.wait_for_order_window()

        with allure.step("Закрыть окно заказа"):
            order_page.close_order_window()

        with allure.step("Перейти в ленту заказов и дождаться обновления счетчиков"):
            main_page.open_feed_page()
            order_page.wait_for_counters_update(initial_total, initial_today)

        with allure.step("Проверить увеличение счетчика 'Выполнено за все время'"):
            final_total = order_page.get_total_orders_count()
            assert final_total > initial_total

    @allure.title("Проверка увеличения счетчика 'Выполнено за сегодня' при создании нового заказа")
    @allure.description("При создании нового заказа счетчик 'Выполнено за сегодня' должен увеличиться")
    def test_today_orders_counter_increases_after_order_creation(self, main_page, order_page, registered_user):
        with allure.step("Получить данные зарегистрированного пользователя"):
            user_data = registered_user

        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open_main_page()
            order_page.login_user_via_ui(user_data["email"], user_data["password"])
            assert main_page.is_constructor_header_displayed()

        with allure.step("Перейти в ленту заказов и сохранить начальные значения счетчиков"):
            main_page.open_feed_page()
            initial_total = order_page.get_total_orders_count()
            initial_today = order_page.get_today_orders_count()

        with allure.step("Вернуться в конструктор и добавить ингредиенты"):
            main_page.click_constructor_button()
            main_page.add_ingredient_to_constructor()
            assert main_page.is_ingredient_counter_equal_to(2)

        with allure.step("Создать заказ и дождаться окна заказа"):
            order_page.create_order()
            order_page.wait_for_order_window()

        with allure.step("Закрыть окно заказа"):
            order_page.close_order_window()

        with allure.step("Перейти в ленту заказов и дождаться обновления счетчиков"):
            main_page.open_feed_page()
            order_page.wait_for_counters_update(initial_total, initial_today)

        with allure.step("Проверить увеличение счетчика 'Выполнено за сегодня'"):
            final_today = order_page.get_today_orders_count()
            assert final_today > initial_today

    @allure.title("Проверка появления номера заказа в разделе 'В работе'")
    def test_order_appears_in_progress_section(self, main_page, order_page, registered_user):
        with allure.step("Получить данные зарегистрированного пользователя"):
            user_data = registered_user

        with allure.step("Открыть главную страницу и авторизоваться"):
            main_page.open_main_page()
            order_page.login_user_via_ui(user_data["email"], user_data["password"])
            assert main_page.is_constructor_header_displayed()

        with allure.step("Добавить ингредиенты в конструктор"):
            main_page.add_ingredient_to_constructor()
            assert main_page.is_ingredient_counter_equal_to(2)

        with allure.step("Создать заказ и дождаться окна заказа"):
            order_page.create_order()
            order_page.wait_for_order_window()

        with allure.step("Закрыть окно заказа"):
            order_page.close_order_window()

        with allure.step("Перейти в ленту заказов"):
            main_page.open_feed_page()

        with allure.step("Получить номер заказа в работе"):
            order_page.wait_for_element_visible(OrderFeedSectionLocators.ORDER_IN_PROGRESS)
            order_id = order_page.get_order_id_in_progress()
            allure.attach(f"Номер заказа в работе: {order_id}", name="Order ID in Progress")
            assert order_id > 0, "Номер заказа не получен или равен 0"
