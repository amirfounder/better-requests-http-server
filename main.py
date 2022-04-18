from better_requests import SERVICES
from better_requests import BetterRequestsServer

if __name__ == '__main__':
    server = BetterRequestsServer()
    server.register_services(SERVICES)
    server.run()
