from .tax_calculator import TaxCalculator

class NovemberTaxCalculator(TaxCalculator):
    def get_tax(self, product_id: str) -> float:
        return self.taxes_table.get_by_id_and_type(product_id, 'november')
