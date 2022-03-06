from ...database.postgresql_connection import PostgresConnection
from ....domain.repository.stock_repository import StockRepository
from ....domain.entity.stock_operation import StockOperation


class StockRepositoryPostgresql(StockRepository):
    def __init__(self, conn: PostgresConnection):
        self.__conn = conn

    def get_by_id(self, id: str) -> list:
        query = """
            select out_operation, quantity, date
            from ecom.stock
            where product_id = %s
        """
        parameters = (id,)
        stock_operations = []
        for operation in self.__conn.query_many(query, parameters):
            stock_operations.append(
                StockOperation(
                    id,
                    operation["out_operation"],
                    operation["quantity"],
                    operation["date"],
                )
            )
        return stock_operations

    def save(self, new_stock_operation: StockOperation) -> bool:
        query = """
            insert into ecom.stock (
                product_id,
                out_operation,
                quantity,
                date
            )
            values (%s, %s, %s, %s)
        """
        parameters = (
            new_stock_operation.id,
            new_stock_operation.out,
            new_stock_operation.quantity,
            new_stock_operation.date,
        )
        return self.__conn.execute(query, parameters) == 1

    def clear(self):
        query = """
            delete from ecom.stock where quantity != 100
        """
        self.__conn.execute(query)
