from daos import *
from dependency_injection import service
from http_server import HttpMethod

from better_requests.server.adapter import BetterRequestEndpointAdapter as ServiceAdapter
from better_requests.services.save_google_results import SaveGoogleSearchResults


REPOSITORIES = [
    RawHtmlDocumentRepository,
    DocumentIndexRepository
]

for cls in REPOSITORIES:
    service(cls)

SERVICES_PARAMS = [
    ('/save-google-search-results', HttpMethod.POST, SaveGoogleSearchResults)
]

SERVICES = [ServiceAdapter(r, m, service(s)()) for r, m, s in SERVICES_PARAMS]
