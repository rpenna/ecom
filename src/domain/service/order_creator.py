from ..factory.repository_abstract_factory import RepositoryAbstractFactory
from ..gateway.zipcode_distance_calculator_api import ZipcodeDistanceCalculatorApi
from ..entity.order import Order
from ..entity.product import Product
from ..service.shipping_calculator import ShippingCalculator
from ..exception.coupon_not_found import CouponNotFound

class OrderCreator:
    def __init__(self, repository_factory: RepositoryAbstractFactory, zipcode_calculator: ZipcodeDistanceCalculatorApi):
        self.__order = None
        self.__zipcode_calculator = zipcode_calculator
        self.__product_repository = repository_factory.make_product_repository()
        self.__coupon_repository = repository_factory.make_coupon_repository()
        self.__order_repository = repository_factory.make_order_repository()

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

    def create(self, order_data: dict) -> Order:
        """Create new order

        Args:
            order_data (dict): new order content

        Returns:
            Order: order created
        """
        year_count = self.__order_repository.count_by_year(
            order_data['issue_date']
        )
        self.__order = Order(
            order_data['cpf'],
            order_data['issue_date'],
            year_count
        )
        distance = self.__zipcode_calculator.calculate(order_data['zipcode'])
        for product in order_data['products']:
            added_product = self.__add_product_to_cart(
                product.get('id'),
                product.get('quantity')
            )
            self.__apply_shipping_cost(
                distance,
                added_product,
                product.get('quantity')
            )
        if order_data['coupon'] is not None:
            self.__apply_discount(order_data['coupon'])
        self.__order_repository.save(self.__order)
        return self.__order