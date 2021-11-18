from .get_order_output import GetOrderOutput
from ..domain.entity.order import Order
from ..domain.factory.repository_abstract_factory import RepositoryAbstractFactory

class GetOrder:
    def __init__(self, repository_factory: RepositoryAbstractFactory):
        self.__order_repository = repository_factory.make_order_repository()
        self.__product_repository = repository_factory.make_product_repository()

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
            'tax': order.tax,
            'total_price': order.get_total_price()
        }
        return GetOrderOutput(order_data)
