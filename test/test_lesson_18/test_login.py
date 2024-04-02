import pytest

from page_objects.login_page import LoginPage
from page_objects.products_page import ProductsPage


@pytest.mark.ui_tests
def test_login_user(open_login_page, get_user_name, get_user_password):
    LoginPage(open_login_page).do_login(get_user_name, get_user_password)
    ProductsPage(open_login_page).find_shopping_cart()
