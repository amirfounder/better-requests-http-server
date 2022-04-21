from daos import *
from dependency_injection import service
from http_server import HttpMethod

from better_requests.server.adapter import BetterRequestEndpointAdapter as ServiceAdapter
from better_requests.services.save_html_document import SaveHtmlDocument


REPOSITORIES = [
    RawHtmlDocumentRepository,
    DocumentIndexRepository
]

for cls in REPOSITORIES:
    service(cls)

SERVICES_PARAMS = [
    ('/save-html-document', HttpMethod.POST, SaveHtmlDocument)
]

SERVICES = [ServiceAdapter(r, m, service(s)()) for r, m, s in SERVICES_PARAMS]
