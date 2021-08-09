from datetime import datetime, timedelta

from .coupon import Coupon
from .order import Order
from .product import Product
from .place_order_input import PlaceOrderInput
from .place_order_output import PlaceOrderOutput
from .shipping_calculator import ShippingCalculator
from .product_not_found import ProductNotFound
from.coupon_not_found import CouponNotFound

BOOK = Product('1', 'book', 19.9, {
    'height': 15,
    'width': 10,
    'depth': 2,
    'weight': 1000
})

PFF2_MASK = Product('2', 'pff2 mask', 2.8, {
    'height': 10,
    'width': 10,
    'depth': 0.01,
    'weight': 50
})
VACUUM_CLEANER = Product('3', 'vacuum cleaner', 227.99, {
    'height': 40,
    'width': 30,
    'depth': 30,
    'weight': 5000
})

NOT_EXPIRED_DATE = datetime.now() + timedelta(days=1)
EXPIRED_DATE = datetime.now() + timedelta(days=1)

VALID_COUPON15 = Coupon('15OFF', 15, NOT_EXPIRED_DATE)
INVALID_COUPON15 = Coupon('15OFFINVALID', 15, EXPIRED_DATE)
VALID_COUPON10 = Coupon('10OFF', 15, NOT_EXPIRED_DATE)
INVALID_COUPON10 = Coupon('10OFFINVALID', 15, EXPIRED_DATE)

class PlaceOrder:
    def __init__(self):
        self.__order = None
        self.__products = [
            BOOK,
            PFF2_MASK,
            VACUUM_CLEANER
        ]
        self.__coupons = [
            VALID_COUPON15,
            INVALID_COUPON15,
            VALID_COUPON10,
            INVALID_COUPON10
        ]

    def __get_product_by_id(self, id: str) -> Product:
        """Search for product using its ID

        Args:
            id (str): product's id

        Raises:
            ProductNotFound: when product was not found

        Returns:
            Product: Product found
        """
        for product in self.__products:
            if product.id == id:
                return product
        raise ProductNotFound

    def __get_coupon_by_code(self, code: str) -> Coupon:
        """Search for coupon by code

        Args:
            code (str): Coupon's code

        Raises:
            CouponNotFound: when coupon was not found

        Returns:
            Coupon: Coupon found
        """
        for coupon in self.__coupons:
            if coupon.code == code.upper():
                return coupon
        raise CouponNotFound

    def __add_product_to_cart(self, product: Product, quantity: int) -> None:
        """Add products to the cart

        Args:
            products (Product): product available to be ordered
            quantity (int): quantity of products to be ordered

        Returns:
            None: no return expected
        """
        self.__order.add_to_cart(
            product.id,
            product.price,
            quantity
        )

    def __apply_discount(self, coupon: Coupon) -> None:
        """Apply the discount informed by the coupon

        Args:
            coupon (Coupon): Coupon received from DTO

        Returns:
            None: no return expected
        """
        coupon = self.__get_coupon_by_code(coupon)
        self.__order.add_discount_coupon(coupon)

    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        """Place order according to the DTO received

        Args:
            input (PlaceOrderInput): DTO of the order

        Returns:
            PlaceOrderOutput: Same content as DTO, but including the 'total'
            key, which informs the total amount of the order.
        """
        self.__order = Order(input.cpf)
        distance = 1000
        for product in input.products:
            available_product = self.__get_product_by_id(product.get('id'))
            quantity = product.get('quantity')
            self.__add_product_to_cart(available_product, quantity)
            self.__order.shipping_fee += ShippingCalculator.calculate(distance, available_product) * quantity
        if input.coupon is not None:
            self.__apply_discount(input.coupon)
        return PlaceOrderOutput(self.__order.get_total(), self.__order.shipping_fee)
