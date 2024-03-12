from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ProductsPage(BasePage):
    shopping_cart_class_locator = 'shopping_cart_link'

    def __init__(self, driver):
        super().__init__(driver)

    def find_shopping_cart(self):
        self._element_is_visible(locator=(By.CLASS_NAME, self.shopping_cart_class_locator))
