from flask import make_response, Response, request
from flask.views import MethodView
from datetime import datetime
from ...domain.exception.order_not_found import OrderNotFound
from ...application.get_order import GetOrder
from ...application.place_order import PlaceOrder
from ...application.place_order_input import PlaceOrderInput
from ..factory.memory_repository_factory import MemoryRepositoryFactory
from ..gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

class OrderView(MethodView):
    def __init__(self):
        self.__repository_factory = MemoryRepositoryFactory()

    def get(self, code) -> Response:
        try:
            get_order = GetOrder(self.__repository_factory)
            print(code)
            order = get_order.execute(code)
            return make_response(
                {
                    'code': order.code,
                    'issue_date': order.issue_date,
                    'total': float(order.total_price),
                    'products': order.products,
                },
                200
            )
        except OrderNotFound:
            return make_response({}, 422)
        except KeyError:
            return make_response({}, 400)

    def post(self) -> Response:
        body = request.get_json()
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
        return make_response(
            {
                'total_price': float(output.total_price),
                'shipping_fee': output.shipping_fee,
                'code': output.code
            },
            201
        )
