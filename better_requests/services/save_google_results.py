from typing import Dict

from daos.internal import (
    GoogleSearchResultsHtmlDocumentRawRepository,
    GoogleSearchResultsHtmlDocumentRawModel,
    GoogleSearchResultsHtmlDocumentIndexRepository,
    GoogleSearchResultsHtmlDocumentIndexModel
)

from better_requests.services.base import BaseBetterRequestsService as Base


class SaveGoogleSearchResults(Base):
    def __init__(
            self,
            document_repository: GoogleSearchResultsHtmlDocumentRawRepository,
            index_repository: GoogleSearchResultsHtmlDocumentIndexRepository
    ):
        self.document_repository = document_repository
        self.index_repository = index_repository

    def run(self, params: Dict):
        document = GoogleSearchResultsHtmlDocumentRawModel()
        document.contents = params.get('markup')

        self.document_repository.save(document)

        index_item = GoogleSearchResultsHtmlDocumentIndexModel()

        index_item.document_id = document.id
        index_item.document_format = self.document_repository.filetype
        index_item.raw_version_document_path = str(document.path)
        index_item.is_raw_version_stored = True
        index_item.url = params.get('url')
        index_item.retrieved_from_web_at = params.get('timestamp')

        self.index_repository.save(index_item)

        return {
            'status': 'SUCCESS'
        }
