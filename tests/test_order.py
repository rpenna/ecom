import pytest
from decimal import Decimal

from ..src.order import Order
from ..src.coupon import Coupon
from ..src.invalid_cpf import InvalidCpf

@pytest.fixture
def order():
    return Order('30291840051')

@pytest.fixture
def order_three_products():
    order = Order('30291840051')
    order.add_to_cart('book', 19.9, 1)
    order.add_to_cart('pff2 mask', 2.8, 20)
    order.add_to_cart('vacuum cleaner', 227.99, 1)
    return order


def test_should_accept_order_with_three_products(order_three_products):
    assert order_three_products.get_total() == Decimal('303.89')

def test_should_apply_discount(order_three_products):
    coupon = Coupon('10offCoupon', 10)
    order_three_products.add_discount_coupon(coupon)
    assert order_three_products.get_total() == Decimal('273.50')

def test_should_deny_creating_order_with_invalid_cpf():
    with pytest.raises(InvalidCpf):
        order = Order('30291840050')
