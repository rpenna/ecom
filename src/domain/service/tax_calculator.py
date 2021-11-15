from datetime import datetime
from abc import ABC, abstractmethod

from ..entity.product import Product
from ..entity.monetary import Monetary

class TaxCalculator(ABC):
    @abstractmethod
    def get_tax(self, product: str) -> float:
        """Get tax according to the month

        Args:
            product (str): product description

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
        tax = self.get_tax(product.description)
        taxes = (product.price * quantity) * tax
        return Monetary(taxes)
