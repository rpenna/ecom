import abc
from ..repository.order_repository import OrderRepository
from ..repository.product_repository import ProductRepository
from ..repository.coupon_repository import CouponRepository

class RepositoryAbstractFactory(metaclass=abc.ABCMeta):
    def make_order_repository(self) -> OrderRepository:
        raise NotImplementedError

    def make_product_repository(self) -> ProductRepository:
        raise NotImplementedError
    
    def make_coupon_repository(self) -> CouponRepository:
        raise NotImplementedError
