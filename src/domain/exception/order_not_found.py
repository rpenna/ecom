class OrderNotFound(Exception):
    def __init__(self, message='The order does not exist'):
        super().__init__(message)
