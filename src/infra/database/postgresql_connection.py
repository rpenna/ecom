import psycopg2
import psycopg2.extras
from .postgresql_config import PG_URL


class PostgresConnection:
    def __init__(self):
        self.__conn = None
        self.__dict_cursor = psycopg2.extras.RealDictCursor

    def __connect(self):
        if self.__conn is None:
            self.__conn = psycopg2.connect(PG_URL)
        return self.__conn

    def execute(self, query: str, parameters: tuple = None):
        cursor = self.__connect().cursor()
        result = cursor.execute(query, parameters)
        self.__conn.commit()
        cursor.close()
        self.__conn.close()
        return result

    def query_one(self, query: str, parameters: tuple = None):
        cursor = self.__connect().cursor(cursor_factory=self.__dict_cursor)
        cursor.execute(query, parameters)
        result = cursor.fetchone()
        cursor.close()
        self.__conn.close()
        return result

    def query_many(self, query: str, parameters: tuple = None):
        cursor = self.__connect().cursor(cursor_factory=self.__dict_cursor)
        cursor.execute(query, parameters)
        result = cursor.fetchmany()
        cursor.close()
        self.__conn.close()
        return result
