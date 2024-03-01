import pytest
import os


@pytest.mark.smoke
def test_phone_basic_model(get_new_phone2, get_model):
    assert get_new_phone2.model == get_model


@pytest.mark.sanity
@pytest.mark.smoke
def test_phone_basic_brand(get_new_phone2, get_brand):
    assert get_new_phone2.brand == get_brand


@pytest.mark.sanity
def test_call_history_with_1_call(get_new_phone2):
    phone = get_new_phone2
    phone.make_call('+380999998877')

    assert len(phone.call_history) == 1


def test_call_history_with_2_calls(get_new_phone2):
    phone = get_new_phone2
    phone.make_call('+380999998877')
    phone.make_call('+380999998877')

    assert len(phone.call_history) == 2


@pytest.mark.skipif(os.getenv('CURRENT_ENV') != 'DEV', reason='Only for DEV')
def test_invalid_number(get_new_phone2):
    with pytest.raises(ValueError):
        get_new_phone2.validate_number('+38099999877')


@pytest.mark.xfail
def test_valid_number(get_new_phone2):  # bug in jira # 555
    get_new_phone2.validate_number('+38099999877')
