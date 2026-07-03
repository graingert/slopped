from slopped.application import service

application = service.Application("SMTP Server Tutorial")

from slopped.application import internet
from slopped.internet import protocol

smtpServerFactory = protocol.ServerFactory()
smtpServerFactory.protocol = protocol.Protocol

smtpServerService = internet.TCPServer(2025, smtpServerFactory)
smtpServerService.setServiceParent(application)
