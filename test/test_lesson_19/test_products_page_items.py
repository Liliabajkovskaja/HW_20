import logging

logger = logging.getLogger(__file__)

def test_titles_are_unique(get_logged_product_page_with_cookie):

    products_page = get_logged_product_page_with_cookie
    titles = products_page.get_items_titles()
    assert len(titles) == len(set(titles)), 'You have non-unique elements'


def test_get_local_storage_value(get_logged_product_page_with_cookie):

    products_page = get_logged_product_page_with_cookie
    storage_values = products_page.driver.execute_script("return  localStorage")
    assert len(storage_values) > 0, 'Local storage is empty'


def test_scroll_to_6_element(get_logged_product_page):
    # we are expected that 6 element at the page
    logger.info('My logs: run test_scroll_to_6_element', )
    products_page = get_logged_product_page
    products_page.scroll_by_selenium_to_last_item(6)