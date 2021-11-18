from abc import ABC, abstractmethod

from ..entity.order_product import OrderProduct
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

    def calculate(self, product: OrderProduct) -> Monetary:
        """Calculate taxes for the specified product and its quantity

        Args:
            product (OrderProduct): product ordered

        Returns:
            Monetary: Taxes calculated
        """
        tax = self.get_tax(product.id)
        taxes = (product.price * product.quantity) * tax
        return Monetary(taxes)
