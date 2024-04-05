
import psycopg2


class PostgresConnector:

    def __enter__(self):
        self.conn = psycopg2.connect(database="postgres", user="postgres", password="123", host="localhost", port=5432)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()