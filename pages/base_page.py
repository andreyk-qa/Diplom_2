from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Открыть URL: {url}")
    def _open_url(self, url):
        self.driver.get(url)

    @allure.step("Найти элемент по локатору: {locator}")
    def _find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Кликнуть по элементу: {locator}")
    def _click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    @allure.step("Ввести текст '{text}' в поле: {locator}")
    def _send_keys(self, locator, text):
        element = self._find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текст элемента: {locator}")
    def _get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    @allure.step("Проверить, что элемент {locator} отображается")
    def _is_visible(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Проверить, что элемент {locator} не отображается")
    def _is_not_visible(self, locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Перетащить элемент {source_locator} на элемент {target_locator}")
    def _drag_and_drop(self, source_locator, target_locator):
        source_element = self.wait.until(EC.presence_of_element_located(source_locator))
        target_element = self.wait.until(EC.presence_of_element_located(target_locator))

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];

            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);

            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, source_element, target_element)

    @allure.step("Подождать появления элемента: {locator}")
    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Подождать исчезновения элемента: {locator}")
    def wait_for_element_invisible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_loaded(self, timeout=30):
        def page_loaded(driver):
            return driver.execute_script("return document.readyState") == "complete"
        self.wait.until(page_loaded)
