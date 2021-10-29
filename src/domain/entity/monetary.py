from decimal import Decimal, ROUND_HALF_UP

class Monetary:
    """Value Object that represents money"""
    def __init__(self, value: float = 0):
        self.__value = self.__transform(float(value))

    def __eq__(self, other) -> bool:
        return self.__value == other.value

    def __ne__(self, other) -> bool:
        return self.__value != other.value

    def __lt__(self, other) -> bool:
        return self.__value < other.value

    def __le__(self, other) -> bool:
        return self.__value <= other.value

    def __gt__(self, other) -> bool:
        return self.__value > other.value

    def __ge__(self, other) -> bool:
        return self.__value >= other.value

    def __repr__(self) -> str:
        return str(self.__value)

    @property
    def value(self):
        return self.__value

    def __transform(self, value: float) -> Decimal:
        """Receives a floating value and returns it rounded by 2, representing
        monetary value

        Args:
            value (float): Value to be converted

        Returns:
            Decimal: monetary value
        """
        amount = Decimal(value)
        cents = Decimal('.01')
        return amount.quantize(cents, ROUND_HALF_UP)
