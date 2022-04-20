from daos import GoogleSearchResultsHtmlDocumentRawRepository, GoogleSearchResultsHtmlDocumentIndexRepository
from daos.internal import NewsArticleHtmlDocumentRawRepository, NewsArticleHtmlDocumentIndexRepository
from dependency_injection import service
from http_server import HttpMethod

from better_requests.server.adapter import BetterRequestEndpointAdapter as ServiceAdapter
from better_requests.services.save_google_results import SaveGoogleSearchResults
from better_requests.services.save_news_article import SaveNewsArticle


REPOSITORIES = [
    NewsArticleHtmlDocumentRawRepository,
    NewsArticleHtmlDocumentIndexRepository,
    GoogleSearchResultsHtmlDocumentRawRepository,
    GoogleSearchResultsHtmlDocumentIndexRepository
]

for cls in REPOSITORIES:
    service(cls)

SERVICES_PARAMS = [
    ('/save-news-article', HttpMethod.POST, SaveNewsArticle),
    ('/save-google-search-results', HttpMethod.POST, SaveGoogleSearchResults)
]

SERVICES = [ServiceAdapter(r, m, service(s)()) for r, m, s in SERVICES_PARAMS]
