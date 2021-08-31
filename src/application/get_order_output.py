from ..domain.entity.order import Order

class GetOrderOutput:
    def __init__(self, order: Order):
        self. __order = order

    @property
    def code(self):
        return self.__order.code

    @property
    def total_price(self):
        return self.__order.get_total_price()
