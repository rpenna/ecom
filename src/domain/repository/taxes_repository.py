from abc import ABC, abstractmethod
class TaxesRepository(ABC):
    @abstractmethod
    def get_by_id_and_type(self, id: str, type: str) -> float:
        """Search product's tax by ID and its type of tax

        Args:
            id (str): product's id
            type (str): type of tax

        Returns:
            float: Product ' tax'
        """
        raise NotImplementedError