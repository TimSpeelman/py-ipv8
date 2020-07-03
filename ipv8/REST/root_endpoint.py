from .attestation_endpoint import AttestationEndpoint
from .base_endpoint import BaseEndpoint
from .dht_endpoint import DHTEndpoint
from .isolation_endpoint import IsolationEndpoint
from .network_endpoint import NetworkEndpoint
from .noblock_dht_endpoint import NoBlockDHTEndpoint
from .overlays_endpoint import OverlaysEndpoint
from .trustchain_endpoint import TrustchainEndpoint
from .tunnel_endpoint import TunnelEndpoint
from .me_endpoint import MeEndpoint


class RootEndpoint(BaseEndpoint):
    extra_endpoints = {}
    """
    The root endpoint of the HTTP API is the root resource in the request tree.
    It will dispatch requests regarding torrents, channels, settings etc to the right child endpoint.
    """
    def __init__(self, middlewares=(), endpoints={}):
        self.extra_endpoints = endpoints # must precede super, because parent init calls setup_routes
        super(RootEndpoint, self).__init__(middlewares)

    def setup_routes(self):
        endpoints = {'/attestation': AttestationEndpoint(),
                     '/dht': DHTEndpoint(),
                     '/me': MeEndpoint(),
                     '/isolation': IsolationEndpoint(),
                     '/network': NetworkEndpoint(),
                     '/noblockdht': NoBlockDHTEndpoint(),
                     '/overlays': OverlaysEndpoint(),
                     '/trustchain': TrustchainEndpoint(),
                     '/tunnel': TunnelEndpoint(),
                     **self.extra_endpoints}
        for path, ep_cls in endpoints.items():
            self.add_endpoint(path, ep_cls)
