class Product:
    def __init__(self, description: str, price: float, quantity: int, info: dict):
        self.__description = description
        self.__price = price
        self.__quantity = quantity
        self.__info = info
        self.__volume = None
        self.__density = None

    @property
    def description(self):
        return self.__description

    def get_volume(self) -> float:
        """Calculate the product volume according to its dimensions

        Returns:
            float: product's volume in m^3
        """
        height = self.__info['height'] / 100
        width = self.__info['width'] / 100
        depth = self.__info['depth'] / 100
        self.__volume = height * width * depth
        return self.__volume

    def get_density(self) -> float:
        """Calculates the product density according to its weight and volume.

        Returns:
            float: density in kg/m^3
        """
        if self.__volume is None:
            self.get_volume()
        weight = self.__info['weight'] / 1000
        self.__density = weight / self.__volume
        return self.__density

    def get_total(self) -> float:
        """Calculates total price of the product according to its price and 
        quantity

        Returns:
            float: Total price
        """
        return self.__price * self.__quantity
