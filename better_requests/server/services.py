from daos.internal import NewsArticleHtmlDocumentRawRepository, NewsArticleHtmlDocumentIndexRepository
from dependency_injection import service
from http_server import HttpMethod

from better_requests.server.adapter import BetterRequestEndpointAdapter
from better_requests.services.save_news_article_html import SaveNewsArticleHtmlDocument


# Registering repositories as services in IOC container
REPOSITORIES = [
    service(NewsArticleHtmlDocumentRawRepository),
    service(NewsArticleHtmlDocumentIndexRepository)
]

# The actual services used by the HTTP server
SERVICES = [
    BetterRequestEndpointAdapter('/news-article', HttpMethod.POST, service(SaveNewsArticleHtmlDocument)()),
]
