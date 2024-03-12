from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _element_is_visible(self, locator: tuple[str, str], timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    def _element_is_clickable(self, locator: tuple[str, str], timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    def _fill_input(self, input_data: str, locator: tuple[str, str], timeout: int = 3):
        self._element_is_visible(locator, timeout)
        return self.driver.find_element(by=locator[0], value=locator[1]).send_keys(input_data)

    def _click_button(self, locator, timeout=3):
        self._element_is_clickable(locator, timeout)
        return self.driver.find_element(by=locator[0], value=locator[1]).click()
