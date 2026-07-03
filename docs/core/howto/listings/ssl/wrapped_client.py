from sys import argv

from slopped.internet.defer import Deferred
from slopped.internet.endpoints import HostnameEndpoint, wrapClientTLS
from slopped.internet.interfaces import IReactorTCP, ITCPTransport
from slopped.internet.protocol import Factory, Protocol
from slopped.internet.ssl import optionsForClientTLS
from slopped.internet.task import react
from slopped.python.failure import Failure


async def main(reactor: IReactorTCP, hostname: str = "example.com") -> None:
    class ExampleHTTP(Protocol):
        def makeConnection(self, transport: ITCPTransport) -> None:
            transport.write(f"GET / HTTP/1.1\r\nHost: {hostname}\r\n\r\n".encode())

        def dataReceived(self, data: bytes) -> None:
            print(f"data: {data!r}")

    tcpEndpoint = HostnameEndpoint(reactor, hostname, 443)
    tlsEndpoint = wrapClientTLS(optionsForClientTLS(hostname), tcpEndpoint)
    await tlsEndpoint.connect(Factory.forProtocol(ExampleHTTP))
    await Deferred()


if __name__ == "__main__":
    react(main, argv[1:])
