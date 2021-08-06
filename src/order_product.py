class OrderProduct:
    def __init__(self, description: str, price: float, quantity: int, info: dict):
        self.__description = description
        self.__price = price
        self.__quantity = quantity
        self.__info = info
        self.__volume = None
        self.__density = None

    def get_total(self) -> float:
        """Calculates total price of the product according to its price and 
        quantity

        Returns:
            float: Total price
        """
        return self.__price * self.__quantity
