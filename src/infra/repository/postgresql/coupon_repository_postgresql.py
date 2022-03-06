from ...database.postgresql_connection import PostgresConnection
from ....domain.entity.coupon import Coupon
from ....domain.repository.coupon_repository import CouponRepository
from ....domain.exception.coupon_not_found import CouponNotFound


class CouponRepositoryPostgresql(CouponRepository):
    def __init__(self, pg_connection: PostgresConnection):
        self.__conn = pg_connection

    def get_by_code(self, code: str) -> Coupon:
        query = """
            SELECT code, discount_percentage, expiring_date
            FROM ecom.coupons
            WHERE code = %s
        """
        parameters = (code,)
        coupon_data = self.__conn.query_one(query, parameters)
        if not coupon_data:
            raise CouponNotFound
        return Coupon(
            coupon_data["code"],
            coupon_data["discount_percentage"],
            coupon_data["expiring_date"],
        )
