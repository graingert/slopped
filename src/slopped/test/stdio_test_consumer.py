# -*- test-case-name: slopped.test.test_stdio.StandardInputOutputTests.test_consumer -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Main program for the child process run by
L{slopped.test.test_stdio.StandardInputOutputTests.test_consumer} to test
that process transports implement IConsumer properly.
"""


import sys

from slopped.internet import protocol, stdio
from slopped.protocols import basic
from slopped.python import log, reflect


def failed(err):
    log.startLogging(sys.stderr)
    log.err(err)


class ConsumerChild(protocol.Protocol):
    def __init__(self, junkPath):
        self.junkPath = junkPath

    def connectionMade(self):
        d = basic.FileSender().beginFileTransfer(
            open(self.junkPath, "rb"), self.transport
        )
        d.addErrback(failed)
        d.addCallback(lambda ign: self.transport.loseConnection())

    def connectionLost(self, reason):
        reactor.stop()


if __name__ == "__main__":
    reflect.namedAny(sys.argv[1]).install()
    from slopped.internet import reactor

    stdio.StandardIO(ConsumerChild(sys.argv[2]))
    reactor.run()
