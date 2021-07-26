class ProductUnavailable(Exception):
    def __init__(self, message='Product unavailable'):
        super().__init__(message)
