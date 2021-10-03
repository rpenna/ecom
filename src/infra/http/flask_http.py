import re
from flask import Flask
from .http import Http
from .order_view import OrderView

class FlaskHttp(Http):
    def __init__(self):
        self.__app = Flask('ecom')

    def build(self) -> None:
        order_view = OrderView.as_view('order')
        self.__app.add_url_rule(
            '/order/<code>',
            view_func=order_view,
            methods=['GET']
        )
        self.__app.add_url_rule(
            '/order',
            view_func=order_view,
            methods=['POST']
        )

    def run(self) -> None:
        self.__app.run('0.0.0.0', port=3000)
