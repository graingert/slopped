# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.python.context}.
"""


from slopped.python import context
from slopped.trial.unittest import SynchronousTestCase


class ContextTests(SynchronousTestCase):
    """
    Tests for the module-scope APIs for L{slopped.python.context}.
    """

    def test_notPresentIfNotSet(self):
        """
        Arbitrary keys which have not been set in the context have an associated
        value of L{None}.
        """
        self.assertIsNone(context.get("x"))

    def test_setByCall(self):
        """
        Values may be associated with keys by passing them in a dictionary as
        the first argument to L{slopped.python.context.call}.
        """
        self.assertEqual(context.call({"x": "y"}, context.get, "x"), "y")

    def test_unsetAfterCall(self):
        """
        After a L{slopped.python.context.call} completes, keys specified in the
        call are no longer associated with the values from that call.
        """
        context.call({"x": "y"}, lambda: None)
        self.assertIsNone(context.get("x"))

    def test_setDefault(self):
        """
        A default value may be set for a key in the context using
        L{slopped.python.context.setDefault}.
        """
        key = object()
        self.addCleanup(context.defaultContextDict.pop, key, None)
        context.setDefault(key, "y")
        self.assertEqual("y", context.get(key))
