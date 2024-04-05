from core.dbs.sqlite_user_table import SqliteUsersTable
from assertpy import assert_that
from core.assertations.db_users_asserts import assert_one_user


def test_get_all_users():

    users = SqliteUsersTable().get_all_users()
    assert_that(len(users), 'Users > 0').is_not_zero()
    assert users


def test_get_with_id_1():
    user_id = 1

    user = SqliteUsersTable().get_id_by_id(user_id)

    assert_that(user).is_length(1)
    user = user[0]

    assert_that(user[0]).is_equal_to(user_id)


def test_get_info_created_user(create_delete_user):
    user = SqliteUsersTable().get_id_by_id(create_delete_user['user_id'])
    assert_one_user(db_data=user, expected_data=create_delete_user)
