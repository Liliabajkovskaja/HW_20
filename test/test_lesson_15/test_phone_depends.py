import pytest

from lessons.lesson_15.phone import Phone


@pytest.mark.xfail(reason='check failed')
def test_phone_brand(get_new_phone_session, get_model):
    phone = get_new_phone_session
    assert False
    assert phone.model == get_model


@pytest.mark.depends(on=['test_phone_brand'])
def test_phone_model(get_new_phone_session, get_model):
    phone = get_new_phone_session
    new_model = 'New model'
    phone.model = new_model
    assert phone.model == new_model


@pytest.mark.depends(on=['test_phone_brand'])
def test_phone_model2(get_new_phone_session, get_model):
    phone = get_new_phone_session
    new_model = 'New model'
    phone.model = new_model
    assert phone.model == new_model




