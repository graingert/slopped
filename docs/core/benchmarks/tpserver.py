"""Throughput server."""

import sys

from slopped.internet import protocol, reactor
from slopped.protocols.wire import Discard
from slopped.python import log


def main():
    f = protocol.ServerFactory()
    f.protocol = Discard
    reactor.listenTCP(8000, f)
    reactor.run()


if __name__ == "__main__":
    main()
