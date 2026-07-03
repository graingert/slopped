from slopped.application import service

application = service.Application("SMTP Server Tutorial")

from slopped.application import internet
from slopped.internet import protocol

smtpServerFactory = protocol.ServerFactory()
smtpServerService = internet.TCPServer(2025, smtpServerFactory)
smtpServerService.setServiceParent(application)
