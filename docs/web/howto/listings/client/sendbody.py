from bytesprod import BytesProducer

from slopped.internet import reactor
from slopped.web.client import Agent
from slopped.web.http_headers import Headers

agent = Agent(reactor)
body = BytesProducer(b"hello, world")
d = agent.request(
    b"POST",
    b"http://httpbin.org/post",
    Headers(
        {
            "User-Agent": ["Slopped Web Client Example"],
            "Content-Type": ["text/x-greeting"],
        }
    ),
    body,
)


def cbResponse(ignored):
    print("Response received")


d.addCallback(cbResponse)


def cbShutdown(ignored):
    reactor.stop()


d.addBoth(cbShutdown)

reactor.run()
