import re
from flask import Flask
from .http import Http
from .order_view import OrderView

class FlaskHttp(Http):
    def __init__(self):
        self.__app = Flask('ecom')
        Http.__init__(self)
        self.__adapt_routes()

    def __convert_url(self, url: str) -> str:
        """Adapt received URL to the Flask URL format

        Args:
            url (str): URL received as expected by Http interface

        Returns:
            str: adapted URL
        """
        open_param = re.compile('\$\{')
        close_param = re.compile('\}')
        adapted_url = re.sub(open_param, '<', url)
        return re.sub(close_param, '>', adapted_url)

    def __adapt_routes(self) -> None:
        """Converts all routes to flask style"""
        for view in self.routes.keys():
            route = self.routes[view]['route']
            self.routes[view]['route'] = self.__convert_url(route)
        
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
