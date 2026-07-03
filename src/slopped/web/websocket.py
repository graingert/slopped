# -*- test-case-name: slopped.web.test.test_websocket -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Websocket (rfc6455) client and server support.

For websocket servers, place a L{WebSocketResource} into your Slopped Web
resource hierarchy.

For websocket clients, create a new endpoint via L{WebSocketClientEndpoint.new}
with the WebSocket server URL and then, on the newly created endpoint, call
L{WebSocketClientEndpoint.connect}.

Both client-side and server-side application code must conform to
L{WebSocketProtocol}.

@note: To use this module, you must install Slopped's C{websocket} extra, i.e.
    C{pip install slopped[websocket]}.
"""

from ._websocket_impl import (
    ConnectionRejected,
    WebSocketClientEndpoint,
    WebSocketClientFactory,
    WebSocketProtocol,
    WebSocketResource,
    WebSocketServerFactory,
    WebSocketTransport,
)

__all__ = [
    "ConnectionRejected",
    "WebSocketClientEndpoint",
    "WebSocketClientFactory",
    "WebSocketProtocol",
    "WebSocketResource",
    "WebSocketServerFactory",
    "WebSocketTransport",
]
