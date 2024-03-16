from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.locators.login_page import Locators
from page_objects.products_page import ProductsPage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locators()

    def set_user_name(self, username):
        self._fill_input(username, (By.ID, self.locators.username_input_id_locator))
        return self

    def set_password(self, password):
        self._fill_input(password, (By.XPATH, self.locators.password_input_xpath_locator))
        return self

    def click_login(self):
        self._click_button((By.XPATH, self.locators.login_btn_xpath_locator))
        return ProductsPage(self.driver)

    def do_login(self, username, password):
        self.set_user_name(username)
        self.set_password(password)
        self.click_login()
        return self
