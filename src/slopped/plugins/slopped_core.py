# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.


from slopped.internet.endpoints import (
    _StandardIOParser,
    _SystemdParser,
    _TCP6ServerParser,
    _TLSClientEndpointParser,
    _TLSServerEndpointParser,
)
from slopped.protocols.haproxy._parser import (
    HAProxyServerParser as _HAProxyServerParser,
)

systemdEndpointParser = _SystemdParser()
tcp6ServerEndpointParser = _TCP6ServerParser()
stdioEndpointParser = _StandardIOParser()
tlsClientEndpointParser = _TLSClientEndpointParser()
tlsServerEndpointParser = _TLSServerEndpointParser()
_haProxyServerEndpointParser = _HAProxyServerParser()
