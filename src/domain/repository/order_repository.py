import abc
from ..entity.order import Order

class OrderRepository(metaclass=abc.ABCMeta):
    def create(self, order: Order) -> bool:
        """Save order to database

        Args:
            order (Order): order to be created on database

        Returns:
            bool: True if order was created
        """
        raise NotImplementedError
