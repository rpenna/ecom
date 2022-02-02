from ...domain.repository.coupon_repository import CouponRepository
from ...domain.repository.order_repository import OrderRepository
from ...domain.repository.product_repository import ProductRepository
from ...domain.repository.stock_repository import StockRepository
from ...domain.repository.taxes_repository import TaxesRepository
from ...domain.factory.repository_abstract_factory import RepositoryAbstractFactory
from ..repository.postgresql.order_repository_postgresql import (
    OrderRepositoryPostgresql,
)
from ..repository.postgresql.product_repository_postgresql import (
    ProductRepositoryPostgresql,
)
from ..repository.postgresql.coupon_repository_postgresql import (
    CouponRepositoryPostgresql,
)
from ..repository.postgresql.taxes_repository_postgresql import (
    TaxesRepositoryPostgresql,
)
from ..repository.postgresql.stock_repository_postgresql import (
    StockRepositoryPostgresql,
)


class PostgresqlRepositoryFactory(RepositoryAbstractFactory):
    def make_order_repository(self) -> OrderRepository:
        return OrderRepositoryPostgresql()

    def make_product_repository(self) -> ProductRepository:
        return ProductRepositoryPostgresql()

    def make_coupon_repository(self) -> CouponRepository:
        return CouponRepositoryPostgresql()

    def make_taxes_repository(self) -> TaxesRepository:
        return TaxesRepositoryPostgresql()

    def make_stock_repository(self) -> StockRepository:
        return StockRepositoryPostgresql()
