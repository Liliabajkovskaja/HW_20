import pytest
from lessons.lesson_15.phone import Phone


@pytest.fixture(scope='session', autouse=False)
def get_model():
    return 'Iphone 15'


@pytest.fixture(scope='session', autouse=False)
def get_brand():
    return 'Apple'


@pytest.fixture
def get_new_phone(get_model, get_brand):
    return Phone(get_brand, get_model)


@pytest.fixture(scope='session')
def get_new_phone_session(get_brand, get_model):
    return Phone(get_brand, get_model)


@pytest.fixture(scope='module', autouse=False)  # by default (scope='function', autouse=False)
def get_new_phone2(get_brand, get_model):
    return Phone(get_brand, get_model)


@pytest.fixture(scope='function', autouse=True)
def clear_call_history(get_new_phone2):
    yield
    get_new_phone2.clear_call_history()
