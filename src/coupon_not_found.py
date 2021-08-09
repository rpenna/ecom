class CouponNotFound(Exception):
    def __init__(self, message='Coupon not found'):
        super().__init__(message='Coupon not found')
