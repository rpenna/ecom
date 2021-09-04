from datetime import datetime
from ....domain.entity.order import Order
from ....domain.repository.order_repository import OrderRepository
from ....domain.exception.order_not_found import OrderNotFound

class OrderRepositoryMemory(OrderRepository):
    _instance = None
    __orders = []

    def __new__(cls):
        """Singleton design pattern implementation alternative in python

        Returns:
            OrderRepositoryMemroy: An OrderRepositoryMemory instance
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

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
        
    def save(self, new_order: Order) -> None:
        """Save order in database

        Args:
            new_order (Order): order to be saved on database
        """
        self.__orders.append(new_order)

    def get_by_code(self, code: str) -> Order:
        """Search for order by its code

        Args:
            code (str): code to be searched

        Raises:
            OrderNotFound: when order was not found

        Returns:
            Order: order found
        """
        for order in self.__orders:
            if order.code == code:
                return order
        raise OrderNotFound
