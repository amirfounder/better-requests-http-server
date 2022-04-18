from http_server import HttpMethods

from better_requests.server.http_endpoint_adapter import BetterRequestEndpointAdapter
from better_requests.services.save_news_article_html import SaveNewsArticleHtmlDocument

HTTP_ENDPOINTS = [
    BetterRequestEndpointAdapter('/', HttpMethods.POST, SaveNewsArticleHtmlDocument())
]
