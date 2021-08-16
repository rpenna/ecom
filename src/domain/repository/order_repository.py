import abc
from ..entity.order import Order

class OrderRepository(metaclass=abc.ABCMeta):
    def create(self) -> str:
        """Create new order in database

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