import pytest
from datetime import datetime
from ...src.domain.service.tax_calculator import TaxCalculator
from ...src.domain.entity.product import Product
from ...src.domain.entity.monetary import Monetary

INFO_BOOK = {
    'height': 15,
    'width': 10,
    'depth': 2,
    'weight': 1000
}
INFO_PFF2_MASK = {
    'height': 10,
    'width': 10,
    'depth': 0.01,
    'weight': 50
}
INFO_VACUUM_CLEANER = {
    'height': 40,
    'width': 30,
    'depth': 30,
    'weight': 5000
}

def test_given_a_book_when_calculate_tax_on_default_month_then_it_should_return_expected_tax():
    product = Product('1', 'book', 19.9, INFO_BOOK)
    issue_date = datetime(2021, 10, 29, 15, 5, 44, 343)
    tax_calculator = TaxCalculator(issue_date)
    taxes = tax_calculator.calculate(product, 2)
    assert taxes == Monetary(0.4)

def test_given_a_book_when_calculate_tax_on_november_then_it_should_return_expected_tax():
    product = Product('1', 'book', 19.9, INFO_BOOK)
    issue_date = datetime(2021, 11, 29, 15, 5, 44, 343)
    tax_calculator = TaxCalculator(issue_date)
    taxes = tax_calculator.calculate(product, 2)
    assert taxes == Monetary(0.04)

def test_given_a_medical_product_when_calculate_tax_on_default_month_then_it_should_return_expected_tax():
    product = Product('2', 'pff2 mask', 2.8, INFO_PFF2_MASK)
    issue_date = datetime(2021, 10, 29, 15, 5, 44, 343)
    tax_calculator = TaxCalculator(issue_date)
    taxes = tax_calculator.calculate(product, 2)
    assert taxes == Monetary(0.0056)

def test_given_a_medical_product_when_calculate_tax_on_november_then_it_should_return_expected_tax():
    product = Product('2', 'pff2 mask', 2.8, INFO_PFF2_MASK)
    issue_date = datetime(2021, 11, 29, 15, 5, 44, 343)
    tax_calculator = TaxCalculator(issue_date)
    taxes = tax_calculator.calculate(product, 2)
    assert taxes == Monetary(0)

def test_given_a_home_category_product_when_calculate_tax_on_default_month_then_it_should_return_expected_tax():
    product = Product('3', 'vacuum cleaner', 227.99, INFO_VACUUM_CLEANER)
    issue_date = datetime(2021, 10, 29, 15, 5, 44, 343)
    tax_calculator = TaxCalculator(issue_date)
    taxes = tax_calculator.calculate(product, 1)
    assert taxes == Monetary(22.799)

def test_given_a_home_category_product_when_calculate_tax_on_november_then_it_should_return_expected_tax():
    product = Product('3', 'vacuum cleaner', 227.99, INFO_VACUUM_CLEANER)
    issue_date = datetime(2021, 11, 29, 15, 5, 44, 343)
    tax_calculator = TaxCalculator(issue_date)
    taxes = tax_calculator.calculate(product, 1)
    assert taxes == Monetary(2.2799)
