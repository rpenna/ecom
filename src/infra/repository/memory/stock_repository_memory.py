from datetime import datetime
from ....domain.repository.stock_repository import StockOperation

class StockRepositoryMemory(StockOperation):

    def __init__(self):
        self.__stock_operations = [
            StockOperation('1', False, 100, datetime.now()),
            StockOperation('2', False, 100, datetime.now()),
            StockOperation('3', False, 100, datetime.now())
        ]

    def get_by_id(self, id: str) -> list:
        """Find stock operation by product ID, sorted by operation date

        Args:
            id (str): product ID

        Returns:
            list: List of StockOperation
        """
        operations = []
        for operation in self.__stock_operations:
            if operation.id == id:
                operations.append(operation)
        return operations

    def save(self, new_stock_operation: StockOperation) -> bool:
        """Save new stock operation to repository

        Args:
            new_stock_operation (StockOperation): stock operation to be added

        Returns:
            bool: True if stock operation saved successfully
        """
        for operation in self.__stock_operations:
            same_id = operation.id == new_stock_operation
            same_date = operation.date == new_stock_operation.date
            if same_id and same_date:
                return False
        self.__stock_operations.append(new_stock_operation)
        return True
