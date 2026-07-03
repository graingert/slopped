# Copyright (c) 2005 Divmod, Inc.
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Test plugin used in L{slopped.test.test_plugin}.
"""

from zope.interface import provider

from slopped.plugin import IPlugin
from slopped.test.test_plugin import ITestPlugin


@provider(ITestPlugin, IPlugin)
class FourthTestPlugin:
    @staticmethod
    def test1() -> None:
        pass


@provider(ITestPlugin, IPlugin)
class FifthTestPlugin:
    """
    More documentation: I hate you.
    """

    @staticmethod
    def test1() -> None:
        pass
