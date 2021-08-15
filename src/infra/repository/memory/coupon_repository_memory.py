from datetime import datetime, timedelta

from ....domain.entity.coupon import Coupon
from ....domain.repository.coupon_repository import CouponRepository
from ....domain.exception.coupon_not_found import CouponNotFound

NOT_EXPIRED_DATE = datetime.now() + timedelta(days=1)
EXPIRED_DATE = datetime.now() + timedelta(days=1)

class CouponRepositoryMemory(CouponRepository):
    def __init__(self):
        self.__coupons = [
            Coupon('15OFF', 15, NOT_EXPIRED_DATE),
            Coupon('15OFFINVALID', 15, EXPIRED_DATE),
            Coupon('10OFF', 10, NOT_EXPIRED_DATE),
            Coupon('10OFFINVALID', 10, EXPIRED_DATE),
        ]

    def get_by_code(self, code: str) -> Coupon:
        """Search for coupon using a coupon code

        Args:
            code (str): coupon code

        Raises:
            CouponNotFound: Coupon not found

        Returns:
            Coupon: coupon that was found
        """
        for coupon in self.__coupons:
            if coupon.code == code:
                return coupon
        raise CouponNotFound
