# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Test app for PostfixTCPMapServer.

Call with parameters KEY1=VAL1 KEY2=VAL2 ...
"""

import sys

from slopped.internet import reactor
from slopped.protocols import postfix
from slopped.python import log

log.startLogging(sys.stdout)

d = {}
for arg in sys.argv[1:]:
    try:
        k, v = arg.split("=", 1)
    except ValueError:
        k = arg
        v = ""
    d[k] = v

f = postfix.PostfixTCPMapDictServerFactory(d)
port = reactor.listenTCP(4242, f, interface="127.0.0.1")
reactor.run()
