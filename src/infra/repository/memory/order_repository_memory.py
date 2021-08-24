from datetime import datetime
from ....domain.entity.order import Order
from ....domain.repository.order_repository import OrderRepository

class OrderRepositoryMemory(OrderRepository):
    def __init__(self):
        self.__orders = []

    def count_by_year(self, issue_date: datetime) -> str:
        """Create new order in database

        Args:
            issue_date (datetime): order's issue date

        Returns:
            str: ID code of the order created
        """
        counter = 1
        year = issue_date.year
        for order in self.__orders:
            if order.issue_date.year == year:
                counter += 1
        return counter
        
    def save(self, saved_order: Order) -> bool:
        """Save order in database

        Args:
            saved_order (Order): order to be saved on database

        Returns:
            bool: True if order was saved
        """
        i = 0
        for order in self.__orders:
            if order.id == saved_order.id:
                self.__orders[i] = saved_order
                return True
            i += 1
        return False
