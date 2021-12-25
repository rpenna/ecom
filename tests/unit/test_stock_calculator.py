import pytest
from datetime import datetime
from ...src.domain.entity.stock_operation import StockOperation
from ...src.domain.service.stock_calculator import StockCalculator

EXPECTED_QUANTITY = 5

@pytest.fixture
def stock_record():
    operation_date_out = datetime(2021, 10,15)
    operation_date_in = datetime(2021, 10,10)
    stock_in = StockOperation(
        id='123',
        out=False,
        quantity=10,
        operation_date=operation_date_in
    )
    stock_out = StockOperation(
        id='123',
        out=True,
        quantity=5,
        operation_date=operation_date_out
    )
    return [stock_in, stock_out]

def test_given_a_stock_record_when_asked_to_calculate_then_it_should_return_item_quantity(stock_record):
    calculator = StockCalculator()
    quantity = calculator.calculate(stock_record)
    assert quantity == EXPECTED_QUANTITY
