import pytest

from ..src.shipping import Shipping
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
        Product('camera', 750, 1, CHARACTERISTICS_CAMERA),
        Product('guitar', 2000, 1, CHARACTERISTICS_GUITAR),
        Product('fridge', 3000, 1, CHARACTERISTICS_FRIDGE)
    ]

one_product = (
    (Product('camera', 750, 1, CHARACTERISTICS_CAMERA), 10),
    (Product('guitar', 2000, 1, CHARACTERISTICS_GUITAR), 30),
    (Product('fridge', 3000, 1, CHARACTERISTICS_FRIDGE), 400)
)

@pytest.mark.parametrize(
    'product, expected_fee',
    one_product
)
def test_should_calculate_shipping_fee_for_one_product(product, expected_fee):
    distance = 1000
    shipping = Shipping(distance, [product])
    assert shipping.get_total() == expected_fee

def test_should_calculate_shipping_of_three_products(three_products):
    distance = 1000
    shipping = Shipping(distance, three_products)
    assert shipping.get_total() == 440

def test_should_minimum_shipping_fee_must_be_ten():
    product = Product('small product', 1, 1, CHEAP_FEE)
    distance = 1000
    shipping = Shipping(distance, [product])
    assert shipping.get_total() == 10
