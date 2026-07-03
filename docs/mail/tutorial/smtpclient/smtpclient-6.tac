from slopped.application import service

application = service.Application("SMTP Client Tutorial")

from slopped.application import internet
from slopped.internet import protocol
from slopped.mail import smtp


class SMTPClientFactory(protocol.ClientFactory):
    protocol = smtp.ESMTPClient

    def buildProtocol(self, addr):
        return self.protocol(secret=None, identity="example.com")


smtpClientFactory = SMTPClientFactory()

smtpClientService = internet.TCPClient("localhost", 25, smtpClientFactory)
smtpClientService.setServiceParent(application)
