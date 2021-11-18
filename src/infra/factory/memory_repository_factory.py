from ...domain.repository.coupon_repository import CouponRepository
from ...domain.repository.order_repository import OrderRepository
from ...domain.repository.product_repository import ProductRepository
from ...domain.factory.repository_abstract_factory import RepositoryAbstractFactory
from ..repository.memory.order_repository_memory import OrderRepositoryMemory
from ..repository.memory.product_repository_memory import ProductRepositoryMemory
from ..repository.memory.coupon_repository_memory import CouponRepositoryMemory
from ..repository.memory.taxes_repository_memory import TaxesRepositoryMemory

class MemoryRepositoryFactory(RepositoryAbstractFactory):
    def make_order_repository(self) -> OrderRepository:
        return OrderRepositoryMemory()

    def make_product_repository(self) -> ProductRepository:
        return ProductRepositoryMemory()

    def make_coupon_repository(self) -> CouponRepository:
        return CouponRepositoryMemory()

    def make_taxes_repository(self) -> TaxesRepositoryMemory:
        return TaxesRepositoryMemory()
