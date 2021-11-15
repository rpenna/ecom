from abc import ABC, abstractmethod

from ..entity.product import Product
from ..entity.monetary import Monetary
from ..repository.taxes_repository import TaxesRepository

class TaxCalculator(ABC):

    def __init__(self, taxes_table: TaxesRepository):
        self.taxes_table = taxes_table

    @abstractmethod
    def get_tax(self, product_id: str) -> float:
        """Get tax according to the month

        Args:
            product_id (str): product ID

        Returns:
            float: Tax
        """
        raise NotImplementedError

    def calculate(self, product: Product, quantity: int) -> Monetary:
        """Calculate taxes for the specified product and its quantity

        Args:
            product (Product): product ordered
            quantity (int): quantity of products ordered

        Returns:
            Monetary: Taxes calculated
        """
        tax = self.get_tax(product.id)
        taxes = (product.price * quantity) * tax
        return Monetary(taxes)
