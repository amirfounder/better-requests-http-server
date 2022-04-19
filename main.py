from better_requests import SERVICES, BetterRequestsServer

if __name__ == '__main__':
    server = BetterRequestsServer()
    server.register_services(SERVICES)
    server.run()
