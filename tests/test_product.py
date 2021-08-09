import pytest

from ..src.product import Product

@pytest.fixture
def product_for_testing():
    info = {
        'height': 20,
        'width': 15,
        'depth': 10,
        'weight': 1000
    }
    return Product('0', 'testing_product', 1, info)

def test_should_calculate_volume_correctly(product_for_testing):
    assert product_for_testing.get_volume() == 0.003

def test_should_calculate_density_correctly(product_for_testing):
    assert product_for_testing.get_density() == 333.3333333333333
