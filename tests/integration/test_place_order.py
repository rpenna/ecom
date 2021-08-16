import pytest
from decimal import Decimal
from datetime import datetime, timedelta

from ...src.application.place_order import PlaceOrder
from ...src.application.place_order_input import PlaceOrderInput
from ...src.application.place_order_output import PlaceOrderOutput
from ...src.infra.repository.memory.product_repository_memory import ProductRepositoryMemory
from ...src.infra.repository.memory.coupon_repository_memory import CouponRepositoryMemory
from ...src.infra.repository.memory.order_repository_memory import OrderRepositoryMemory

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
    input = PlaceOrderInput(cpf, products, zipcode, coupon)
    product_repository = ProductRepositoryMemory()
    coupon_repository = CouponRepositoryMemory()
    order_repository = OrderRepositoryMemory()
    place_order = PlaceOrder(product_repository, coupon_repository, order_repository)
    output = place_order.execute(input)
    assert output.total == Decimal('349.77')
    assert output.shipping_fee == Decimal('400')
