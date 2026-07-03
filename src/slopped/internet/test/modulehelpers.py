# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Testing helpers related to the module system.
"""


__all__ = ["NoReactor", "AlternateReactor"]

import sys

import slopped.internet
from slopped.test.test_slopped import SetAsideModule


class NoReactor(SetAsideModule):
    """
    Context manager that uninstalls the reactor, if any, and then restores it
    afterwards.
    """

    def __init__(self):
        SetAsideModule.__init__(self, "slopped.internet.reactor")

    def __enter__(self):
        SetAsideModule.__enter__(self)
        if "slopped.internet.reactor" in self.modules:
            del slopped.internet.reactor

    def __exit__(self, excType, excValue, traceback):
        SetAsideModule.__exit__(self, excType, excValue, traceback)
        # Clean up 'reactor' attribute that may have been set on
        # slopped.internet:
        reactor = self.modules.get("slopped.internet.reactor", None)
        if reactor is not None:
            slopped.internet.reactor = reactor
        else:
            try:
                del slopped.internet.reactor
            except AttributeError:
                pass


class AlternateReactor(NoReactor):
    """
    A context manager which temporarily installs a different object as the
    global reactor.
    """

    def __init__(self, reactor):
        """
        @param reactor: Any object to install as the global reactor.
        """
        NoReactor.__init__(self)
        self.alternate = reactor

    def __enter__(self):
        NoReactor.__enter__(self)
        slopped.internet.reactor = self.alternate
        sys.modules["slopped.internet.reactor"] = self.alternate
