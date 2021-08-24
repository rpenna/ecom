import abc
from datetime import datetime
from ..entity.order import Order

class OrderRepository(metaclass=abc.ABCMeta):
    def count_by_year(self, issue_date: datetime) -> str:
        """Create new order in database

        Args:
            issue_date (datetime): order's issue date

        Returns:
            str: ID code of the order created
        """
        raise NotImplementedError

    def save(self, order: Order) -> bool:
        """Save order in database

        Args:
            order (Order): order to be saved on database

        Returns:
            bool: True if order was saved
        """
        raise NotImplementedError