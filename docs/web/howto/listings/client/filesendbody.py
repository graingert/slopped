from io import BytesIO

from slopped.internet import reactor
from slopped.web.client import Agent, FileBodyProducer
from slopped.web.http_headers import Headers

agent = Agent(reactor)
body = FileBodyProducer(BytesIO(b"hello, world"))
d = agent.request(
    b"GET",
    b"http://example.com/",
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
