from .base_page import BasePage
from locators.main_functionality_locators import MainFunctionalityLocators
from locators.order_feed_section_locators import OrderFeedSectionLocators
from data import Url
import allure


class MainFunctionalityPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self._open_url(Url.MAIN_PAGE_URL)
        self.wait_for_page_loaded()

    @allure.step("Открыть страницу 'Лента заказов'")
    def open_feed_page(self):
        self._open_url(Url.MAIN_PAGE_URL + Url.FEED_PAGE_URL)

    @allure.step("Кликнуть кнопку 'Лента Заказов' вверху страницы")
    def click_order_feed_button(self):
        self._click(MainFunctionalityLocators.ORDER_FEED_BUTTON)

    @allure.step("Кликнуть кнопку 'Конструктор' вверху страницы")
    def click_constructor_button(self):
        self._click(MainFunctionalityLocators.CONSTRUCTOR_BUTTON)

    @allure.step("Кликнуть на ингредиент 'Краторная булка N-200i' в конструкторе")
    def click_ingredient_button(self):
        self._click(MainFunctionalityLocators.INGREDIENT_BUTTON)

    @allure.step("Кликнуть по крестику всплывающего окна")
    def click_close_button(self):
        self._click(MainFunctionalityLocators.CLOSE_DETAILS_BUTTON)

    @allure.step("Проверить, что произошел успешный переход на страницу 'Лента Заказов'")
    def is_feed_header_displayed(self):
        try:
            self._is_visible(MainFunctionalityLocators.ORDER_FEED)
            return True
        except:
            return False

    @allure.step("Проверить, что произошел успешный переход на страницу 'Конструктор'")
    def is_constructor_header_displayed(self):
        try:
            self._is_visible(MainFunctionalityLocators.ASSEMBLE_BURGER)
            return True
        except:
            return False

    @allure.step("Проверить, что появилось всплывающее окно с деталями ингредиента")
    def is_ingredient_details_displayed(self):
        try:
            self._is_visible(MainFunctionalityLocators.INGREDIENT_DETAILS)
            return True
        except:
            return False

    @allure.step("Проверить, что всплывающее окно с деталями ингредиента не отображается")
    def is_ingredient_details_not_displayed(self):
        try:
            self._is_not_visible(MainFunctionalityLocators.INGREDIENT_DETAILS)
            return True
        except:
            return False

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        self._drag_and_drop(
            MainFunctionalityLocators.INGREDIENT_BUTTON,
            OrderFeedSectionLocators.BURGER_CONSTRUCTOR_BASKET
        )

    @allure.step("Получить текущее значение счетчика ингредиента")
    def get_ingredient_counter_value(self):
        try:
            counters = self.driver.find_elements(*MainFunctionalityLocators.COUNTER_INGREDIENT)

            for counter in counters:
                text = counter.text.strip()
                if text == '2':
                    return 2

            for counter in counters:
                text = counter.text.strip()
                if text.isdigit() and int(text) > 0:
                    return int(text)

            return 0

        except Exception:
            return 0

    @allure.step("Проверить, что счетчик ингредиента увеличился")
    def is_ingredient_counter_increased(self, initial_value):
        current_value = self.get_ingredient_counter_value()
        return current_value > initial_value

    @allure.step("Проверить, что счетчик ингредиента равен {expected_value}")
    def is_ingredient_counter_equal_to(self, expected_value):
        current_value = self.get_ingredient_counter_value()
        return current_value == expected_value

    @allure.step("Получить начальное значение счетчика перед добавлением ингредиента")
    def get_initial_counter_value(self):
        return self.get_ingredient_counter_value()

    @allure.step("Дождаться обновления счетчика ингредиента до значения {expected_value}")
    def wait_for_ingredient_counter_update(self, expected_value, timeout=10):
        def counter_updated(driver):
            try:
                current_value = self.get_ingredient_counter_value()
                return current_value == expected_value
            except Exception:
                return False
        self.wait.until(counter_updated)
