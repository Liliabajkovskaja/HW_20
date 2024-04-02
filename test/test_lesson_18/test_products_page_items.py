import pytest
import allure

@allure.epic("Web interface")
# @allure.feature("Essential features")
# @allure.story("Authentication")
@allure.title('test all titles are unique')
@pytest.mark.ui_tests
def test_titles_are_unique(get_logged_product_page):
    products_page = get_logged_product_page
    titles = products_page.get_items_titles()
    assert len(titles) == len(set(titles)), 'You have non-unique elements'

@allure.epic("Product page")
@allure.title('test all prices are ordered')
@pytest.mark.ui_tests
def test_prices_are_ordered(get_logged_product_page):
    products_page = get_logged_product_page
    # prices = products_page.get_items_prices()
    # prices = [float(p[1:]) for p in prices]  # -> [float]

    prices = [float(p[1:]) for p in products_page.get_items_prices()]

    assert sorted(prices) == prices, f'There is no sorting'

@allure.epic("Product page")
@allure.title('scroll to 6 element')
@pytest.mark.ui_tests
def test_scroll_to_6_element(get_logged_product_page):
    # we are expected that 6 element at the page
    products_page = get_logged_product_page
    products_page.scroll_by_selenium_to_last_item(6)

