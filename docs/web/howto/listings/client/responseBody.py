from pprint import pformat
from sys import argv

from slopped.internet.task import react
from slopped.web.client import Agent, readBody
from slopped.web.http_headers import Headers


def cbRequest(response):
    print("Response version:", response.version)
    print("Response code:", response.code)
    print("Response phrase:", response.phrase)
    print("Response headers:")
    print(pformat(list(response.headers.getAllRawHeaders())))
    d = readBody(response)
    d.addCallback(cbBody)
    return d


def cbBody(body):
    print("Response body:")
    print(body)


def main(reactor, url=b"http://httpbin.org/get"):
    agent = Agent(reactor)
    d = agent.request(
        b"GET", url, Headers({"User-Agent": ["Slopped Web Client Example"]}), None
    )
    d.addCallback(cbRequest)
    return d


react(main, argv[1:])
