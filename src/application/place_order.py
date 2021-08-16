from .place_order_input import PlaceOrderInput
from .place_order_output import PlaceOrderOutput
from ..domain.entity.order import Order
from ..domain.entity.product import Product
from ..domain.repository.product_repository import ProductRepository
from ..domain.repository.coupon_repository import CouponRepository
from ..domain.repository.order_repository import OrderRepository
from ..domain.service.shipping_calculator import ShippingCalculator
from ..domain.exception.product_not_found import ProductNotFound
from ..domain.exception.coupon_not_found import CouponNotFound
from ..infra.gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

class PlaceOrder:
    def __init__(self, product_repository: ProductRepository, coupon_repository: CouponRepository, order_repository: OrderRepository):
        self.__order = None
        self.__zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
        self.__product_repository = product_repository
        self.__coupon_repository = coupon_repository
        self.__order_repository = order_repository

    def __add_product_to_cart(self, id: str, quantity: int) -> Product:
        """Add products to the cart

        Args:
            id (str): product's ID
            quantity (int): quantity of products to be ordered

        Returns:
            Product: product added to cart
        """
        available_product = self.__product_repository.get_by_id(id)
        self.__order.add_to_cart(
            id,
            available_product.price,
            quantity
        )
        return available_product

    def __apply_shipping_cost(self, distance: float, product: Product, quantity: int) -> None:
        """Add product's shipping fee to the order cost

        Args:
            distance (float): distance from the storage to the destination
            product (Product): Product to be shipped
            quantity (int): quantity of products

        Returns:
            None: No return expected
        """
        product_shipping_fee = ShippingCalculator.calculate(distance, product)
        self.__order.shipping_fee += product_shipping_fee * quantity

    def __apply_discount(self, code: str) -> None:
        """Apply the discount informed by the coupon code

        Args:
            code (str): Coupon code received from DTO

        Returns:
            None: no return expected
        """
        try:
            coupon = self.__coupon_repository.get_by_code(code)
            self.__order.add_discount_coupon(coupon)
        except CouponNotFound:
            pass

    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        """Place order according to the DTO received, saving the order created
        to the database.

        Args:
            input (PlaceOrderInput): DTO of the order

        Returns:
            PlaceOrderOutput: Created order output
        """
        self.__order = Order(input.cpf)
        distance = self.__zipcode_calculator.calculate(input.zipcode)
        for product in input.products:
            added_product = self.__add_product_to_cart(
                product.get('id'),
                product.get('quantity')
            )
            self.__apply_shipping_cost(
                distance,
                added_product,
                product.get('quantity')
            )
        if input.coupon is not None:
            self.__apply_discount(input.coupon)
        self.__order_repository.create(self.__order)
        return PlaceOrderOutput(self.__order.get_total(), self.__order.shipping_fee)
