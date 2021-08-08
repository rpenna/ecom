import pytest

from ..src.shipping_calculator import ShippingCalculator
from ..src.product import Product

CHARACTERISTICS_CAMERA = {
    'height': 20,
    'width': 15,
    'depth': 10,
    'weight': 1000
}
CHARACTERISTICS_GUITAR = {
    'height': 200,
    'width': 30,
    'depth': 10,
    'weight': 3000
}
CHARACTERISTICS_FRIDGE = {
    'height': 200,
    'width': 100,
    'depth': 50,
    'weight': 40000
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
        Product('camera', 750, CHARACTERISTICS_CAMERA),
        Product('guitar', 2000, CHARACTERISTICS_GUITAR),
        Product('fridge', 3000, CHARACTERISTICS_FRIDGE)
    ]

one_product = (
    (Product('camera', 750, CHARACTERISTICS_CAMERA), 10),
    (Product('guitar', 2000, CHARACTERISTICS_GUITAR), 30),
    (Product('fridge', 3000, CHARACTERISTICS_FRIDGE), 400)
)

@pytest.mark.parametrize(
    'product, expected_fee',
    one_product
)
def test_should_calculate_shipping_fee_for_one_product(product, expected_fee):
    distance = 1000
    shipping_fee = ShippingCalculator.calculate(distance, product)
    assert shipping_fee == expected_fee
