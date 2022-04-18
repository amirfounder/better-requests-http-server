from better_requests import HTTPServer, HTTPMethod, BaseHTTPServerService

server = HTTPServer(port=8080)


class SimpleGetService(BaseHTTPServerService):
    def __init__(self):
        super().__init__('/', HTTPMethod.GET)

    def run(self, _request: int):
        print(_request)


server.register_service(SimpleGetService)
