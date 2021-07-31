from .coupon import Coupon
from .order import Order

class PlaceOrder:
    def execute(self, data: dict) -> dict:
        order = Order(data.get('cpf', ''))
        for product in data.get('cart', []):
            order.add_to_cart(
                product.get('description'),
                product.get('price'),
                product.get('quantity')
            )
        if 'coupon' in data:
            code = data['coupon'].get('code')
            discount = data['coupon'].get('discount')
            coupon = Coupon(code, discount)
            order.add_discount_coupon(coupon)
        summary = data
        summary['total'] = order.get_total()
        return summary
