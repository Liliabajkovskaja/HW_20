import pytest

from lessons.lesson_15.phone import Phone

@pytest.mark.smoke
@pytest.mark.parametrize('phone_suffix', [10, 11, 12, 13, 14], ids=[f'Iphone_{k}' for k in range(10, 15)])
def test_phone_basic_model(phone_suffix):
    model = f'Iphone {phone_suffix}'
    new_phone = Phone(brand='Apple', model=model)


    assert new_phone.model == model



