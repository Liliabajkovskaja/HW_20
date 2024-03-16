from time import time

from pytest import fixture
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.login_page import LoginPage
from page_objects.products_page import ProductsPage
from utils.config_manager import ConfigManager
from utils.driver_factory import DriverFactory
from utils.config_manager import ROOT_PATH


@fixture(scope='session')
def get_driver() -> WebDriver:
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


@fixture(scope='session')
def get_user_name() -> str:
    return ConfigManager.user_name


@fixture(scope='session')
def get_user_password() -> str:
    return ConfigManager.user_pass

