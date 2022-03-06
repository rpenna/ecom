from ...database.postgresql_connection import PostgresConnection
from ....domain.repository.taxes_repository import TaxesRepository


class TaxesRepositoryPostgresql(TaxesRepository):
    def __init__(self, conn: PostgresConnection):
        self.__conn = conn

    def get_by_id_and_type(self, product_id: str, tax_type: str) -> float:
        query = """
            select value
            from ecom.taxes
            where product_id = %s
                and type = %s
        """
        parameters = (product_id, tax_type)
        taxes = self.__conn.query_one(query, parameters)
        if taxes is not None:
            return taxes["value"]
