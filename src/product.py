class Product:
    def __init__(self, description: str, price: float, quantity: int):
        self.__description = description
        self.__price = price
        self.__quantity = quantity

    @property
    def description(self):
        return self.__description

    def get_total(self):
        return self.__price * self.__quantity
