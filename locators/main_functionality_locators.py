from selenium.webdriver.common.by import By


class MainFunctionalityLocators:

    CONSTRUCTOR_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Конструктор']]")
    ORDER_FEED_BUTTON = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link') and .//p[text()='Лента Заказов']]")
    INGREDIENT_BUTTON = (By.XPATH, ".//p[contains(text(), 'Краторная булка N-200i')]")
    CLOSE_DETAILS_BUTTON = (By.CSS_SELECTOR, "button[class*='Modal_modal__close_modified__']")
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти')]")
    COUNTER_INGREDIENT = (By.XPATH, "//p[contains(@class, 'counter_counter__num__')]")
    ASSEMBLE_BURGER = (By.XPATH, ".//h1[contains(text(), 'Соберите бургер')]")
    ORDER_FEED = (By.XPATH, ".//h1[contains(text(), 'Лента заказов')]")
    INGREDIENT_DETAILS = (By.XPATH, ".//h2[contains(text(), 'Детали ингредиента')]")
    EMAIL_INPUT = (By.XPATH, ".//label[contains(text(), 'Email')]/../input")
    PASSWORD_INPUT = (By.XPATH, ".//label[contains(text(), 'Пароль')]/../input")
