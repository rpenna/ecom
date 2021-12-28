from .place_order_input import PlaceOrderInput
from .place_order_output import PlaceOrderOutput
from ...domain.service.order_creator import OrderCreator
from ...domain.factory.repository_abstract_factory import RepositoryAbstractFactory
from ...domain.gateway.zipcode_distance_calculator_api import ZipcodeDistanceCalculatorApi

class PlaceOrder:
    def __init__(self, repository_factory: RepositoryAbstractFactory, zipcode_calculator: ZipcodeDistanceCalculatorApi):
        self.__zipcode_calculator = zipcode_calculator
        self.__repository_factory = repository_factory

    def execute(self, input: PlaceOrderInput) -> PlaceOrderOutput:
        """Place order according to the DTO received, saving the order created
        to the database.

        Args:
            input (PlaceOrderInput): DTO of the order

        Returns:
            PlaceOrderOutput: Created order output
        """
        order_data = input.dict()
        order_service = OrderCreator(
            self.__repository_factory,
            self.__zipcode_calculator
        )
        order = order_service.create(order_data)
        return PlaceOrderOutput(order)
