from http_server import BaseHttpServer


class BetterRequestsServer(BaseHttpServer):
    def __init__(self):
        super().__init__(port=8082)
