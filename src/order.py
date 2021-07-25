from .invalid_cpf import InvalidCpf
from .validator import Validator

class Order:
    def __init__(self, cpf: str):
        self.__cpf = cpf
        self.__products = []
        self.__discount = 0
        self.__validator = Validator()

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
        self.__products.append(
            {
                'description': description,
                'price': price,
                'quantity': quantity
            }
        )
        return round(price * quantity, 2)


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

    def close_order(self) -> dict:
        """Close order for buying products added to cart, if CPF informed
        is valid

        Raises:
            InvalidCpf: CPF received is not valid

        Returns:
            dict: order summary
        """
        if not self.__validator.validate_cpf(self.__cpf):
            raise InvalidCpf
        order_price = 0
        for product in self.__products:
            order_price += product['price'] * product['quantity']
        summary = {
            'items': self.__products,
            'order_price': round(order_price, 2),
            'discount_percentage': self.__discount,
            'total': round(order_price - (order_price * (self.__discount/100)), 2)
        }
        return summary
