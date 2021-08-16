from datetime import datetime
from ....domain.entity.order import Order
from ....domain.repository.order_repository import OrderRepository

class OrderRepositoryMemory(OrderRepository):
    def __init__(self):
        self.__orders = []

    def __get_sequential_code(self, year: str) -> int:
        """Counts the next sequential code for the year informed

        Args:
            year (str): year to be counted

        Returns:
            int: next sequential code
        """
        orders_counter = 1
        for order in self.__orders:
            if order.id.startswith(year):
                orders_counter += 1
        return orders_counter

    def create(self, new_order: Order) -> str:
        """Create new order in database

        Args:
            new_order (Order): order to be created on database

        Returns:
            str: ID code of the order created
        """
        year = datetime.strftime(datetime.now(), '%Y')
        sequential_code = self.__get_sequential_code(year)
        id_code = year + str(sequential_code).zfill(8)
        new_order.id = id_code
        self.__orders.append(new_order)
        return id_code
        
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
