from typing import Dict

from daos.internal import (
    NewsArticleHtmlDocumentRepository,
    NewsArticleHtmlDocumentModel,
    NewsArticleHtmlDocumentIndexRepository,
    NewsArticleHtmlDocumentIndexModel
)

from better_requests.services.base import BaseBetterRequestsService


class SaveNewsArticleHtmlDocument(BaseBetterRequestsService):
    def __init__(self):
        self.document_repository = NewsArticleHtmlDocumentRepository()
        self.index_repository = NewsArticleHtmlDocumentIndexRepository()

    def run(self, params: Dict):
        document = NewsArticleHtmlDocumentModel()
        document.contents = params.get('markup')

        if not document.contents:
            raise Exception('request body must have markup key.')

        self.document_repository.save(document)

        index_item = NewsArticleHtmlDocumentIndexModel()
        index_item.document_id = document.get_id()
        index_item.retrieved_from_web_at = params.get('timestamp')
        index_item.document_format = self.document_repository.file_format.value
        index_item.source_url = params.get('url')
        index_item.document_path = str(document.get_path())

        self.index_repository.save(index_item)

        return {
            'status': 'SUCCESS'
        }
