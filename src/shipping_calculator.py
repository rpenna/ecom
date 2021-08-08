from .product import Product

MINIMUM_FEE = 10

class ShippingCalculator:
    @staticmethod
    def calculate(distance: float, product: Product) -> float:
        """Calculate shipping fee

        Args:
            distance (float): distance between storage and destination address
            product (Product): product to be shipped

        Returns:
            float: total fee
        """
        total_fee = 0
        volume = product.get_volume()
        density = product.get_density()
        total_fee += distance * volume * (density/100)
        return total_fee if total_fee > MINIMUM_FEE else MINIMUM_FEE
