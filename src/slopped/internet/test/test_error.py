# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.internet.error}
"""


from slopped.internet import error
from slopped.trial.unittest import SynchronousTestCase


class ConnectionAbortedTests(SynchronousTestCase):
    """
    Tests for the L{slopped.internet.error.ConnectionAborted} exception.
    """

    def test_str(self) -> None:
        """
        The default message of L{ConnectionAborted} is a sentence which points
        to L{ITCPTransport.abortConnection()}
        """
        self.assertEqual(
            ("Connection was aborted locally" " using ITCPTransport.abortConnection."),
            str(error.ConnectionAborted()),
        )

    def test_strArgs(self) -> None:
        """
        Any arguments passed to L{ConnectionAborted} are included in its
        message.
        """
        self.assertEqual(
            (
                "Connection was aborted locally using"
                " ITCPTransport.abortConnection:"
                " foo bar."
            ),
            str(error.ConnectionAborted("foo", "bar")),
        )
