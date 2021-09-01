class GetOrderOutput:
    def __init__(self, order: dict):
        self. __order = order

    @property
    def code(self):
        return self.__order.get('code')

    @property
    def total_price(self):
        return self.__order.get('total_price')

    @property
    def issue_date(self):
        return self.__order.get('issue_date')
    
    @property
    def products(self):
        return self.__order.get('products')