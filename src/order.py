from .invalid_cpf import InvalidCpf
from .validator import Validator

class Order:
    def __init__(self, cpf: str):
        self.__cpf = cpf
        self.__cart = []
        self.__discount = 0
        self.__validator = Validator()

    def __to_money(self, value: float) -> float:
        """Receives a floating value and returns it rounded by 2, representing
        monetary value

        Args:
            value (float): Value to be converted

        Returns:
            float: monetary value
        """
        return round(value, 2)

    def add_to_cart(self, description: str, price: float, quantity: int) -> float:
        """Add new product to the order, returning the total price of the 
        product

        Args:
            description (str): Description of the product
            price (float): price of the product
            quantity (int): quantity of products added

        Returns:
            float: total price of the product
        """
        self.__cart.append(
            {
                'description': description,
                'price': price,
                'quantity': quantity
            }
        )
        return self.__to_money(price * quantity)

    def add_discount_coupon(self, code: str) -> float:
        """Add discount to the order

        Args:
            code (str): coupon id

        Returns:
            float: discount percentage applied
        """
        if code.lower() in ('10offcoupon'):
            self.__discount = 10
        else:
            self.__discount = 0
        return self.__discount

    def __validate_cpf(self) -> None:
        """Validates CPF

        Raises:
            InvalidCpf: if CPF is not valid

        Returns:
            None: No return
        """
        if not self.__validator.validate_cpf(self.__cpf):
            raise InvalidCpf

    def __make_summary(self, order_price: float) -> dict:
        """Having the order price, produces the order summary

        Args:
            order_price (float): Sum of all the products bought

        Returns:
            dict: summary formatted
        """
        total = order_price - (order_price * (self.__discount/100))
        return {
            'items': self.__cart,
            'order_price': self.__to_money(order_price),
            'discount_percentage': self.__discount,
            'total': self.__to_money(total)
        }

    def close_order(self) -> dict:
        """Close order for buying products added to cart, if CPF informed
        is valid

        Raises:
            InvalidCpf: CPF received is not valid

        Returns:
            dict: order summary
        """
        self.__validate_cpf()
        order_price = 0
        for product in self.__cart:
            order_price += product['price'] * product['quantity']
        return self.__make_summary(order_price)
