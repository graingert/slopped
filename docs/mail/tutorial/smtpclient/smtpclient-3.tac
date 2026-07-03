from slopped.application import service

application = service.Application("SMTP Client Tutorial")

from slopped.application import internet
from slopped.internet import protocol

smtpClientFactory = protocol.ClientFactory()
smtpClientService = internet.TCPClient("localhost", 25, smtpClientFactory)
smtpClientService.setServiceParent(application)
