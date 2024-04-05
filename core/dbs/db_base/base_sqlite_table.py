from core.dbs.db_base.postgress_connector import PostgresConnector
from core.dbs.db_base.sqlite_connector import SqliteConnector


def execute_sql_query(fn):
    def wrapper(*args, **kwargs):
        with SqliteConnector() as cursor:
            return cursor.execute(fn(*args, **kwargs)).fetchall()

    return wrapper


def execute_postgrese_sql_query(fn):
    def wrapper(*args, **kwargs):
        with PostgresConnector() as cursor:
            cursor.execute(fn(*args, **kwargs))
            return cursor.fetchall()

    return wrapper