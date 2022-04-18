from http_server import BaseHttpServer

from better_requests.server.services import SERVICES


class BetterRequestsServer(BaseHttpServer):
    def __init__(self):
        super().__init__(port=8082)
        self.register_services(SERVICES)
