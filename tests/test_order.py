import pytest

from ..src.order import Order
from ..src.invalid_cpf import InvalidCpf

@pytest.fixture
def order_three_products():
    order = Order('30291840051')
    order.add_to_cart('book', 19.9, 1)
    order.add_to_cart('pff2 masks', 2.8, 20)
    order.add_to_cart('vacuum cleaner', 227.99, 1)
    return order

@pytest.fixture
def invalid_cpf_order():
    return Order('30291840050')

def test_should_close_order_with_three_products(order_three_products):
    summary = order_three_products.close_order()
    assert summary['total'] == 303.89

def test_should_apply_discount(order_three_products):
    order_three_products.add_discount_coupon('10offCoupon')
    summary = order_three_products.close_order()
    assert summary['total'] == 273.5

def test_should_deny_close_order_with_invalid_cpf(invalid_cpf_order):
    with pytest.raises(InvalidCpf):
        invalid_cpf_order.add_to_cart('microwave', 459.99, 1)
        invalid_cpf_order.close_order()
