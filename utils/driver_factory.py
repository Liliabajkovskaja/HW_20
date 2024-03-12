from selenium import webdriver


class DriverFactory:

    def __init__(self, driver_type: str):
        self._driver_type = driver_type

    def get_driver(self):
        if self._driver_type.lower() == 'chrome':
            return webdriver.Chrome()
        elif self._driver_type.lower() == 'firefox':
            return webdriver.Firefox()
        else:
            raise ValueError(f'Unknown browser: {self._driver_type}')