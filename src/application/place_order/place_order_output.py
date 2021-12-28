from ...domain.entity.order import Order

class PlaceOrderOutput:
    def __init__(self, order: Order):
        self.__order = order

    @property
    def total_price(self):
        return self.__order.get_total_price()

    @property
    def shipping_fee(self):
        return self.__order.shipping_fee

    @property
    def tax(self):
        return self.__order.tax

    @property
    def code(self):
        return self.__order.code
