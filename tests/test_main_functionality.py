import pytest
import allure


class TestMainFunctionality:

    @allure.title("Проверка перехода по клику на 'Конструктор'")
    def test_navigate_to_constructor(self, main_page):
        with allure.step("Открыть страницу Лента заказов"):
            main_page.open_feed_page()

        with allure.step("Кликнуть на кнопку 'Конструктор'"):
            main_page.click_constructor_button()

        with allure.step("Проверить, что произошел переход на страницу 'Конструктор'"):
            assert main_page.is_constructor_header_displayed()

    @allure.title("Проверка перехода по клику на 'Лента Заказов'")
    def test_navigate_to_order_feed(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликнуть на кнопку 'Лента Заказов'"):
            main_page.click_order_feed_button()

        with allure.step("Проверить, что произошел переход на страницу 'Лента Заказов'"):
            assert main_page.is_feed_header_displayed()

    @allure.title("Проверка отображения деталей ингредиента при клике")
    def test_ingredient_details_displayed_on_click(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликнуть на ингредиент 'Краторная булка N-200i'"):
            main_page.click_ingredient_button()

        with allure.step("Проверить, что появилось всплывающее окно с деталями ингредиента"):
            assert main_page.is_ingredient_details_displayed()

    @allure.title("Проверка закрытия всплывающего окна с деталями ингредиента")
    def test_ingredient_details_closed_on_click(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Кликнуть на ингредиент 'Краторная булка N-200i'"):
            main_page.click_ingredient_button()

        with allure.step("Проверить, что окно с деталями отображается"):
            assert main_page.is_ingredient_details_displayed()

        with allure.step("Кликнуть по крестику всплывающего окна"):
            main_page.click_close_button()

        with allure.step("Проверить, что окно с деталями закрылось"):
            assert main_page.is_ingredient_details_not_displayed()

    @allure.title("Проверка увеличения счетчика ингредиента при добавлении в конструктор")
    @allure.description("При перетаскивании ингредиента в конструктор счетчик должен увеличиться с 0 до 2")
    def test_ingredient_counter_increases_when_added_to_constructor(self, main_page):
        with allure.step("Открыть главную страницу"):
            main_page.open_main_page()

        with allure.step("Получить начальное значение счетчика ингредиента"):
            initial_counter = main_page.get_ingredient_counter_value()
            allure.attach(f"Начальное значение счетчика: {initial_counter}", name="Initial Counter")

        with allure.step("Добавить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor()

        with allure.step("Дождаться обновления счетчика ингредиента"):
            main_page.wait_for_ingredient_counter_update(expected_value=2, timeout=10)

        with allure.step("Получить значение счетчика после добавления"):
            final_counter = main_page.get_ingredient_counter_value()
            allure.attach(f"Конечное значение счетчика: {final_counter}", name="Final Counter")

        with allure.step("Проверить, что счетчик увеличился"):
            assert final_counter > initial_counter

        with allure.step("Проверить, что счетчик равен 2"):
            assert final_counter == 2
