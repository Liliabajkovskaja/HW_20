from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


FIND_BY_STATUS_URL = f"https://procraft.ua/ua/akkumuljatornyj-instrument/"


def test_color():
    driver = webdriver.Chrome()

    driver.get(FIND_BY_STATUS_URL)
    driver.maximize_window()

    wait_el(driver, ("css selector", '.btn.main-menu__btn')).click()
    move_to_el(driver, ("css selector", '.main-nav__item.main-nav__item--2'))
    el = wait_el(driver, ("css selector",  '.main-nav-dropdown__link'))
    color1 = el.value_of_css_property("color")
    el = move_to_el(driver, ("css selector",  '.main-nav-dropdown__link'))
    color2 = el.value_of_css_property("color")

    assert color1 != color2


def wait_el(driver, locator: tuple, timeout=3):
    wait = WebDriverWait(driver=driver, timeout=timeout)
    return wait.until(EC.visibility_of_element_located(locator))


def move_to_el(driver, locator: tuple, timeout=3):
    el = wait_el(driver, locator, timeout)
    AC(driver).move_to_element(el).perform()
    return el
