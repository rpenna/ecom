import pytest
from decimal import Decimal
from datetime import datetime, timedelta

from ...src.domain.entity.order import Order
from ...src.domain.entity.coupon import Coupon
from ...src.domain.entity.order_code import OrderCode
from ...src.domain.exception.invalid_cpf import InvalidCpf

@pytest.fixture
def order():
    return Order('30291840051')

@pytest.fixture
def order_three_products():
    issue_date = datetime(2021, 8, 24)
    year_count = 1
    order = Order('30291840051', issue_date, year_count)
    order.add_to_cart('1', 19.9, 1)
    order.add_to_cart('2', 2.8, 20)
    order.add_to_cart('3', 227.99, 1)
    return order

def test_should_accept_order_with_three_products(order_three_products):
    assert order_three_products.get_total_price() == Decimal('303.89')

def test_should_apply_discount(order_three_products):
    next_week = datetime.now() + timedelta(days=7)
    coupon = Coupon('10offCoupon', 10, next_week)
    order_three_products.add_discount_coupon(coupon)
    assert order_three_products.get_total_price() == Decimal('273.50')

def test_should_not_apply_discount_from_expired_coupon(order_three_products):
    yesterday = datetime.now() - timedelta(days=1)
    coupon = Coupon('10off', 10, yesterday)
    order_three_products.add_discount_coupon(coupon)
    assert order_three_products.get_total_price() == Decimal('303.89')

def test_should_deny_creating_order_with_invalid_cpf():
    issue_date = datetime(2021, 8, 24)
    year_count = 1
    with pytest.raises(InvalidCpf):
        order = Order('30291840050', issue_date, year_count)

def test_should_create_order_code(order_three_products):
    issue_date = datetime(2021, 8, 24)
    year_count = 1
    expected_order_code = OrderCode(issue_date, year_count).value
    assert order_three_products.code == expected_order_code
