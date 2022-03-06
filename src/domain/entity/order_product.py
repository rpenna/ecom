class OrderProduct:
    def __init__(self, id: str, price: float, quantity: int):
        self.__id = id
        self.__price = price
        self.__quantity = quantity

    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price

    @property
    def quantity(self):
        return self.__quantity

    def get_total(self) -> int:
        """Calculates total price of the product according to its price and
        quantity

        Returns:
            int: Total price
        """
        return self.__price * self.__quantity
