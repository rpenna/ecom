import psycopg2
from .postgresql_config import PG_URL


class PostgresConnection:
    def __connect(self):
        if not self.__conn:
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
        cursor = self.__connect().cursor()
        cursor.execute(query, parameters)
        result = cursor.fetch_one()
        cursor.close()
        self.__conn.close()
        return result

    def query_many(self, query: str, parameters: tuple = None):
        cursor = self.__connect().cursor()
        cursor.execute(query, parameters)
        result = cursor.fetch_many()
        cursor.close()
        self.__conn.close()
        return result
