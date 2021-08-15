from .place_order_input import PlaceOrderInput
from .place_order_output import PlaceOrderOutput
from ..domain.entity.order import Order
from ..domain.entity.product import Product
from ..domain.repository.product_repository import ProductRepository
from ..domain.repository.coupon_repository import CouponRepository
from ..domain.service.shipping_calculator import ShippingCalculator
from ..domain.exception.product_not_found import ProductNotFound
from ..domain.exception.coupon_not_found import CouponNotFound
from ..infra.gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

class PlaceOrder:
    def __init__(self, product_repository: ProductRepository, coupon_repository: CouponRepository):
        self.__order = None
        self.__zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
        self.__product_repository = product_repository
        self.__coupon_repository = coupon_repository

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
        """Place order according to the DTO received

        Args:
            input (PlaceOrderInput): DTO of the order

        Returns:
            PlaceOrderOutput: Same content as DTO, but including the 'total'
            key, which informs the total amount of the order.
        """
        self.__order = Order(input.cpf)
        distance = self.__zipcode_calculator.calculate(input.zipcode)
        for product in input.products:
            id = product.get('id')
            available_product = self.__product_repository.get_by_id(id)
            quantity = product.get('quantity')
            self.__add_product_to_cart(available_product, quantity)
            self.__order.shipping_fee += ShippingCalculator.calculate(distance, available_product) * quantity
        if input.coupon is not None:
            self.__apply_discount(input.coupon)
        return PlaceOrderOutput(self.__order.get_total(), self.__order.shipping_fee)
