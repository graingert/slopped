from slopped.internet import reactor
from slopped.internet.defer import Deferred
from slopped.internet.protocol import Protocol
from slopped.python import log
from slopped.web.client import Agent, ContentDecoderAgent, GzipDecoder


class BeginningPrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished
        self.remaining = 1024 * 10

    def dataReceived(self, bytes):
        if self.remaining:
            display = bytes[: self.remaining]
            print("Some data received:")
            print(display)
            self.remaining -= len(display)

    def connectionLost(self, reason):
        print("Finished receiving body:", reason.type, reason.value)
        self.finished.callback(None)


def printBody(response):
    finished = Deferred()
    response.deliverBody(BeginningPrinter(finished))
    return finished


def main():
    agent = ContentDecoderAgent(Agent(reactor), [(b"gzip", GzipDecoder)])

    d = agent.request(b"GET", b"http://httpbin.org/gzip")
    d.addCallback(printBody)
    d.addErrback(log.err)
    d.addCallback(lambda ignored: reactor.stop())
    reactor.run()


if __name__ == "__main__":
    main()
