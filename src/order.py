from decimal import Decimal, ROUND_HALF_UP

from .coupon import Coupon
from .product import Product
from .cpf import Cpf

class Order:
    def __init__(self, cpf: str):
        self.__cpf = Cpf(cpf)
        self.__cart = []
        self.__coupon = None

    @property
    def cpf(self):
        return self.__cpf.value

    def __to_money(self, value: float) -> Decimal:
        """Receives a floating value and returns it rounded by 2, representing
        monetary value

        Args:
            value (float): Value to be converted

        Returns:
            Decimal: monetary value
        """
        amount = Decimal(value)
        cents = Decimal('.01')
        return amount.quantize(cents, ROUND_HALF_UP)

    def add_to_cart(self, description: str, price: float, quantity: int) -> float:
        """Add new product to the order, returning the total price of the 
        product

        Args:
            description (str): Description of the product
            price (float): price of the product
            quantity (int): quantity of products added

        Raises:
            ProductUnavailable: not enough products availabe on inventory

        Returns:
            float: total price of the product
        """
        product = Product(description, price, quantity)
        self.__cart.append(product)

    def add_discount_coupon(self, coupon: Coupon) -> None:
        """Add discount to the order

        Args:
            coupon (Coupon): coupon to be added
        """
        self.__coupon = coupon

    def get_total(self):
        """Calculate the current total price of the order

        Returns:
            float: total price
        """
        total = 0
        for product in self.__cart:
            total += product.get_total()
        if self.__coupon is not None:
            total = self.__coupon.apply_discount(total)
        return self.__to_money(total)
