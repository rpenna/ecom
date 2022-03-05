import math
from ...domain.entity.order import Order


class PlaceOrderOutput:
    def __init__(self, order: Order):
        self.__order = order

    @property
    def total_price(self):
        total = math.ceil(self.__order.get_total_price())
        return f"{total // 100}.{str(total % 100).zfill(2)}"

    @property
    def shipping_fee(self):
        shipping_fee = math.ceil(self.__order.shipping_fee)
        return f"{shipping_fee // 100}.{str(shipping_fee % 100).zfill(2)}"

    @property
    def tax(self):
        return self.__order.tax

    @property
    def code(self):
        return self.__order.code
