from datetime import datetime
from ..service.tax_calculator import TaxCalculator
from ..service.november_tax_calculator import NovemberTaxCalculator
from ..service.default_month_tax_calculator import DefaultMonthTaxCalculator

class TaxCalculatorFactory:
    @staticmethod
    def make(issue_date: datetime) -> TaxCalculator:
        if issue_date.month == 11:
            return NovemberTaxCalculator()
        return DefaultMonthTaxCalculator()
