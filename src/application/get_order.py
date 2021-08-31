from .get_order_output import GetOrderOutput
from ..domain.repository.order_repository import OrderRepository
from ..domain.exception.order_not_found import OrderNotFound

class GetOrder:
    def __init__(self, order_repository: OrderRepository):
        self.__order_repository = order_repository

    def execute(self, code: str) -> GetOrderOutput:
        """Search order by code and return its data

        Args:
            code (str): order's code
        
        Raises:
            OrderNotFound: when order was not found

        Returns:
            GetOrderOutput: order data
        """
        order = self.__order_repository.get_by_code(code)
        return GetOrderOutput(order)
