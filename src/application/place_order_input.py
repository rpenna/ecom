from datetime import datetime

class PlaceOrderInput:
    def __init__(self, cpf: str, issue_date: datetime, products: list, zipcode: str, coupon: str = None):
        self.__cpf = cpf
        self.__issue_date = issue_date
        self.__products = products
        self.__zipcode = zipcode
        self.__coupon = coupon

    @property
    def cpf(self):
        return self.__cpf

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def products(self):
        return self.__products

    @property
    def coupon(self):
        return self.__coupon

    @property
    def zipcode(self):
        return self.__zipcode
