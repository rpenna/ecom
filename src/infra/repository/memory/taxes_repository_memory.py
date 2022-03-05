from ....domain.repository.taxes_repository import TaxesRepository

BOOK_DEFAULT_MONTH_TAX = {"id": "1", "type": "default", "value": 1 / 100}
BOOK_NOVEMBER_TAX = {"id": "1", "type": "november", "value": 0.1 / 100}
PFF2_MASK_DEFAULT_MONTH_TAX = {"id": "2", "type": "default", "value": 0.1 / 100}
PFF2_MASK_NOVEMBER_TAX = {"id": "2", "type": "november", "value": 0}
VACUUM_CLEANER_DEFAULT_MONTH_TAX = {"id": "3", "type": "default", "value": 10 / 100}
VACUUM_CLEANER_NOVEMBER_TAX = {"id": "3", "type": "november", "value": 1 / 100}


class TaxesRepositoryMemory(TaxesRepository):
    def __init__(self):
        self.__table = [
            BOOK_DEFAULT_MONTH_TAX,
            BOOK_NOVEMBER_TAX,
            PFF2_MASK_DEFAULT_MONTH_TAX,
            PFF2_MASK_NOVEMBER_TAX,
            VACUUM_CLEANER_DEFAULT_MONTH_TAX,
            VACUUM_CLEANER_NOVEMBER_TAX,
        ]

    def get_by_id_and_type(self, id: str, type: str) -> float:
        """Search product's tax by ID and its type of tax

        Args:
            id (str): product's id
            type (str): type of tax

        Returns:
            int: Product ' tax'
        """
        for tax in self.__table:
            if tax["id"] == id and tax["type"] == type:
                return tax["value"]
        return 0
