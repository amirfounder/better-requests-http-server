from typing import Dict

from http_server import BaseHttpEndpointServiceAdapter

from better_requests.services.base import BaseBetterRequestsService


class BetterRequestEndpointAdapter(BaseHttpEndpointServiceAdapter[BaseBetterRequestsService]):
    def run(self, params: Dict):
        self.service.run(params)
