from ....domain.entity.product import Product
from ....domain.repository.product_repository import ProductRepository
from ....domain.exception.product_not_found import ProductNotFound

INFO_BOOK = {
    'height': 15,
    'width': 10,
    'depth': 2,
    'weight': 1000
}
INFO_PFF2_MASK = {
    'height': 10,
    'width': 10,
    'depth': 0.01,
    'weight': 50
}
INFO_VACUUM_CLEANER = {
    'height': 40,
    'width': 30,
    'depth': 30,
    'weight': 5000
}

class ProductRepositoryMemory(ProductRepository):
    def __init__(self):
        self.__products = [
            Product('1', 'book', 19.9, INFO_BOOK),
            Product('2', 'pff2 mask', 2.8, INFO_PFF2_MASK),
            Product('3', 'vacuum cleaner', 227.99, INFO_VACUUM_CLEANER)
        ]
    
    def get_by_id(self, id: str) -> Product:
        """Search product by ID

        Args:
            id (str): Id to be searched

        Raises:
            ProductNotFound: product not found

        Returns:
            Product: Product found
        """
        for product in self.__products:
            if product.id == id:
                return product
        raise ProductNotFound
