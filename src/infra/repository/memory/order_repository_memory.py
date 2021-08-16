from ....domain.entity.order import Order
from ....domain.repository.order_repository import OrderRepository

class OrderRepositoryMemory(OrderRepository):
    def __init__(self):
        self.__orders = []

    def create(self, new_order: Order) -> bool:
        """Save order to database

        Args:
            order (Order): order to be created on database

        Returns:
            bool: True if order was created
        """
        for order in self.__orders:
            if order.id == new_order.id:
                return False
        self.__orders.append(new_order)
        return True
