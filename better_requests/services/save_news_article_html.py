from typing import Dict

from daos.internal import (
    NewsArticleHtmlDocumentDao,
    NewsArticleHtmlDocumentIndexDao,
    NewsArticleHtmlDocumentModel,
    NewsArticleHtmlDocumentIndexModel
)

from better_requests.services.base import BaseBetterRequestsService


class SaveNewsArticleHtmlDocument(BaseBetterRequestsService):
    def __init__(self):
        self.news_article_html_dao = NewsArticleHtmlDocumentDao()
        self.news_article_html_index_dao = NewsArticleHtmlDocumentIndexDao()

    def run(self, params: Dict):
        markup = params.get('markup')
        timestamp = params.get('timestamp')

        document = NewsArticleHtmlDocumentModel(markup)

        self.news_article_html_dao.save(document)

        index = NewsArticleHtmlDocumentIndexModel(
            document_id=document.id,
            retrieved_at=timestamp
        )

        self.news_article_html_index_dao.save(index)

