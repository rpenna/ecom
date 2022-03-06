import pytest
from datetime import datetime
from ...src.domain.exception.out_of_stock import OutOfStock
from ...src.application.place_order.place_order import PlaceOrder
from ...src.application.place_order.place_order_input import PlaceOrderInput
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


@pytest.fixture()
def place_order_postgresql(autouse=True):
    postgresql_repository_factory = PostgresqlRepositoryFactory()
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    yield PlaceOrder(postgresql_repository_factory, zipcode_calculator)
    order_repository = postgresql_repository_factory.make_order_repository()
    order_repository.clear()
    stock_repository = postgresql_repository_factory.make_stock_repository()
    stock_repository.clear()


def test_given_an_order_when_its_placed_then_it_should_return_expected_total_price(
    place_order_postgresql, place_order_input
):
    output = place_order_postgresql.execute(place_order_input)
    assert output.total_price == "349.77"


def test_given_an_order_when_its_placed_then_it_should_return_expected_shipping_fee(
    place_order_postgresql, place_order_input
):
    output = place_order_postgresql.execute(place_order_input)
    assert output.shipping_fee == "4.00"


def test_given_an_order_made_in_default_month_when_its_placed_then_it_should_return_expected_tax(
    place_order_postgresql, place_order_input
):
    output = place_order_postgresql.execute(place_order_input)
    assert output.tax == "23.87"


def test_given_an_order_made_in_default_month_when_its_placed_then_it_should_return_expected_tax(
    place_order_postgresql, place_order_input_november
):
    output = place_order_postgresql.execute(place_order_input_november)
    assert output.tax == 237


def test_given_an_order_with_more_quantity_than_available_in_stock_when_its_placed_then_it_shoul_raise_out_of_stock_exception(
    place_order_postgresql,
):
    products = [{"id": "2", "quantity": 300}]
    coupon = "15OFF"
    cpf = "01234567890"
    zipcode = "1234567"
    issue_date = datetime(2021, 11, 24)
    place_order_input = PlaceOrderInput(cpf, issue_date, products, zipcode, coupon)
    with pytest.raises(OutOfStock):
        place_order_postgresql.execute(place_order_input)
