from datetime import datetime
from ...domain.exception.order_not_found import OrderNotFound
from ...application.get_order import GetOrder
from ...domain.factory.repository_abstract_factory import RepositoryAbstractFactory
from ...application.place_order import PlaceOrder
from ...application.place_order_input import PlaceOrderInput
from ..gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

class Http:
    def __init__(self, repository_factory: RepositoryAbstractFactory):
        self.__repository_factory = repository_factory 

    def get_order(self, code: str) -> tuple([dict, int]):
        """Get order by its code

        Args:
            code (str): URL parameters

        Returns:
            tuple(dict, int): content of the order and its status
        """
        try:
            get_order = GetOrder(self.__repository_factory)
            order = get_order.execute(code)
            return (
                {
                    'code': order.code,
                    'issue_date': order.issue_date,
                    'total': float(order.total_price),
                    'products': order.products,
                },
                200
            )
        except OrderNotFound:
            return {}, 422
        except KeyError:
            return {}, 400

    def place_order(self, body: dict) -> tuple([dict, int]):
        products = body['products']
        cpf = body['cpf']
        zipcode = body['zipcode']
        coupon = body.get('coupon')
        order_input = PlaceOrderInput(
            cpf,
            datetime.now(),
            products,
            zipcode,
            coupon
        )
        zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
        place_order = PlaceOrder(self.__repository_factory, zipcode_calculator)
        output = place_order.execute(order_input)
        return (
            {
                'total_price': float(output.total_price),
                'shipping_fee': output.shipping_fee,
                'code': output.code
            },
            201
        )
