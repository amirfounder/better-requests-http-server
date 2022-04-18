from http_server import BaseHttpServer

from better_requests.server.http_endpoints import HTTP_ENDPOINTS


class BetterRequestsServer(BaseHttpServer):
    def __init__(self):
        super().__init__(port=8082)
        self.register_endpoint_adapters(HTTP_ENDPOINTS)

