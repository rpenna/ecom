from .get_order_output import GetOrderOutput
from ..domain.entity.order import Order
from ..domain.repository.product_repository import ProductRepository
from ..domain.repository.order_repository import OrderRepository
from ..domain.exception.order_not_found import OrderNotFound

class GetOrder:
    def __init__(self, order_repository: OrderRepository, product_repository: ProductRepository):
        self.__order_repository = order_repository
        self.__product_repository = product_repository

    def __get_products(self, order: Order) -> list:
        """Lists order's products data

        Args:
            order (Order): order found by the execute method

        Returns:
            list: products of the order
        """
        products = []
        for ordered_product in order.cart:
            product = self.__product_repository.get_by_id(ordered_product.id)
            products.append({
                'description': product.description,
                'quantity': ordered_product.quantity,
                'price': ordered_product.price
            })
        return products

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
        products = self.__get_products(order)
        order_data = {
            'issue_date': order.issue_date,
            'code': order.code,
            'products': products,
            'total_price': order.get_total_price()
        }
        return GetOrderOutput(order_data)
