import abc

from ..entity.product import Product

class ProductRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_id(self, id: str) -> Product:
        """Search product by ID

        Args:
            id (str): Id to be searched

        Raises:
            ProductNotFound: product not found

        Returns:
            Product: Product found
        """
        raise NotImplementedError