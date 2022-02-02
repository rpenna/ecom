import pytest
from datetime import datetime
from ...src.domain.entity.monetary import Monetary
from ...src.domain.exception.out_of_stock import OutOfStock
from ...src.application.place_order.place_order import PlaceOrder
from ...src.application.place_order.place_order_input import PlaceOrderInput
from ...src.infra.factory.memory_repository_factory import MemoryRepositoryFactory
from ...src.infra.factory.postgresql_repository_factory import (
    PostgresqlRepositoryFactory,
)
from ...src.infra.gateway.memory.zipcode_distance_calculator_api_memory import (
    ZipcodeDistanceCalculatorApiMemory,
)


@pytest.fixture
def place_order_input():
    products = [
        {"id": "1", "quantity": 5},
        {"id": "2", "quantity": 30},
        {"id": "3", "quantity": 1},
    ]
    coupon = "15OFF"
    cpf = "01234567890"
    zipcode = "1234567"
    issue_date = datetime(2021, 8, 24)
    return PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)


@pytest.fixture
def place_order_input_november():
    products = [
        {"id": "1", "quantity": 5},
        {"id": "2", "quantity": 30},
        {"id": "3", "quantity": 1},
    ]
    coupon = "15OFF"
    cpf = "01234567890"
    zipcode = "1234567"
    issue_date = datetime(2021, 11, 24)
    return PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)


@pytest.fixture
def place_order_memory():
    memory_repository_factory = MemoryRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    return PlaceOrder(memory_repository_factory, zipcode_calculator)


@pytest.fixture
def place_order_postgresql():
    memory_repository_factory = PostgresqlRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    return PlaceOrder(memory_repository_factory, zipcode_calculator)


def test_given_an_order_when_its_placed_then_it_should_return_expected_total_price(
    place_order_memory, place_order_input
):
    output = place_order_memory.execute(place_order_input)
    assert output.total_price == Monetary(349.77)


def test_given_an_order_when_its_placed_then_it_should_return_expected_shipping_fee(
    place_order_memory, place_order_input
):
    output = place_order_memory.execute(place_order_input)
    assert output.shipping_fee == Monetary(400)


def test_given_an_order_made_in_default_month_when_its_placed_then_it_should_return_expected_tax(
    place_order_memory, place_order_input
):
    output = place_order_memory.execute(place_order_input)
    assert output.tax == Monetary(23.87)


def test_given_an_order_made_in_default_month_when_its_placed_then_it_should_return_expected_tax(
    place_order_memory, place_order_input_november
):
    output = place_order_memory.execute(place_order_input_november)
    assert output.tax == Monetary(2.3794)


def test_given_an_order_with_more_quantity_than_available_in_stock_when_its_placed_then_it_shoul_raise_out_of_stock_exception(
    place_order_memory,
):
    products = [{"id": "2", "quantity": 300}]
    coupon = "15OFF"
    cpf = "01234567890"
    zipcode = "1234567"
    issue_date = datetime(2021, 11, 24)
    place_order_input = PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)
    with pytest.raises(OutOfStock):
        place_order_memory.execute(place_order_input)
