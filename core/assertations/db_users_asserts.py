from assertpy import assert_that, soft_assertions


def assert_one_user(db_data: tuple, expected_data: dict):
    assert_that(db_data).is_length(1)
    user = db_data[0]

    with soft_assertions():
        assert_that(user[0]).is_equal_to(expected_data['user_id'])
        assert_that(user[1]).is_equal_to(expected_data['name'])
        assert_that(user[2]).is_equal_to(expected_data['age'])
        assert_that(user[3]).is_equal_to(expected_data['mail'])