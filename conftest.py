import pytest
import requests
from selenium import webdriver
from data import Url
from helpers import generate_random_string, get_user_access_token, delete_user
from pages.main_functionality_page import MainFunctionalityPage
from pages.order_feed_section_page import OrderFeedSectionPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска тестов: chrome или firefox"
    )


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = None

    if browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
    else:
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)

    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainFunctionalityPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderFeedSectionPage(driver)


@pytest.fixture
def registered_user():
    payload = {
        "email": f"{generate_random_string(10)}@yandex.ru",
        "password": generate_random_string(10),
        "name": generate_random_string(10)
    }
    response = requests.post(
        f'{Url.MAIN_PAGE_URL}{Url.CREATE_USER}',
        json=payload
    )
    access_token = None
    if response.status_code == 200:
        access_token = get_user_access_token(payload)
    user_data = {
        "email": payload["email"],
        "password": payload["password"],
        "name": payload["name"],
        "access_token": access_token
    }
    yield user_data
    if access_token:
        delete_user(access_token)