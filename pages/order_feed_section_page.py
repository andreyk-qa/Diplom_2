from .base_page import BasePage
from locators.main_functionality_locators import MainFunctionalityLocators
from locators.order_feed_section_locators import OrderFeedSectionLocators
import allure


class OrderFeedSectionPage(BasePage):

    @allure.step("Авторизовать пользователя через UI")
    def login_user_via_ui(self, email, password):
        self._click(MainFunctionalityLocators.LOGIN_ACCOUNT_BUTTON)
        self._send_keys(MainFunctionalityLocators.EMAIL_INPUT, email)
        self._send_keys(MainFunctionalityLocators.PASSWORD_INPUT, password)
        self._click(MainFunctionalityLocators.LOGIN_BUTTON)

    @allure.step("Нажать на кнопку 'Оформить заказ'")
    def create_order(self):
        self._click(OrderFeedSectionLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получить значение счетчика 'Выполнено за все время'")
    def get_total_orders_count(self):
        count_text = self._get_text(OrderFeedSectionLocators.TOTAL_ORDERS)
        return int(count_text)

    @allure.step("Получить значение счетчика 'Выполнено за сегодня'")
    def get_today_orders_count(self):
        count_text = self._get_text(OrderFeedSectionLocators.TODAY_ORDERS)
        return int(count_text)

    @allure.step("Получить значение идентификатора заказа")
    def get_order_id(self):
        order_id = self._get_text(OrderFeedSectionLocators.ORDER_ID)
        return int(order_id)

    @allure.step("Получить значение идентификатора заказа в работе")
    def get_order_id_in_progress(self):
        order_id = self._get_text(OrderFeedSectionLocators.ORDER_IN_PROGRESS)
        return int(order_id)

    @allure.step("Дождаться появления окна заказа")
    def wait_for_order_window(self, timeout=15):
        self.wait_for_element_visible(OrderFeedSectionLocators.ORDER_MODAL, timeout)

    @allure.step("Дождаться успешного создания заказа")
    def wait_for_order_success(self, timeout=15):
        self.wait_for_element_visible(OrderFeedSectionLocators.ORDER_SUCCESS_MODAL, timeout)

    @allure.step("Закрыть окно заказа")
    def close_order_window(self):
        close_button = self.wait_for_element_visible(OrderFeedSectionLocators.ORDER_MODAL_CLOSE)
        self.driver.execute_script("arguments[0].click();", close_button)

    @allure.step("Дождаться обновления счетчиков заказов")
    def wait_for_counters_update(self, initial_total, initial_today, timeout=30):
        def counters_updated(driver):
            try:
                current_total = self.get_total_orders_count()
                current_today = self.get_today_orders_count()
                return current_total > initial_total or current_today > initial_today
            except:
                return False
        self.wait.until(counters_updated)