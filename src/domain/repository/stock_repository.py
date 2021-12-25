import abc
from ..entity.stock_operation import StockOperation

class StockRepository(metaclass=abc.ABCMeta):
    
    def get_by_id(self, id: str) -> list:
        """Find stock operation by product ID, sorted by operation date

        Args:
            id (str): product ID

        Returns:
            list: List of StockOperation
        """
        raise NotImplementedError

    def save(self, new_stock_operation: StockOperation) -> bool:
        """Save new stock operation to repository

        Args:
            new_stock_operation (StockOperation): stock operation to be added

        Returns:
            bool: True if stock operation saved successfully
        """
        raise NotImplementedError
