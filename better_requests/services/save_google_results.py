from typing import Dict

from daos.internal import (
    RawHtmlDocumentRepository,
    DocumentIndexRepository,
)

from better_requests.services.base import BaseBetterRequestsService as Base


class SaveGoogleSearchResults(Base):
    def __init__(
            self,
            html_repository: RawHtmlDocumentRepository,
            index_repository: DocumentIndexRepository
    ):
        self.html_repository = html_repository
        self.index_repository = index_repository

    def run(self, params: Dict):
        document = self.html_repository.create()
        document.contents = params.get('markup')

        self.html_repository.update(document)

        index_item = self.index_repository.create()
        index_item.document_id = document.id
        index_item.document_format = self.html_repository.filetype
        index_item.raw_version_document_path = str(document.path)
        index_item.is_raw_version_stored = True
        index_item.url = params.get('url')
        index_item.retrieved_from_web_at = params.get('timestamp')

        self.index_repository.update(index_item)

        return {
            'status': 'SUCCESS'
        }
