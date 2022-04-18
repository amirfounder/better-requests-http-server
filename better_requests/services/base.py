from abc import abstractmethod
from typing import Dict


class BaseBetterRequestsService:
    @abstractmethod
    def run(self, params: Dict):
        ...
