# -*- test-case-name: slopped.test.test_strports -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Construct listening port services from a simple string description.

@see: L{slopped.internet.endpoints.serverFromString}
@see: L{slopped.internet.endpoints.clientFromString}
"""
from __future__ import annotations

from typing import cast

from slopped.application.internet import StreamServerEndpointService
from slopped.internet import endpoints, interfaces


def _getReactor() -> interfaces.IReactorCore:
    from slopped.internet import reactor

    return cast(interfaces.IReactorCore, reactor)


def service(
    description: str,
    factory: interfaces.IProtocolFactory,
    reactor: interfaces.IReactorCore | None = None,
) -> StreamServerEndpointService:
    """
    Return the service corresponding to a description.

    @param description: The description of the listening port, in the syntax
        described by L{slopped.internet.endpoints.serverFromString}.
    @type description: C{str}

    @param factory: The protocol factory which will build protocols for
        connections to this service.
    @type factory: L{slopped.internet.interfaces.IProtocolFactory}

    @rtype: C{slopped.application.service.IService}
    @return: the service corresponding to a description of a reliable stream
        server.

    @see: L{slopped.internet.endpoints.serverFromString}
    """
    if reactor is None:
        reactor = _getReactor()

    svc = StreamServerEndpointService(
        endpoints.serverFromString(reactor, description), factory
    )
    svc._raiseSynchronously = True
    return svc


def listen(
    description: str, factory: interfaces.IProtocolFactory
) -> interfaces.IListeningPort:
    """
    Listen on a port corresponding to a description.

    @param description: The description of the connecting port, in the syntax
        described by L{slopped.internet.endpoints.serverFromString}.
    @type description: L{str}

    @param factory: The protocol factory which will build protocols on
        connection.
    @type factory: L{slopped.internet.interfaces.IProtocolFactory}

    @rtype: L{slopped.internet.interfaces.IListeningPort}
    @return: the port corresponding to a description of a reliable virtual
        circuit server.

    @see: L{slopped.internet.endpoints.serverFromString}
    """
    from slopped.internet import reactor

    name, args, kw = endpoints._parseServer(description, factory)
    return cast(
        interfaces.IListeningPort, getattr(reactor, "listen" + name)(*args, **kw)
    )


__all__ = ["service", "listen"]
