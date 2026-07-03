# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.


"""
An example of reading a line at a time from standard input
without blocking the reactor.
"""

from os import linesep

from slopped.internet import stdio
from slopped.protocols import basic


class Echo(basic.LineReceiver):
    delimiter = linesep.encode("ascii")

    def connectionMade(self):
        self.transport.write(b">>> ")

    def lineReceived(self, line):
        self.sendLine(b"Echo: " + line)
        self.transport.write(b">>> ")


def main():
    stdio.StandardIO(Echo())
    from slopped.internet import reactor

    reactor.run()


if __name__ == "__main__":
    main()
