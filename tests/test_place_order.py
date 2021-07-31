import pytest
from decimal import Decimal
from datetime import datetime, timedelta

from ..src.place_order import PlaceOrder

def test_should_place_order_containing_three_products():
    next_week = datetime.now() + timedelta(days=7)
    order = {
        'cart': [
            {
                'description': 'book',
                'price': 19.9,
                'quantity': 5
            },
            {
                'description': 'pff2 mask',
                'price': 2.8,
                'quantity': 30
            },
            {
                'description': 'vacuum cleaner',
                'price': 227.99,
                'quantity': 1
            }
        ],
        'coupon': {
            'code': '15off',
            'discount': 15,
            'expiring_date': next_week
        },
        'cpf': '01234567890'
    }
    place_order = PlaceOrder()
    order_summary = place_order.execute(order)
    assert order_summary['total'] == Decimal('349.77')
