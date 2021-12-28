import pytest
from datetime import datetime
from ...src.domain.entity.monetary import Monetary
from ...src.application.place_order.place_order import PlaceOrder
from ...src.application.place_order.place_order_input import PlaceOrderInput
from ...src.application.get_order.get_order import GetOrder
from ...src.infra.factory.memory_repository_factory import MemoryRepositoryFactory
from ...src.infra.gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

@pytest.fixture
def expected_total_price():
    return Monetary(349.77)

@pytest.fixture
def expected_taxes_default_month():
    return Monetary(23.87)

@pytest.fixture
def expected_taxes_november():
    return Monetary(2.3794)

@pytest.fixture
def placed_order_input():
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
def placed_order_input_november():
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

def test_should_place_order_with_expected_total_price(
        placed_order_input,
        expected_total_price
    ):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    placed_order = place_order.execute(placed_order_input)
    get_order = GetOrder(memory_repository_factory)
    order = get_order.execute(placed_order.code)
    assert order.total_price == expected_total_price

def test_given_an_order_issued_in_default_month_when_get_order_then_it_should_return_its_tax_costs(
        placed_order_input,
        expected_taxes_default_month
    ):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    placed_order = place_order.execute(placed_order_input)
    get_order = GetOrder(memory_repository_factory)
    order = get_order.execute(placed_order.code)
    assert order.tax == expected_taxes_default_month

def test_given_an_order_issued_in_november_when_get_order_then_it_should_return_its_tax_costs(
        placed_order_input_november,
        expected_taxes_november
    ):
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    place_order = PlaceOrder(
        memory_repository_factory,
        zipcode_calculator
    )
    placed_order = place_order.execute(placed_order_input_november)
    get_order = GetOrder(memory_repository_factory)
    order = get_order.execute(placed_order.code)
    assert order.tax == expected_taxes_november
