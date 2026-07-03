from slopped.internet import reactor
from slopped.internet.protocol import DatagramProtocol


class Echo(DatagramProtocol):
    def datagramReceived(self, data, addr):
        print(f"received {data!r} from {addr}")
        self.transport.write(data, addr)


reactor.listenUDP(9999, Echo(), interface="::")
reactor.run()
