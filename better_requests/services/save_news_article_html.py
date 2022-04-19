from typing import Dict

from daos.internal import (
    NewsArticleHtmlDocumentDao,
    NewsArticleHtmlDocumentModel,
    NewsArticleHtmlDocumentIndexDao,
    NewsArticleHtmlDocumentIndexModel
)

from better_requests.services.base import BaseBetterRequestsService


class SaveNewsArticleHtmlDocument(BaseBetterRequestsService):
    def __init__(self):
        self.html_dao = NewsArticleHtmlDocumentDao()
        self.index_dao = NewsArticleHtmlDocumentIndexDao()

    def run(self, params: Dict):
        document = NewsArticleHtmlDocumentModel()
        document.contents = params.get('markup')

        if not document.contents:
            raise Exception('request body must have markup key.')

        self.html_dao.save(document)

        index_item = NewsArticleHtmlDocumentIndexModel()
        index_item.document_id = document.get_id()
        index_item.retrieved_from_web_at = params.get('timestamp')

        self.index_dao.save(index_item)

        return {
            'status': 'SUCCESS'
        }
