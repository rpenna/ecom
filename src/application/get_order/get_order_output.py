import math


class GetOrderOutput:
    def __init__(self, order: dict):
        self.__order = order

    @property
    def code(self):
        return self.__order.get("code")

    @property
    def total_price(self):
        total = math.ceil(self.__order.get("total_price"))
        return f"{total // 100}.{total % 100}"

    @property
    def issue_date(self):
        return self.__order.get("issue_date")

    @property
    def products(self):
        return self.__order.get("products")

    @property
    def tax(self):
        return self.__order.get("tax")
