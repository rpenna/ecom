from .coupon import Coupon
from .order import Order

class PlaceOrder:
    def __init__(self):
        self.__order = None

    def __add_products_to_cart(self, products: list) -> None:
        """Add all products listed to the cart

        Args:
            products (list): products received via DTO

        Returns:
            None: no return expected
        """
        for product in products:
            self.__order.add_to_cart(
                product.get('description'),
                product.get('price'),
                product.get('quantity'),
                product.get('info')
            )

    def __apply_discount(self, coupon: dict) -> None:
        """Apply the discount informed by the coupon

        Args:
            coupon (dict): Coupon received from DTO

        Returns:
            None: no return expected
        """
        code = coupon.get('code')
        discount = coupon.get('discount')
        expiring_date = coupon.get('expiring_date')
        coupon = Coupon(code, discount, expiring_date)
        self.__order.add_discount_coupon(coupon)

    def execute(self, data: dict) -> dict:
        """Place order according to the DTO received

        Args:
            data (dict): DTO of the order

        Returns:
            dict: Same content as DTO, but including the 'total' key, which 
            informs the total amount of the order.
        """
        self.__order = Order(data.get('cpf', ''))
        self.__add_products_to_cart(data.get('cart', []))
        if 'coupon' in data:
            self.__apply_discount(data['coupon'])
        distance = 1000
        summary = data
        summary['total'] = self.__order.get_total(distance)
        return summary
