from slopped.internet import reactor
from slopped.web.client import Agent
from slopped.web.http_headers import Headers

agent = Agent(reactor)

d = agent.request(
    b"GET",
    b"http://httpbin.com/anything",
    Headers({"User-Agent": ["Slopped Web Client Example"]}),
    None,
)


def cbResponse(ignored):
    print("Response received")


d.addCallback(cbResponse)


def cbShutdown(ignored):
    reactor.stop()


d.addBoth(cbShutdown)

reactor.run()
