from random import choice

from core.dbs.db_base.base_sqlite_table import execute_postgrese_sql_query


class PostgresProductTable:

    def __init__(self):
        self.db_name = 'test_db.db'
        self.table_name = 'public.products'

    @execute_postgrese_sql_query
    def get_all_products(self):
        return f'select * from {self.table_name}'


print(PostgresProductTable().get_all_products())
