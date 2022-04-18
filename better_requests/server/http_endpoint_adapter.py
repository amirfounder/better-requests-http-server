from typing import Dict

from http_server import BaseHttpEndpointAdapter

from better_requests.services.base import BaseBetterRequestsService


class BetterRequestEndpointAdapter(BaseHttpEndpointAdapter[BaseBetterRequestsService]):
    def run(self, params: Dict):
        self.service.run(params)
