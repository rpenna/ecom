import pytest
from decimal import Decimal
from datetime import datetime, timedelta

from ..src.place_order import PlaceOrder
from ..src.place_order_input import PlaceOrderInput
from ..src.place_order_output import PlaceOrderOutput

def test_should_place_order_containing_three_products():
    products = [
        {
            'id': '1',
            'price': 19.9,
            'quantity': 5
        },
        {
            'id': '2',
            'price': 2.8,
            'quantity': 30
        },
        {
            'id': '3',
            'price': 227.99,
            'quantity': 1
        }
    ]
    coupon = '15OFF'
    cpf = '01234567890'
    zipcode = '1234567'
    input = PlaceOrderInput(cpf, products, zipcode, coupon)
    place_order = PlaceOrder()
    output = place_order.execute(input)
    assert output.total == Decimal('349.77')
    assert output.shipping_fee == Decimal('400')
