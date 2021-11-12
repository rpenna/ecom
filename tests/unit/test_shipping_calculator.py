import pytest

from ...src.domain.service.shipping_calculator import ShippingCalculator
from ...src.domain.entity.product import Product
from ...src.domain.entity.monetary import Monetary

CHARACTERISTICS_BOOK = {
    'height': 15,
    'width': 10,
    'depth': 2,
    'weight': 1000
}
CHARACTERISTICS_PFF2_MASK = {
    'height': 10,
    'width': 10,
    'depth': 0.01,
    'weight': 50
}
CHARACTERISTICS_VACCUM_CLEANER = {
    'height': 40,
    'width': 30,
    'depth': 30,
    'weight': 5000
}
CHEAP_FEE = {
    'height': 10,
    'width': 10,
    'depth': 5,
    'weight': 500
}

@pytest.fixture
def three_products():
    return [
        Product('1', 'book', 750, CHARACTERISTICS_BOOK),
        Product('2', 'pff2_mask', 2000, CHARACTERISTICS_PFF2_MASK),
        Product('3', 'vaccum_cleaner', 3000, CHARACTERISTICS_VACCUM_CLEANER)
    ]

one_product = (
    (Product('1', 'book', 750, CHARACTERISTICS_BOOK), Monetary(10)),
    (Product('2', 'pff2_mask', 2000, CHARACTERISTICS_PFF2_MASK), Monetary(10)),
    (Product('3', 'vaccum_cleaner', 3000, CHARACTERISTICS_VACCUM_CLEANER), Monetary(50))
)

@pytest.mark.parametrize(
    'product, expected_fee',
    one_product
)
def test_should_calculate_shipping_fee_for_one_product(product, expected_fee):
    distance = 1000
    shipping_fee = ShippingCalculator.calculate(distance, product)
    assert shipping_fee == expected_fee
