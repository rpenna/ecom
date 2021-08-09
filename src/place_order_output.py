class PlaceOrderOutput:
    def __init__(self, total: float, shipping_fee: float):
        self.__total = total
        self.__shipping_fee = shipping_fee

    @property
    def total(self):
        return self.__total

    @property
    def shipping_fee(self):
        return self.__shipping_fee
