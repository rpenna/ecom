from abc import ABC, abstractmethod


class TaxesRepository(ABC):
    @abstractmethod
    def get_by_id_and_type(self, id: str, type: str) -> int:
        """Search product's tax by ID and its type of tax

        Args:
            id (str): product's id
            type (str): type of tax

        Returns:
            int: Product ' tax'
        """
        raise NotImplementedError
