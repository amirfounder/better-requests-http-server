from typing import Dict

from daos.internal import (
    NewsArticleHtmlDocumentRawRepository,
    NewsArticleHtmlDocumentRawModel,
    NewsArticleHtmlDocumentIndexRepository,
    NewsArticleHtmlDocumentIndexModel
)

from better_requests.services.base import BaseBetterRequestsService


class SaveNewsArticle(BaseBetterRequestsService):
    def __init__(
            self,
            document_repository: NewsArticleHtmlDocumentRawRepository,
            index_repository: NewsArticleHtmlDocumentIndexRepository
    ):
        self.document_repository = document_repository
        self.index_repository = index_repository

    def run(self, params: Dict):
        document = NewsArticleHtmlDocumentRawModel()
        document.contents = params.get('markup')

        self.document_repository.save(document)

        index_item = NewsArticleHtmlDocumentIndexModel()

        index_item.document_id = document.get_id()
        index_item.document_format = self.document_repository.file_format.value
        index_item.raw_version_document_path = str(document.get_path())
        index_item.is_raw_version_stored = True
        index_item.url = params.get('url')
        index_item.retrieved_from_web_at = params.get('timestamp')

        self.index_repository.save(index_item)

        return {
            'status': 'SUCCESS'
        }
