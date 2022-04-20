from daos import GoogleSearchResultsHtmlDocumentRawRepository, GoogleSearchResultsHtmlDocumentIndexRepository
from daos.internal import NewsArticleHtmlDocumentRawRepository, NewsArticleHtmlDocumentIndexRepository
from dependency_injection import service as ioc_service
from http_server import HttpMethod

from better_requests.server.adapter import BetterRequestEndpointAdapter
from better_requests.services.save_google_results import SaveGoogleSearchResults
from better_requests.services.save_news_article import SaveNewsArticle


REPOSITORIES = [
    NewsArticleHtmlDocumentRawRepository,
    NewsArticleHtmlDocumentIndexRepository,
    GoogleSearchResultsHtmlDocumentRawRepository,
    GoogleSearchResultsHtmlDocumentIndexRepository
]

for cls in REPOSITORIES:
    ioc_service(cls)

SERVICE_PARAMS = [
    ('/save-news-article', HttpMethod.POST, SaveNewsArticle),
    ('/save-google-search-results', HttpMethod.POST, SaveGoogleSearchResults)
]

SERVICES = [BetterRequestEndpointAdapter(r, m, ioc_service(s)()) for r, m, s in SERVICE_PARAMS]
