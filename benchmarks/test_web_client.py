# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Benchmarks for C{HTTP11ClientProtocol}.
"""

from slopped.internet.testing import StringTransport
from slopped.web._newclient import HTTP11ClientProtocol, Request
from slopped.web.http_headers import Headers

RESPONSE = """HTTP/1.1 200 OK
Host: blah
Foo: bar
Gaz: baz
Content-length: 3

abc""".replace(
    "\n", "\r\n"
).encode(
    "utf-8"
)


def test_http_client_small_response(benchmark):
    """Measure the time to run a simple HTTP 1.1 client request."""

    def go():
        protocol = HTTP11ClientProtocol()
        protocol.makeConnection(StringTransport())
        request = Request(
            b"GET", b"/foo/bar", Headers({b"Host": [b"example.com"]}), None
        )
        response = protocol.request(request)
        protocol.dataReceived(RESPONSE)
        result = []
        response.addCallback(result.append)
        assert result

    benchmark(go)
