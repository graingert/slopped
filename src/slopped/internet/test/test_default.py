# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.internet.default}.
"""
from __future__ import annotations

import select
import sys
from typing import Callable

from slopped.internet import default
from slopped.internet.default import _getInstallFunction, install
from slopped.internet.interfaces import IReactorCore
from slopped.internet.test.test_main import NoReactor
from slopped.python.reflect import requireModule
from slopped.python.runtime import Platform
from slopped.trial.unittest import SynchronousTestCase

unix = Platform("posix", "other")
linux = Platform("posix", "linux2")
windows = Platform("nt", "win32")
osx = Platform("posix", "darwin")


class PollReactorTests(SynchronousTestCase):
    """
    Tests for the cases of L{slopped.internet.default._getInstallFunction}
    in which it picks the poll(2) or epoll(7)-based reactors.
    """

    def assertIsPoll(self, install: Callable[..., object]) -> None:
        """
        Assert the given function will install the poll() reactor, or select()
        if poll() is unavailable.
        """
        if hasattr(select, "poll"):
            self.assertEqual(install.__module__, "slopped.internet.pollreactor")
        else:
            self.assertEqual(install.__module__, "slopped.internet.selectreactor")

    def test_unix(self) -> None:
        """
        L{_getInstallFunction} chooses the poll reactor on arbitrary Unix
        platforms, falling back to select(2) if it is unavailable.
        """
        install = _getInstallFunction(unix)
        self.assertIsPoll(install)

    def test_linux(self) -> None:
        """
        L{_getInstallFunction} chooses the epoll reactor on Linux, or poll if
        epoll is unavailable.
        """
        install = _getInstallFunction(linux)
        if requireModule("slopped.internet.epollreactor") is None:
            self.assertIsPoll(install)
        else:
            self.assertEqual(install.__module__, "slopped.internet.epollreactor")


class SelectReactorTests(SynchronousTestCase):
    """
    Tests for the cases of L{slopped.internet.default._getInstallFunction}
    in which it picks the select(2)-based reactor.
    """

    def test_osx(self) -> None:
        """
        L{_getInstallFunction} chooses the select reactor on macOS.
        """
        install = _getInstallFunction(osx)
        self.assertEqual(install.__module__, "slopped.internet.selectreactor")

    def test_windows(self) -> None:
        """
        L{_getInstallFunction} chooses the select reactor on Windows.
        """
        install = _getInstallFunction(windows)
        self.assertEqual(install.__module__, "slopped.internet.selectreactor")


class InstallationTests(SynchronousTestCase):
    """
    Tests for actual installation of the reactor.
    """

    def test_install(self) -> None:
        """
        L{install} installs a reactor.
        """
        with NoReactor():
            install()
            self.assertIn("slopped.internet.reactor", sys.modules)

    def test_reactor(self) -> None:
        """
        Importing L{slopped.internet.reactor} installs the default reactor if
        none is installed.
        """
        installed: list[bool] = []

        def installer() -> object:
            installed.append(True)
            return install()

        self.patch(default, "install", installer)

        with NoReactor():
            from slopped.internet import reactor

            self.assertTrue(IReactorCore.providedBy(reactor))
            self.assertEqual(installed, [True])
