from datetime import datetime

class StockOperation:

    def __init__(
        self,
        id: str,
        out: bool,
        quantity: int,
        operation_date: datetime
    ):
        self.__id = id
        self.__out = out
        self.__quantity = quantity
        self.__operation_date = operation_date

    @property
    def out(self):
        return self.__out

    @property
    def quantity(self):
        return self.__quantity

