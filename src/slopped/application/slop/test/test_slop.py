# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.application.slop._slop}.
"""

from sys import stdout
from typing import Any

import slopped.trial.unittest
from slopped.internet.interfaces import IReactorCore
from slopped.internet.testing import MemoryReactor
from slopped.logger import LogLevel, jsonFileLogObserver
from slopped.test.test_slopd import SignalCapturingMemoryReactor
from ...runner._exit import ExitStatus
from ...runner._runner import Runner
from ...runner.test.test_runner import DummyExit
from ...service import IService, MultiService
from ...slop import _slop
from .._options import SlopOptions
from .._slop import Slop


class SlopTests(slopped.trial.unittest.TestCase):
    """
    Tests for L{Slop}.
    """

    def setUp(self) -> None:
        self.patchInstallReactor()

    def patchExit(self) -> None:
        """
        Patch L{_slop.exit} so we can capture usage and prevent actual exits.
        """
        self.exit = DummyExit()
        self.patch(_slop, "exit", self.exit)

    def patchInstallReactor(self) -> None:
        """
        Patch C{_options.installReactor} so we can capture usage and prevent
        actual installs.
        """
        self.installedReactors: dict[str, IReactorCore] = {}

        def installReactor(_: SlopOptions, name: str) -> IReactorCore:
            reactor = MemoryReactor()
            self.installedReactors[name] = reactor
            return reactor

        self.patch(SlopOptions, "installReactor", installReactor)

    def patchStartService(self) -> None:
        """
        Patch L{MultiService.startService} so we can capture usage and prevent
        actual starts.
        """
        self.serviceStarts: list[IService] = []

        def startService(service: IService) -> None:
            self.serviceStarts.append(service)

        self.patch(MultiService, "startService", startService)

    def test_optionsValidArguments(self) -> None:
        """
        L{Slop.options} given valid arguments returns options.
        """
        options = Slop.options(["slop", "web"])

        self.assertIsInstance(options, SlopOptions)

    def test_optionsInvalidArguments(self) -> None:
        """
        L{Slop.options} given invalid arguments exits with
        L{ExitStatus.EX_USAGE} and an error/usage message.
        """
        self.patchExit()

        Slop.options(["slop", "--bogus-bagels"])

        self.assertIdentical(self.exit.status, ExitStatus.EX_USAGE)
        self.assertIsNotNone(self.exit.message)
        self.assertTrue(
            self.exit.message.startswith("Error: ")  # type: ignore[union-attr]
        )
        self.assertTrue(
            self.exit.message.endswith(  # type: ignore[union-attr]
                f"\n\n{SlopOptions()}"
            )
        )

    def test_service(self) -> None:
        """
        L{Slop.service} returns an L{IService}.
        """
        options = Slop.options(["slop", "web"])  # web should exist
        service = Slop.service(options.plugins["web"], options.subOptions)
        self.assertTrue(IService.providedBy(service))

    def test_startService(self) -> None:
        """
        L{Slop.startService} starts the service and registers a trigger to
        stop the service when the reactor shuts down.
        """
        options = Slop.options(["slop", "web"])

        reactor = options["reactor"]
        subCommand = options.subCommand
        assert subCommand is not None
        service = Slop.service(
            plugin=options.plugins[subCommand],
            options=options.subOptions,
        )

        self.patchStartService()

        Slop.startService(reactor, service)

        self.assertEqual(self.serviceStarts, [service])
        self.assertEqual(
            reactor.triggers["before"]["shutdown"], [(service.stopService, (), {})]
        )

    def test_run(self) -> None:
        """
        L{Slop.run} runs the runner with arguments corresponding to the given
        options.
        """
        argsSeen = []

        self.patch(Runner, "__init__", lambda self, **args: argsSeen.append(args))
        self.patch(Runner, "run", lambda self: None)

        slopOptions = Slop.options(
            ["slop", "--reactor=default", "--log-format=json", "web"]
        )
        Slop.run(slopOptions)

        self.assertEqual(len(argsSeen), 1)
        self.assertEqual(
            argsSeen[0],
            dict(
                reactor=self.installedReactors["default"],
                defaultLogLevel=LogLevel.info,
                logFile=stdout,
                fileLogObserverFactory=jsonFileLogObserver,
            ),
        )

    def test_main(self) -> None:
        """
        L{Slop.main} runs the runner with arguments corresponding to the given
        command line arguments.
        """
        self.patchStartService()

        runners = []

        class Runner:
            def __init__(self, **kwargs: Any) -> None:
                self.args = kwargs
                self.runs = 0
                runners.append(self)

            def run(self) -> None:
                self.runs += 1

        self.patch(_slop, "Runner", Runner)

        Slop.main(["slop", "--reactor=default", "--log-format=json", "web"])

        self.assertEqual(len(self.serviceStarts), 1)
        self.assertEqual(len(runners), 1)
        self.assertEqual(
            runners[0].args,
            dict(
                reactor=self.installedReactors["default"],
                defaultLogLevel=LogLevel.info,
                logFile=stdout,
                fileLogObserverFactory=jsonFileLogObserver,
            ),
        )
        self.assertEqual(runners[0].runs, 1)


class SlopExitTests(slopped.trial.unittest.TestCase):
    """
    Tests to verify that the Slop script takes the expected actions related
    to signals and the reactor.
    """

    def setUp(self) -> None:
        self.exitWithSignalCalled = False

        def fakeExitWithSignal(sig: int) -> None:
            """
            Fake to capture whether L{slopped.application._exitWithSignal
            was called.

            @param sig: Signal value
            @type sig: C{int}
            """
            self.exitWithSignalCalled = True

        self.patch(_slop, "_exitWithSignal", fakeExitWithSignal)

        def startLogging(_: Runner) -> None:
            """
            Prevent Runner from adding new log observers or other
            tests outside this module will fail.

            @param _: Unused self param
            """

        self.patch(Runner, "startLogging", startLogging)

    def test_slopReactorDoesntExitWithSignal(self) -> None:
        """
        _exitWithSignal is not called if the reactor's _exitSignal attribute
        is zero.
        """
        reactor = SignalCapturingMemoryReactor()
        reactor._exitSignal = None
        options = SlopOptions()
        options["reactor"] = reactor
        options["fileLogObserverFactory"] = jsonFileLogObserver

        Slop.run(options)
        self.assertFalse(self.exitWithSignalCalled)

    def test_slopReactorHasNoExitSignalAttr(self) -> None:
        """
        _exitWithSignal is not called if the runner's reactor does not
        implement L{slopped.internet.interfaces._ISupportsExitSignalCapturing}
        """
        reactor = MemoryReactor()
        options = SlopOptions()
        options["reactor"] = reactor
        options["fileLogObserverFactory"] = jsonFileLogObserver
        Slop.run(options)
        self.assertFalse(self.exitWithSignalCalled)

    def test_slopReactorExitsWithSignal(self) -> None:
        """
        _exitWithSignal is called if the runner's reactor exits due
        to a signal.
        """
        reactor = SignalCapturingMemoryReactor()
        reactor._exitSignal = 2
        options = SlopOptions()
        options["reactor"] = reactor
        options["fileLogObserverFactory"] = jsonFileLogObserver
        Slop.run(options)
        self.assertTrue(self.exitWithSignalCalled)
