import pytest
from decimal import Decimal
from datetime import datetime, timedelta
from ...src.application.place_order import PlaceOrder
from ...src.application.place_order_input import PlaceOrderInput
from ...src.application.place_order_output import PlaceOrderOutput
from ...src.infra.factory.memory_repository_factory import MemoryRepositoryFactory
from ...src.infra.gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

def test_should_place_order_containing_three_products():
    products = [
        {
            'id': '1',
            'quantity': 5
        },
        {
            'id': '2',
            'quantity': 30
        },
        {
            'id': '3',
            'quantity': 1
        }
    ]
    coupon = '15OFF'
    cpf = '01234567890'
    zipcode = '1234567'
    issue_date = datetime(2021, 8, 24)
    input = PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    output = place_order.execute(input)
    assert output.total_price == Decimal('349.77')
    assert output.shipping_fee == Decimal('400')
