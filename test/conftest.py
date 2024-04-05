# import logging
# from time import time
# import os.path as path
# from typing import Type
#
# import allure
# import pytest
# from pytest import fixture
# from selenium.common import TimeoutException
# from selenium.webdriver.remote.webdriver import WebDriver
#
# from page_objects.login_page import LoginPage
# from page_objects.products_page import ProductsPage
# from utils.driver_factory import DriverFactory
# from utils.config_manager import ROOT_PATH
# from utils.config_manager import ConfigManager as iniManager
# from utils.config_manager_json import ConfigManager as jsonManager
#
# logger = logging.getLogger()
#
#
# @fixture(scope='session')
# def env(request) -> Type[jsonManager | iniManager]:
#     if request.config.getoption("--json"):
#         logger.info('Getting configs from json')
#         return jsonManager
#     logger.info('Getting configs from ini file')
#     return iniManager
#
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_setup(item):
#     config = item.config
#     logging_plugin = config.pluginmanager.get_plugin("logging-plugin")
#     file_path = path.join(ROOT_PATH, 'logs', f"{time()}.log")  # logfile
#     logging_plugin.set_log_path(str(file_path))
#     yield
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--json", action="store_true", help="read json"
#     )
#
#
# @fixture(scope='session')
# def get_driver(env) -> WebDriver:
#     driver = DriverFactory(env.browser).get_driver()
#     yield driver
#     driver.quit()
#
#
# @fixture(autouse=True)
# def make_screenshot_after_test(get_driver):
#     yield
#
#     file_name = f'{time()}.png'
#     full_path = path.join(ROOT_PATH, file_name)
#     get_driver.save_screenshot(full_path)
#
#     allure.attach.file(
#         full_path,
#         name=file_name,
#         attachment_type=allure.attachment_type.PNG
#     )
#
#
#
#
# @fixture
# def open_login_page(get_driver, env) -> WebDriver:
#     get_driver.get(env.url)
#     # get_driver.maximize_window()
#     return get_driver
#
#
# @fixture
# def get_logged_product_page(open_login_page, get_user_name, get_user_password) -> ProductsPage:
#
#     try:
#         return ProductsPage(open_login_page).find_shopping_cart(timeout=1)     # check if product page is opened
#     except TimeoutException:
#
#         LoginPage(open_login_page).do_login(get_user_name, get_user_password)
#         return ProductsPage(open_login_page)
#
#
# @fixture
# def get_logged_product_page_with_cookie(open_login_page, get_user_name, get_user_password) -> ProductsPage:
#     open_login_page.add_cookie(cookie_dict={'name': 'session-username', 'value': 'standard_user'})
#     ProductsPage(open_login_page).driver.get('https://www.saucedemo.com/inventory.html')
#     return ProductsPage(open_login_page)
#
#
# @fixture(scope='session')
# def get_user_name(env) -> str:
#     return env.user_name
#
#
# @fixture(scope='session')
# def get_user_password(env) -> str:
#     return env.user_pass
#
