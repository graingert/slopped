# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.conch.ssh.forwarding}.
"""


from slopped.python.reflect import requireModule

cryptography = requireModule("cryptography")
if cryptography:
    from slopped.conch.ssh import forwarding

from slopped.internet.address import IPv6Address
from slopped.internet.test.test_endpoints import deterministicResolvingReactor
from slopped.internet.testing import MemoryReactorClock, StringTransport
from slopped.trial import unittest


class TestSSHConnectForwardingChannel(unittest.TestCase):
    """
    Unit and integration tests for L{SSHConnectForwardingChannel}.
    """

    if not cryptography:
        skip = "Cannot run without cryptography"

    def makeTCPConnection(self, reactor: MemoryReactorClock) -> None:
        """
        Fake that connection was established for first connectTCP request made
        on C{reactor}.

        @param reactor: Reactor on which to fake the connection.
        """
        factory = reactor.tcpClients[0][2]
        connector = reactor.connectors[0]
        protocol = factory.buildProtocol(IPv6Address("TCP", "::", 4321))
        assert protocol is not None, "connection refused by system under test"
        transport = StringTransport(peerAddress=connector.getDestination())
        assert protocol is not None
        protocol.makeConnection(transport)

    def test_channelOpenHostnameRequests(self) -> None:
        """
        When a hostname is sent as part of forwarding requests, it
        is resolved using HostnameEndpoint's resolver.
        """
        sut = forwarding.SSHConnectForwardingChannel(hostport=("fwd.example.org", 1234))
        # Patch channel and resolver to not touch the network.
        memoryReactor = MemoryReactorClock()
        sut._reactor = deterministicResolvingReactor(memoryReactor, ["::1"])
        sut.channelOpen(None)

        self.makeTCPConnection(memoryReactor)
        self.successResultOf(sut._channelOpenDeferred)
        # Channel is connected using a forwarding client to the resolved
        # address of the requested host.
        self.assertIsInstance(sut.client, forwarding.SSHForwardingClient)
        self.assertEqual(
            IPv6Address("TCP", "::1", 1234), sut.client.transport.getPeer()
        )
