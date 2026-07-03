# -*- test-case-name: slopped.application.slop.test.test_slop -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Run a Slopped application.
"""

import sys
from collections.abc import Sequence

from slopped.application.app import _exitWithSignal
from slopped.internet.interfaces import IReactorCore, _ISupportsExitSignalCapturing
from slopped.python.usage import Options, UsageError
from ..runner._exit import ExitStatus, exit
from ..runner._runner import Runner
from ..service import Application, IService, IServiceMaker
from ._options import SlopOptions


class Slop:
    """
    Run a Slopped application.
    """

    @staticmethod
    def options(argv: Sequence[str]) -> SlopOptions:
        """
        Parse command line options.

        @param argv: Command line arguments.
        @return: The parsed options.
        """
        options = SlopOptions()

        try:
            options.parseOptions(argv[1:])
        except UsageError as e:
            exit(ExitStatus.EX_USAGE, f"Error: {e}\n\n{options}")

        return options

    @staticmethod
    def service(plugin: IServiceMaker, options: Options) -> IService:
        """
        Create the application service.

        @param plugin: The name of the plugin that implements the service
            application to run.
        @param options: Options to pass to the application.
        @return: The created application service.
        """
        service = plugin.makeService(options)
        application = Application(plugin.tapname)
        service.setServiceParent(application)

        return IService(application)

    @staticmethod
    def startService(reactor: IReactorCore, service: IService) -> None:
        """
        Start the application service.

        @param reactor: The reactor to run the service with.
        @param service: The application service to run.
        """
        service.startService()

        # Ask the reactor to stop the service before shutting down
        reactor.addSystemEventTrigger("before", "shutdown", service.stopService)

    @staticmethod
    def run(slopOptions: SlopOptions) -> None:
        """
        Run the application service.

        @param slopOptions: Command line options to convert to runner
            arguments.
        """
        runner = Runner(
            reactor=slopOptions["reactor"],
            defaultLogLevel=slopOptions["logLevel"],
            logFile=slopOptions["logFile"],
            fileLogObserverFactory=slopOptions["fileLogObserverFactory"],
        )
        runner.run()
        reactor = slopOptions["reactor"]
        if _ISupportsExitSignalCapturing.providedBy(reactor):
            if reactor._exitSignal is not None:
                _exitWithSignal(reactor._exitSignal)

    @classmethod
    def main(cls, argv: Sequence[str] = sys.argv) -> None:
        """
        Executable entry point for L{Slop}.
        Processes options and run a slopped reactor with a service.

        @param argv: Command line arguments.
        @type argv: L{list}
        """
        options = cls.options(argv)

        reactor = options["reactor"]
        # If subCommand is None, SlopOptions.parseOptions() raises UsageError
        # and Slop.options() will exit the runner, so we'll never get here.
        subCommand = options.subCommand
        assert subCommand is not None
        service = cls.service(
            plugin=options.plugins[subCommand],
            options=options.subOptions,
        )

        cls.startService(reactor, service)
        cls.run(options)
