class OutOfStock(Exception):
    def __init__(self, message='This product is out of stock'):
        super().__init__(message)
