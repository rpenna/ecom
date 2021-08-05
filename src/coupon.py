from datetime import datetime

class Coupon:
    def __init__(self, code: str, discount_percentage: float, expiring_date: datetime):
        self.__code = code
        self.__discount_percentage = discount_percentage
        self.__expiring_date = expiring_date

    @property
    def discount_percentage(self):
        return self.__discount_percentage

    def is_expired(self) -> bool:
        """Verifies if coupon has an expired date.

        Returns:
            bool: True if is expired
        """
        return datetime.now() > self.__expiring_date
