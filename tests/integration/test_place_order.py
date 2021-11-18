import pytest
from datetime import datetime
from ...src.domain.entity.monetary import Monetary
from ...src.application.place_order import PlaceOrder
from ...src.application.place_order_input import PlaceOrderInput
from ...src.infra.factory.memory_repository_factory import MemoryRepositoryFactory
from ...src.infra.gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

@pytest.fixture
def place_order_input():
    products = [
        {
            'id': '1',
            'quantity': 5
        },
        {
            'id': '2',
            'quantity': 30
        },
        {
            'id': '3',
            'quantity': 1
        }
    ]
    coupon = '15OFF'
    cpf = '01234567890'
    zipcode = '1234567'
    issue_date = datetime(2021, 8, 24)
    return PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)

@pytest.fixture
def place_order_input_november():
    products = [
        {
            'id': '1',
            'quantity': 5
        },
        {
            'id': '2',
            'quantity': 30
        },
        {
            'id': '3',
            'quantity': 1
        }
    ]
    coupon = '15OFF'
    cpf = '01234567890'
    zipcode = '1234567'
    issue_date = datetime(2021, 11, 24)
    return PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)

def test_given_an_order_when_its_placed_then_it_should_return_expected_total_price(place_order_input):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    output = place_order.execute(place_order_input)
    assert output.total_price == Monetary(349.77)

def test_given_an_order_when_its_placed_then_it_should_return_expected_shipping_fee(place_order_input):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    output = place_order.execute(place_order_input)
    assert output.shipping_fee == Monetary(400)

def test_given_an_order_made_in_default_month_when_its_placed_then_it_should_return_expected_tax(place_order_input):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    output = place_order.execute(place_order_input)
    assert output.tax == Monetary(23.87)

def test_given_an_order_made_in_default_month_when_its_placed_then_it_should_return_expected_tax(place_order_input_november):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    output = place_order.execute(place_order_input_november)
    assert output.tax == Monetary(2.3794)
