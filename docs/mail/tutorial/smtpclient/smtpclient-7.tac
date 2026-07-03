import StringIO

from slopped.application import service

application = service.Application("SMTP Client Tutorial")

from slopped.application import internet
from slopped.internet import protocol
from slopped.mail import smtp


class SMTPTutorialClient(smtp.ESMTPClient):
    mailFrom = "tutorial_sender@example.com"
    mailTo = "tutorial_recipient@example.net"
    mailData = """\
Date: Fri, 6 Feb 2004 10:14:39 -0800
From: Tutorial Guy <tutorial_sender@example.com>
To: Tutorial Gal <tutorial_recipient@example.net>
Subject: Tutorate!

Hello, how are you, goodbye.
"""

    def getMailFrom(self):
        result = self.mailFrom
        self.mailFrom = None
        return result

    def getMailTo(self):
        return [self.mailTo]

    def getMailData(self):
        return StringIO.StringIO(self.mailData)

    def sentMail(self, code, resp, numOk, addresses, log):
        print("Sent", numOk, "messages")


class SMTPClientFactory(protocol.ClientFactory):
    protocol = SMTPTutorialClient

    def buildProtocol(self, addr):
        return self.protocol(secret=None, identity="example.com")


smtpClientFactory = SMTPClientFactory()

smtpClientService = internet.TCPClient("localhost", 25, smtpClientFactory)
smtpClientService.setServiceParent(application)
