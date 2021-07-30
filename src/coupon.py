class Coupon:
    def __init__(self, code: str, discount_percentage: float):
        self.__code = code
        self.__discount_percentage = discount_percentage

    def apply_discount(self, amount: float) -> float:
        discount_factor = self.__discount_percentage/100
        return amount * (1 - discount_factor)