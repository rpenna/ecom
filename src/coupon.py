from datetime import datetime

class Coupon:
    def __init__(self, code: str, discount_percentage: float, expiring_date: datetime):
        self.__code = code
        self.__discount_percentage = discount_percentage
        self.__expiring_date = expiring_date

    def __is_coupon_expired(self) -> bool:
        """Verifies if coupon has an expired date.

        Returns:
            bool: True if is expired
        """
        return datetime.now() > self.__expiring_date

    def apply_discount(self, amount: float) -> float:
        if self.__is_coupon_expired():
            return amount
        discount_factor = self.__discount_percentage/100
        return amount * (1 - discount_factor)