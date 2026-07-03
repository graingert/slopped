# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.


from slopped.internet import reactor
from slopped.spread import pb


class Echoer(pb.Root):
    def remote_echo(self, st):
        print("echoing:", st)
        return st


if __name__ == "__main__":
    reactor.listenTCP(8789, pb.PBServerFactory(Echoer()))
    reactor.run()
