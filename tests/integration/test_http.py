import pytest
import requests
from datetime import datetime
from ...src.infra.factory.memory_repository_factory import MemoryRepositoryFactory
from ...src.infra.gateway.memory.zipcode_distance_calculator_api_memory import ZipcodeDistanceCalculatorApiMemory
from ...src.application.place_order import PlaceOrder
from ...src.application.place_order_input import PlaceOrderInput

@pytest.fixture
def order_input():
    return {
        'products': [
            {
                'id': '1',
                'quantity': 5
            },
            {
                'id': '2',
                'quantity': 30
            },
            {
                'id': '3',
                'quantity': 1
            }
        ],
        'cpf': '01234567890',
        'zipcode': '1234567',
        'coupon': '15OFF'
    }

@pytest.mark.skip(reason="no reason for testing HTTP requests everytime")
def test_should_not_find_inexistent_order():
    get_order_url = 'http://localhost:3000/order/123456'
    get_order_response = requests.get(get_order_url)
    assert get_order_response.status_code == 422

@pytest.mark.skip(reason="no reason for testing HTTP requests everytime")
def test_should_set_order_via_http(order_input):
    place_order_response = requests.post(
        'http://localhost:3000/order',
        json=order_input
    )
    assert place_order_response.status_code == 201

@pytest.mark.skip(reason="no reason for testing HTTP requests everytime")
def test_should_get_order_via_http(order_input):
    place_order_response = requests.post(
        'http://localhost:3000/order',
        json=order_input
    )
    order_data = place_order_response.json()
    get_order_url = 'http://localhost:3000/order/%s' % order_data['code']
    get_order_response = requests.get(get_order_url)
    assert get_order_response.status_code == 200

@pytest.mark.skip(reason="no reason for testing HTTP requests everytime")
def test_should_get_correct_order_code_via_http(order_input):
    place_order_response = requests.post(
        'http://localhost:3000/order',
        json=order_input
    )
    order_data = place_order_response.json()
    get_order_url = 'http://localhost:3000/order/%s' % order_data['code']
    get_order_response = requests.get(get_order_url)
    json_get_order_response = get_order_response.json()
    assert order_data['code'] == json_get_order_response['code']
