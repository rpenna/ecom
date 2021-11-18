import pytest
from datetime import datetime
from ...src.domain.factory.tax_calculator_factory import TaxCalculatorFactory
from ...src.domain.entity.order_product import OrderProduct
from ...src.domain.entity.monetary import Monetary
from ...src.infra.repository.memory.taxes_repository_memory import TaxesRepositoryMemory

TAXES_TABLE = TaxesRepositoryMemory()

@pytest.fixture
def order_books():
    return OrderProduct('1', 19.9, 2)

@pytest.fixture
def order_pff2_masks():
    return OrderProduct('2', 2.8, 2)

@pytest.fixture
def order_vacuum_cleaner():
    return OrderProduct('3', 227.99, 1)

@pytest.fixture
def default_month_date():
    return datetime(2021, 10, 29, 15, 5, 44, 343)

@pytest.fixture
def november_date():
    return datetime(2021, 11, 29, 15, 5, 44, 343)

def test_given_a_book_when_calculate_tax_on_default_month_then_it_should_return_expected_tax(order_books ,default_month_date):
    tax_calculator = TaxCalculatorFactory().make(default_month_date, TAXES_TABLE)
    taxes = tax_calculator.calculate(order_books)
    assert taxes == Monetary(0.4)

def test_given_a_book_when_calculate_tax_on_november_then_it_should_return_expected_tax(order_books, november_date):
    tax_calculator = TaxCalculatorFactory().make(november_date, TAXES_TABLE)
    taxes = tax_calculator.calculate(order_books)
    assert taxes == Monetary(0.04)

def test_given_a_medical_product_when_calculate_tax_on_default_month_then_it_should_return_expected_tax(order_pff2_masks, default_month_date):
    tax_calculator = TaxCalculatorFactory().make(default_month_date, TAXES_TABLE)
    taxes = tax_calculator.calculate(order_pff2_masks)
    assert taxes == Monetary(0.0056)

def test_given_a_medical_product_when_calculate_tax_on_november_then_it_should_return_expected_tax(order_pff2_masks, november_date):
    tax_calculator = TaxCalculatorFactory().make(november_date, TAXES_TABLE)
    taxes = tax_calculator.calculate(order_pff2_masks)
    assert taxes == Monetary(0)

def test_given_a_home_category_product_when_calculate_tax_on_default_month_then_it_should_return_expected_tax(order_vacuum_cleaner, default_month_date):
    tax_calculator = TaxCalculatorFactory().make(default_month_date, TAXES_TABLE)
    taxes = tax_calculator.calculate(order_vacuum_cleaner)
    assert taxes == Monetary(22.799)

def test_given_a_home_category_product_when_calculate_tax_on_november_then_it_should_return_expected_tax(order_vacuum_cleaner, november_date):
    tax_calculator = TaxCalculatorFactory().make(november_date, TAXES_TABLE)
    taxes = tax_calculator.calculate(order_vacuum_cleaner)
    assert taxes == Monetary(2.2799)
