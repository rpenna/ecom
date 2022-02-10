import abc
from ..repository.order_repository import OrderRepository
from ..repository.product_repository import ProductRepository
from ..repository.coupon_repository import CouponRepository
from ..repository.taxes_repository import TaxesRepository
from ..repository.stock_repository import StockRepository


class RepositoryAbstractFactory(metaclass=abc.ABCMeta):
    def make_order_repository(self) -> OrderRepository:
        raise NotImplementedError

    def make_product_repository(self) -> ProductRepository:
        raise NotImplementedError

    def make_coupon_repository(self) -> CouponRepository:
        raise NotImplementedError

    def make_taxes_repository(self) -> TaxesRepository:
        raise NotImplementedError

    def make_stock_repository(self) -> StockRepository:
        raise NotImplementedError
