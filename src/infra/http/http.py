from abc import abstractmethod
from ...domain.exception.order_not_found import OrderNotFound
from ...application.get_order import GetOrder
from ..factory.memory_repository_factory import MemoryRepositoryFactory

class Http:
    def __init__(self):
        self.__repository_factory = MemoryRepositoryFactory()
        self.routes = {
            'order': {
                'route': '/order/${code}',
                'views': [
                    {
                        'method': 'get',
                        'function': self.get_order
                    }
                ]
            }
        }

    def get_order(self, code: str) -> tuple([dict, int]):
        """Get order by its code

        Args:
            code (str): URL parameters

        Returns:
            tuple(dict, int): content of the order and its status
        """
        try:
            get_order = GetOrder(self.__repository_factory)
            order = get_order.execute(code)
            return {
                'code': order.code,
                'issue_date': order.issue_date,
                'total': order.total_price,
                'products': order.products,
            }, 200
        except OrderNotFound:
            return {}, 422
        except KeyError:
            return {}, 400

    @abstractmethod
    def build() -> None:
        """Builds HTTP routes"""
        raise NotImplementedError()

    @abstractmethod
    def run() -> None:
        """Runs server"""
        raise NotImplementedError()
