import pytest
from ..src.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory

def test_should_calculate_distance_by_zipcode():
    zipcode_calculator = ZipcodeDistanceCalculatorApiMemory()
    distance = zipcode_calculator.calculate('1234567')
    assert distance == 1000
