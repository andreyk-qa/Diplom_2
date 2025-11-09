from selenium.webdriver.common.by import By


class OrderFeedSectionLocators:

    FLUORESCENT_BUN_R2_D3 = (By.CSS_SELECTOR, "a[href*='61_c0c5a71d1f82001bdaaa6d']")
    SAUCE_SPICY_X = (By.CSS_SELECTOR, "a[href*='61c0c5a71d1f82001bdaaa72']")
    BURGER_CONSTRUCTOR_BASKET = (By.CSS_SELECTOR, "[class*='BurgerConstructor_basket__list__']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Оформить заказ')]")
    TOTAL_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за все время:')]/../p[contains(@class, 'OrderFeed_number__')]")
    TODAY_ORDERS = (By.XPATH, "//p[contains(text(), 'Выполнено за сегодня:')]/../p[contains(@class, 'OrderFeed_number__')]")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady_')]//li[contains(@class, 'text_type_digits-default')]")
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__')]")
    ORDER_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__')]")
    ORDER_SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Modal_modal__')]//p[contains(text(), 'идентификатор')]")
    ORDER_MODAL_CLOSE = (By.XPATH, ".//div[contains(@class, 'Modal_modal__')]//button[contains(@class, 'Modal_modal__close_modified__')]")
