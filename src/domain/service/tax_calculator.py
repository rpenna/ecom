from datetime import datetime

from ..entity.product import Product
from ..entity.monetary import Monetary

class TaxCalculator:
    def __init__(self, issue_date: datetime) -> None:
        self.__issue_date = issue_date

    def calculate(self, product: Product, quantity: int) -> Monetary:
        taxes = 0
        if 'book' in product.description.lower():
            tax = 1/100
            if self.__issue_date.month == 11:
                tax = 0.1/100
            taxes = (product.price * quantity) * tax
        if 'pff2 mask' in product.description.lower():
            tax = 0.1/100
            if self.__issue_date.month == 11:
                print('arrived')
                tax = 0
            taxes = (product.price * quantity) * tax
        if 'vacuum cleaner' in product.description.lower():
            tax = 10/100
            if self.__issue_date.month == 11:
                tax = 1/100
            taxes = (product.price * quantity) * tax
        return Monetary(taxes)
