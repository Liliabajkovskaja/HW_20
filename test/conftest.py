import logging
from time import time

import pytest
from pytest import fixture
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.login_page import LoginPage
from page_objects.products_page import ProductsPage
from utils.driver_factory import DriverFactory
from utils.config_manager import ROOT_PATH
from utils.config_manager import ConfigManager


logger = logging.getLogger()

def pytest_addoption(parser):
    parser.addoption(
        "--json", action="store_true", help="read json"
    )


@pytest.fixture
def json(request):

    return request.config.getoption("--json")


@fixture(scope='session')
def get_driver(request) -> WebDriver:

    if request.config.getoption("--json"):
        logger.info('Getting configs from json')
        from utils.config_manager_json import ConfigManager

    driver = DriverFactory(ConfigManager.browser).get_driver()
    yield driver
    driver.quit()


@fixture(autouse=True)
def make_screenshot_after_test(get_driver):
    yield
    get_driver.save_screenshot(f'{ROOT_PATH}/{time()}.png')


@fixture
def open_login_page(get_driver) -> WebDriver:
    get_driver.get(ConfigManager.url)
    # get_driver.maximize_window()
    return get_driver


@fixture
def get_logged_product_page(open_login_page, get_user_name, get_user_password) -> ProductsPage:

    try:
        return ProductsPage(open_login_page).find_shopping_cart(timeout=1)     # check if product page is opened
    except TimeoutException:

        LoginPage(open_login_page).do_login(get_user_name, get_user_password)
        return ProductsPage(open_login_page)


@fixture
def get_logged_product_page_with_cookie(open_login_page, get_user_name, get_user_password) -> ProductsPage:
    open_login_page.add_cookie(cookie_dict={'name': 'session-username', 'value': 'standard_user'})
    ProductsPage(open_login_page).driver.get('https://www.saucedemo.com/inventory.html')
    return ProductsPage(open_login_page)


@fixture(scope='session')
def get_user_name() -> str:
    return ConfigManager.user_name


@fixture(scope='session')
def get_user_password() -> str:
    return ConfigManager.user_pass

