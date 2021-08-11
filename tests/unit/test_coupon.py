import pytest
from datetime import datetime, timedelta

from ...src.domain.entity.coupon import Coupon

def test_expired_coupon_should_be_expired():
    expired_date = datetime.now() - timedelta(days=1)
    coupon = Coupon('expired_coupon', 15, expired_date)
    assert coupon.is_expired()

def test_valid_coupon_should_not_be_expired():
    not_expired_date = datetime.now() + timedelta(days=1)
    coupon = Coupon('not_expired_coupon', 10, not_expired_date)
    assert coupon.is_expired() == False
