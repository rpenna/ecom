import asyncpg
from ....domain.entity.coupon import Coupon
from ....domain.repository.coupon_repository import CouponRepository
from ....domain.exception.coupon_not_found import CouponNotFound


class CouponRepositoryPostgresql(CouponRepository):
    def __init__(self, pg_connection: asyncpg.Connection):
        self.__conn = pg_connection

    async def get_by_code(self, code: str) -> Coupon:
        query = """
            SELECT code, discount_percentage, expiring_date
            FROM ecom.coupons
            WHERE code = $1
        """
        coupon_data = await self.__conn.fetch_row(query, code)
        return Coupon(
            coupon_data["code"],
            coupon_data["discount_percentage"],
            coupon_data["expiring_date"],
        )
