from flask import make_response, Response, request
from flask.views import MethodView
from .http import Http
from ..factory.memory_repository_factory import MemoryRepositoryFactory

class OrderView(MethodView):
    def __init__(self):
        memory_repository_factory = MemoryRepositoryFactory()
        self.__http = Http(memory_repository_factory)

    def get(self, code) -> Response:
        response = self.__http.get_order(code)
        return make_response(response[0], response[1])

    def post(self) -> Response:
        body = request.get_json()
        response = self.__http.place_order(body)
        return make_response(
            response[0],
            response[1]
        )
