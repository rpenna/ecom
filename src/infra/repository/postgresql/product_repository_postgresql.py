from inspect import Parameter
from ...database.postgresql_connection import PostgresConnection
from ....domain.entity.product import Product
from ....domain.exception.product_not_found import ProductNotFound
from ....domain.repository.product_repository import ProductRepository


class ProductRepositoryPostgresql(ProductRepository):
    def __init__(self, conn: PostgresConnection):
        self.__conn = conn

    def get_by_id(self, id: str) -> Product:
        query = """
            select 
                id,
                description,
                price,
                height,
                width,
                depth,
                weight
            from ecom.products
            where id = %s
        """
        parameters = (id,)
        product = self.__conn.query_one(query, parameters)
        if product is None:
            raise ProductNotFound
        infos = {
            "height": product["height"],
            "width": product["width"],
            "depth": product["depth"],
            "weight": product["weight"],
        }
        return Product(product["id"], product["description"], product["price"], infos)
