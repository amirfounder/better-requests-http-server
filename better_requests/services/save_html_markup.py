from typing import Dict

from daos.internal import NewsArticleHtmlDocumentDao, NewsArticleHtmlDocumentIndexDao

from better_requests.services.base import BaseBetterRequestsService


class SaveNewsArticleHtmlDocument(BaseBetterRequestsService):
    def __init__(self):
        self.news_article_html_dao = NewsArticleHtmlDocumentDao()
        self.news_article_html_index_dao = NewsArticleHtmlDocumentIndexDao()

    def run(self, params: Dict):
        pass
