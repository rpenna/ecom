from datetime import datetime
from ..service.tax_calculator import TaxCalculator
from ..service.november_tax_calculator import NovemberTaxCalculator
from ..service.default_month_tax_calculator import DefaultMonthTaxCalculator
from ..repository.taxes_repository import TaxesRepository

class TaxCalculatorFactory:
    @staticmethod
    def make(issue_date: datetime, taxes_table: TaxesRepository) -> TaxCalculator:
        if issue_date.month == 11:
            return NovemberTaxCalculator(taxes_table)
        return DefaultMonthTaxCalculator(taxes_table)
