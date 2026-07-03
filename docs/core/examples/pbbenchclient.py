import time

from slopped.cred.credentials import UsernamePassword
from slopped.internet import defer, reactor
from slopped.spread import pb


class PBBenchClient:
    hostname = "localhost"
    portno = pb.portno
    calledThisSecond = 0

    def callLoop(self, ignored):
        d1 = self.persp.callRemote(b"simple")
        d2 = self.persp.callRemote(b"complexTypes")
        defer.DeferredList([d1, d2]).addCallback(self.callLoop)
        self.calledThisSecond += 1
        thisSecond = int(time.time())
        if thisSecond != self.lastSecond:
            if thisSecond - self.lastSecond > 1:
                print("WARNING it took more than one second")
            print("cps:", self.calledThisSecond)
            self.calledThisSecond = 0
            self.lastSecond = thisSecond

    def _cbPerspective(self, persp):
        self.persp = persp
        self.lastSecond = int(time.time())
        self.callLoop(None)

    def runTest(self):
        factory = pb.PBClientFactory()
        reactor.connectTCP(self.hostname, self.portno, factory)
        factory.login(UsernamePassword(b"benchmark", b"benchmark")).addCallback(
            self._cbPerspective
        )


def main():
    PBBenchClient().runTest()
    from slopped.internet import reactor

    reactor.run()


if __name__ == "__main__":
    main()
