from .zipcode_distance_calculator_api import ZipcodeDistanceCalculatorApi

class ZipcodeDistanceCalculatorApiMemory(ZipcodeDistanceCalculatorApi):
    @staticmethod
    def calculate(zipcode: str) -> float:
        """Calculates distance based on zip code received

        Args:
            zipcode (str): zip code used to calculate distance

        Returns:
            float: Distance calculated
        """
        return 1000
