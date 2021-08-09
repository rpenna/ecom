from decimal import Decimal, ROUND_HALF_UP

from .coupon import Coupon
from .order_product import OrderProduct
from .cpf import Cpf

class Order:
    def __init__(self, cpf: str):
        self.__cpf = Cpf(cpf)
        self.__cart = []
        self.__coupon = None
        self.__shipping_fee = 0

    @property
    def cpf(self):
        return self.__cpf.value

    @property
    def shipping_fee(self) -> float:
        return self.__shipping_fee

    @shipping_fee.setter
    def shipping_fee(self, value: float) -> None:
        self.__shipping_fee = value

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

    def add_to_cart(self, id: str, price: float, quantity: int) -> float:
        """Add new product to the order, returning the total price of the 
        product
 
        Args:
            id (str): id of the product
            price (float): price of the product
            quantity (int): quantity of products added

        Raises:
            ProductUnavailable: not enough products availabe on inventory

        Returns:
            float: total price of the product
        """
        product = OrderProduct(id, price, quantity)
        self.__cart.append(product)

    def add_discount_coupon(self, coupon: Coupon) -> None:
        """Add discount to the order

        Args:
            coupon (Coupon): coupon to be added
        """
        if not coupon.is_expired():
            self.__coupon = coupon

    def __apply_discount(self, amount: float) -> float:
        """Applies discount related to the coupon

        Args:
            amount (float): value to be discounted

        Returns:
            float: discounted value
        """
        if self.__coupon is None:
            return amount
        percentage = self.__coupon.discount_percentage/100
        return amount * (1 - percentage)

    def get_total(self):
        """Calculate the current total price of the order

        Returns:
            float: total price
        """
        total = 0
        for product in self.__cart:
            total += product.get_total()
        total = self.__apply_discount(total)
        return self.__to_money(total)
