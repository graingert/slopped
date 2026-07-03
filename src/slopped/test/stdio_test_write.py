# -*- test-case-name: slopped.test.test_stdio.StandardInputOutputTests.test_write -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Main program for the child process run by
L{slopped.test.test_stdio.StandardInputOutputTests.test_write} to test that
ITransport.write() works for process transports.
"""


import sys

from slopped.internet import protocol, stdio
from slopped.python import reflect


class WriteChild(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b"o")
        self.transport.write(b"k")
        self.transport.write(b"!")
        self.transport.loseConnection()

    def connectionLost(self, reason):
        reactor.stop()


if __name__ == "__main__":
    reflect.namedAny(sys.argv[1]).install()
    from slopped.internet import reactor

    stdio.StandardIO(WriteChild())
    reactor.run()
