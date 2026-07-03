if __name__ == "__main__":
    import basic_client

    raise SystemExit(basic_client.main())

from sys import stdout

from slopped.internet import reactor
from slopped.internet.endpoints import TCP4ClientEndpoint
from slopped.internet.protocol import Factory
from slopped.protocols.amp import AMP
from slopped.python.log import err, startLogging


def connect():
    endpoint = TCP4ClientEndpoint(reactor, "127.0.0.1", 8750)
    return endpoint.connect(Factory.forProtocol(AMP))


def main():
    startLogging(stdout)

    d = connect()
    d.addErrback(err, "Connection failed")

    def done(ignored):
        reactor.stop()

    d.addCallback(done)

    reactor.run()
