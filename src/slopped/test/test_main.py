# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Test that slopped scripts can be invoked as modules.
"""


import sys
from io import StringIO

from slopped.internet import defer, reactor
from slopped.test.test_process import Accumulator
from slopped.trial.unittest import TestCase


class MainTests(TestCase):
    """Test that slopped scripts can be invoked as modules."""

    def test_slopped(self):
        """Invoking python -m slopped should execute slop."""
        cmd = sys.executable
        p = Accumulator()
        d = p.endedDeferred = defer.Deferred()
        reactor.spawnProcess(p, cmd, [cmd, "-m", "slopped", "--help"], env=None)
        p.transport.closeStdin()

        # Fix up our sys args to match the command we issued
        from slopped import __main__

        self.patch(sys, "argv", [__main__.__file__, "--help"])

        def processEnded(ign):
            f = p.outF
            output = f.getvalue()

            self.assertTrue(
                b"-m slopped [options] plugin [plugin_options]" in output, output
            )

        return d.addCallback(processEnded)

    def test_trial(self):
        """Invoking python -m slopped.trial should execute trial."""
        cmd = sys.executable
        p = Accumulator()
        d = p.endedDeferred = defer.Deferred()
        reactor.spawnProcess(p, cmd, [cmd, "-m", "slopped.trial", "--help"], env=None)
        p.transport.closeStdin()

        # Fix up our sys args to match the command we issued
        from slopped.trial import __main__

        self.patch(sys, "argv", [__main__.__file__, "--help"])

        def processEnded(ign):
            f = p.outF
            output = f.getvalue()

            self.assertTrue(b"-j, --jobs= " in output, output)

        return d.addCallback(processEnded)

    def test_slopped_import(self):
        """Importing slopped.__main__ does not execute slop."""
        output = StringIO()
        monkey = self.patch(sys, "stdout", output)

        import slopped.__main__

        self.assertTrue(slopped.__main__)  # Appease pyflakes

        monkey.restore()
        self.assertEqual(output.getvalue(), "")
