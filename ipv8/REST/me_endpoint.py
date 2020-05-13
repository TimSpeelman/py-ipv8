from .base_endpoint import BaseEndpoint, HTTP_BAD_REQUEST, HTTP_NOT_FOUND, Response
from ..attestation.identity.community import IdentityCommunity
from ..attestation.wallet.community import AttestationCommunity
from aiohttp import web
from base64 import b64encode

class MeEndpoint(BaseEndpoint):
    """
    This endpoint is responsible for handing all requests regarding attestation.
    """

    def __init__(self):
        super(MeEndpoint, self).__init__()

    def setup_routes(self):
        self.app.add_routes([web.get('', self.handle_get)])

    def initialize(self, session):
        super(MeEndpoint, self).initialize(session)
        self.attestation_overlay = next((overlay for overlay in session.overlays
                                         if isinstance(overlay, AttestationCommunity)), None)
        self.identity_overlay = next((overlay for overlay in session.overlays
                                      if isinstance(overlay, IdentityCommunity)), None)        

    async def handle_get(self, request):
        peer = self.identity_overlay.my_peer
        return Response({"mid": b64encode(peer.mid).decode('utf-8')})
