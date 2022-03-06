from datetime import datetime
from ...database.postgresql_connection import PostgresConnection
from ....domain.repository.order_repository import OrderRepository
from ....domain.entity.order import Order
from ....domain.entity.coupon import Coupon
from ....domain.exception.order_not_found import OrderNotFound


class OrderRepositoryPostgresql(OrderRepository):
    def __init__(self, conn: PostgresConnection):
        self.__conn = conn

    def count_by_year(self, issue_date: datetime) -> str:
        query = """
            select count(*) AS total
            from ecom.orders
            where extract(year from issue_date) = %s
        """
        parameters = (issue_date.year,)
        total = self.__conn.query_one(query, parameters).get("total")
        if total is not None:
            return str(total)
        return "0"

    def save(self, order: Order) -> bool:
        query = """
            insert into ecom.orders (
                cpf,
                issue_date,
                code,
                coupon_code,
                shipping_fee
            )
            values (%s, %s, %s, %s, %s)
        """
        parameters = (
            order.cpf,
            order.issue_date,
            order.code,
            order.coupon.code,
            order.shipping_fee,
        )
        self.__conn.execute(query, parameters)
        for product in order.cart:
            query = """
                insert into ecom.order_product (
                    product_id,
                    order_code,
                    quantity,
                    price
                )
                values (%s, %s, %s, %s)
            """
            parameters = (product.id, order.code, product.quantity, product.price)
            if not self.__conn.execute(query, parameters) == 1:
                return False
        return True

    def get_by_code(self, code: str) -> Order:
        query = """
            select
                cpf,
                issue_date,
                coupon_code,
                shipping_fee,
                discount_percentage,
                expiring_date
            from ecom.orders as orders
                left join ecom.coupons as coupons
                    on orders.coupon_code = coupons.code
            where orders.code = %s
        """
        parameters = (code,)
        order_data = self.__conn.query_one(query, parameters)
        year_count = int(code[-8:])
        order = Order(order_data["cpf"], order_data["issue_date"], year_count)
        if not order:
            raise OrderNotFound
        if order_data["coupon_code"] is not None:
            coupon = Coupon(
                order_data["coupon_code"],
                order_data["discount_percentage"],
                order_data["expiring_date"],
            )
            order.add_discount_coupon(coupon)
        products_query = """
            select product_id, price, quantity
            from ecom.order_product
            where order_code = %s
        """
        products_parameters = (code,)
        products = self.__conn.query_many(products_query, products_parameters)
        for product in products:
            order.add_to_cart(product["id"], product["price"], product["quantity"])
        order.shipping_fee = order_data["shipping_fee"]
        return order

    def clear(self):
        query = """
            delete from ecom.orders
        """
        self.__conn.execute(query)
