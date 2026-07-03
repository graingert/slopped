#!/usr/bin/env python

# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.


from slopped.cred import credentials
from slopped.internet import reactor
from slopped.spread import pb


def main():
    factory = pb.PBClientFactory()
    reactor.connectTCP("localhost", 8800, factory)
    def1 = factory.login(credentials.UsernamePassword("user2", "pass2"))
    def1.addCallback(connected)
    reactor.run()


def connected(perspective):
    print("got perspective2 ref:", perspective)
    print("asking it to foo(14)")
    perspective.callRemote("foo", 14)


main()
