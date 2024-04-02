from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import allure


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step
    def _element_is_visible(self, locator: tuple[str, str], timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step
    def _element_is_clickable(self, locator: tuple[str, str], timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step
    def _elements_is_present(self, locator: tuple[str, str], timeout: int = 3):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))

    @allure.step
    def _fill_input(self, input_data: str, locator: tuple[str, str], timeout: int = 3):
        self._element_is_visible(locator, timeout)
        return self.driver.find_element(by=locator[0], value=locator[1]).send_keys(input_data)

    @allure.step
    def _click_button(self, locator, timeout=3):
        self._element_is_clickable(locator, timeout)
        return self.driver.find_element(by=locator[0], value=locator[1]).click()

    @allure.step
    def get_texts(self, locator, timeout=3) -> [str]:
        self._element_is_visible(locator, timeout)
        return [k.text for k in self.driver.find_elements(by=locator[0], value=locator[1])]

    @allure.step
    def get_element_by_number(self, locator, number, timeout=3) -> [WebElement]:
        els = self._elements_is_present(locator, timeout)
        if number <= len(els):
            return els[number - 1]
        else:
            raise AttributeError(f'There are ony {len(els)} elements. You\'ve tried to get {number}')

