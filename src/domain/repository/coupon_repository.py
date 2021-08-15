import abc
from ..entity.coupon import Coupon

class CouponRepository(metaclass=abc.ABCMeta):
    def get_by_code(self, code: str) -> Coupon:
        """Search for coupon using a coupon code

        Args:
            code (str): coupon code

        Raises:
            CouponNotFound: Coupon not found

        Returns:
            Coupon: coupon that was found
        """
        raise NotImplementedError
