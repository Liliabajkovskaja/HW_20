import pytest
from lesson_15.phone import Phone


class TestPhone:
    """
    comment
    """

    expected_model = 'Iphone 13'
    expected_brand = 'Apple'
    phone = Phone(expected_brand, expected_model)
    def setup_method(self):

        print('\nsetup_method was run')

    def teardown_method(self):
        self.phone.clear_call_history()
        print('\nteardown_method was run')

    def test_get_model_2(self, get_new_phone):
        """
        comment
        :return:
        """
        phone = get_new_phone
        # if phone.model != expected_model:
        #     raise AssertionError
        assert phone.model == 'Iphone 13'  # comment

    def test_get_model(self):
        """
        comment
        :return:
        """

        # if phone.model != expected_model:
        #     raise AssertionError
        assert self.phone.model == self.expected_model  # comment

    def test_get_brand(self):

        assert self.phone.brand == self.expected_brand

    def test_check_call_history_after_call(self):
        self.phone.make_call('+380999998877')

        assert len(self.phone.call_history) == 1

    def test_empty_call_history(self):
        assert self.phone.call_history == []

    def test_invalid_number(self):
        with pytest.raises(ValueError):
            self.phone.validate_number('+38099999877')

