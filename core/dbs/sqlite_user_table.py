from random import choice

from core.dbs.db_base.base_sqlite_table import execute_sql_query


class SqliteUsersTable:

    def __init__(self):
        self.db_name = 'test_db.db'
        self.table_name = 'Users'

    @execute_sql_query
    def get_all_users(self):
        return f'select * from {self.table_name}'

    @execute_sql_query
    def get_id_by_name(self, user_name):
        return f'select id from {self.table_name} where name = {user_name}'

    @execute_sql_query
    def get_id_by_id(self, user_id):
        return f'select * from {self.table_name} where id = {user_id}'

    @execute_sql_query
    def create_user(self, user_id=None, name='den', age=23, mail='asd@asd.com'):

        # if bool(user_id) is not False:
        #     user_id = user_id
        # else:
        #     user_id = choice(range(3, 10000))

        user_id = user_id or choice(range(3, 10000))
        return f'insert into {self.table_name} values ({user_id}, "{name}", {age}, "{mail}")'

    @execute_sql_query
    def delete_user_by_id(self, user_id):
        return f'delete from {self.table_name} where id = {user_id}'


print(SqliteUsersTable().get_all_users())
