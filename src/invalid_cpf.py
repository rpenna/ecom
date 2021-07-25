class InvalidCpf(Exception):
    def __init__(self, message='Invalid CPF'):
        super().__init__(message)
