class OrderProduct:
    def __init__(self, id: str, price: float, quantity: int):
        self.__id = id
        self.__price = price
        self.__quantity = quantity

    def get_total(self) -> float:
        """Calculates total price of the product according to its price and 
        quantity

        Returns:
            float: Total price
        """
        return self.__price * self.__quantity
