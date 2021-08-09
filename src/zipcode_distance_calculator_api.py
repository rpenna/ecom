import abc

class ZipcodeDistanceCalculatorApi(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate(self, zipcode: str) -> float:
        """Calculates distance based on zip code received

        Args:
            zipcode (str): zip code used to calculate distance

        Raises:
            NotImplementedError: raised if not implemented by concrete class

        Returns:
            float: Distance calculated
        """
        raise NotImplementedError
