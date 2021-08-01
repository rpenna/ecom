import pytest
from decimal import Decimal
from datetime import datetime, timedelta

from ..src.order import Order
from ..src.coupon import Coupon
from ..src.invalid_cpf import InvalidCpf

BOOK_INFO = {
    'height': 15,
    'width': 10,
    'depth': 2,
    'weight': 1000
}

PFF2_MASK_INFO = {
    'height': 10,
    'width': 10,
    'depth': 0.01,
    'weight': 50
}

VACUUM_CLEANER_INFO = {
    'height': 40,
    'width': 30,
    'depth': 30,
    'weight': 5000
}
@pytest.fixture
def order():
    return Order('30291840051')

@pytest.fixture
def order_three_products():
    order = Order('30291840051')
    order.add_to_cart('book', 19.9, 1, BOOK_INFO)
    order.add_to_cart('pff2 mask', 2.8, 20, PFF2_MASK_INFO)
    order.add_to_cart('vacuum cleaner', 227.99, 1, VACUUM_CLEANER_INFO)
    return order

def test_should_accept_order_with_three_products(order_three_products):
    assert order_three_products.get_total(1000) == Decimal('364.39')

def test_should_apply_discount(order_three_products):
    next_week = datetime.now() + timedelta(days=7)
    coupon = Coupon('10offCoupon', 10, next_week)
    order_three_products.add_discount_coupon(coupon)
    assert order_three_products.get_total(1000) == Decimal('334')

def test_should_not_apply_discount_from_expired_coupon(order_three_products):
    yesterday = datetime.now() - timedelta(days=1)
    coupon = Coupon('10off', 10, yesterday)
    order_three_products.add_discount_coupon(coupon)
    assert order_three_products.get_total(1000) == Decimal('364.39')

def test_should_deny_creating_order_with_invalid_cpf():
    with pytest.raises(InvalidCpf):
        order = Order('30291840050')