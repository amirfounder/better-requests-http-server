from http_server import HttpMethod

from better_requests.server.adapter import BetterRequestEndpointAdapter
from better_requests.services.save_news_article_html import SaveNewsArticleHtmlDocument

SERVICES = [
    BetterRequestEndpointAdapter('/news-article', HttpMethod.POST, SaveNewsArticleHtmlDocument()),
]
