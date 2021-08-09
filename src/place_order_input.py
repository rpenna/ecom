class PlaceOrderInput:
    def __init__(self, cpf: str, products: list, zipcode: str, coupon: str = None):
        self.__cpf = cpf
        self.__products = products
        self.__zipcode = zipcode
        self.__coupon = coupon

    @property
    def cpf(self):
        return self.__cpf

    @property
    def products(self):
        return self.__products

    @property
    def coupon(self):
        return self.__coupon

    @property
    def zipcode(self):
        return self.__zipcode
