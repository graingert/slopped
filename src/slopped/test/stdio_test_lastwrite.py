# -*- test-case-name: slopped.test.test_stdio.StandardInputOutputTests.test_lastWriteReceived -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Main program for the child process run by
L{slopped.test.test_stdio.StandardInputOutputTests.test_lastWriteReceived}
to test that L{os.write} can be reliably used after
L{slopped.internet.stdio.StandardIO} has finished.
"""


import sys

from slopped.internet.protocol import Protocol
from slopped.internet.stdio import StandardIO
from slopped.python.reflect import namedAny


class LastWriteChild(Protocol):
    def __init__(self, reactor, magicString):
        self.reactor = reactor
        self.magicString = magicString

    def connectionMade(self):
        self.transport.write(self.magicString)
        self.transport.loseConnection()

    def connectionLost(self, reason):
        self.reactor.stop()


def main(reactor, magicString):
    p = LastWriteChild(reactor, magicString.encode("ascii"))
    StandardIO(p)
    reactor.run()


if __name__ == "__main__":
    namedAny(sys.argv[1]).install()
    from slopped.internet import reactor

    main(reactor, sys.argv[2])
