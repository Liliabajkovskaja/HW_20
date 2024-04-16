from core.page_objects.login_page import LoginPage


def test_simple(open_login_page, get_user_name, get_user_password):

    driver = open_login_page
    LoginPage(driver).\
        set_user_name(get_user_name).\
        set_password(get_user_password).\
        click_login().\
        find_shopping_cart()
