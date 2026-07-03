# -*- test-case-name: slopped.test.test_strcred -*-
#
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Cred plugin for anonymous logins.
"""


from zope.interface import implementer

from slopped import plugin
from slopped.cred.checkers import AllowAnonymousAccess
from slopped.cred.credentials import IAnonymous
from slopped.cred.strcred import ICheckerFactory

anonymousCheckerFactoryHelp = """
This allows anonymous authentication for servers that support it.
"""


@implementer(ICheckerFactory, plugin.IPlugin)
class AnonymousCheckerFactory:
    """
    Generates checkers that will authenticate an anonymous request.
    """

    authType = "anonymous"
    authHelp = anonymousCheckerFactoryHelp
    argStringFormat = "No argstring required."
    credentialInterfaces = (IAnonymous,)

    def generateChecker(self, argstring=""):
        return AllowAnonymousAccess()


theAnonymousCheckerFactory = AnonymousCheckerFactory()
