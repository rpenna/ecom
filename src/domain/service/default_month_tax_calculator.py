from .tax_calculator import TaxCalculator

class DefaultMonthTaxCalculator(TaxCalculator):
    def get_tax(self, product: str) -> float:
        if product == 'book':
            return 1/100
        if product == 'pff2 mask':
            return 0.1/100
        if product == 'vacuum cleaner':
            return 10/100
