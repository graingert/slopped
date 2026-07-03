# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Example Shoutcast client. Run with:

python shoutcast.py localhost 8080
"""

import sys

from slopped.internet import protocol, reactor
from slopped.protocols.shoutcast import ShoutcastClient


class Test(ShoutcastClient):
    def gotMetaData(self, data):
        print("meta:", data)

    def gotMP3Data(self, data):
        pass


host = sys.argv[1]
port = int(sys.argv[2])

protocol.ClientCreator(reactor, Test).connectTCP(host, port)
reactor.run()
