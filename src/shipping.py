class Shipping:
    def __init__(self, distance: float, products: list):
        """Constructor

        Args:
            distance (float): Distance from storage to delivery address
            products (list): list containing Product objects
        """
        self.__distance = distance
        self.__products = products

    def get_total(self) -> float:
        """Calculate shipping fee

        Returns:
            float: total fee
        """
        total_fee = 0
        for product in self.__products:
            volume = product.get_volume()
            density = product.get_density()
            total_fee += self.__distance * volume * (density/100)
        return total_fee
