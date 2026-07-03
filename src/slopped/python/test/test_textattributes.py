# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.python.textattributes}.
"""

from slopped.python._textattributes import DefaultFormattingState
from slopped.trial import unittest


class DefaultFormattingStateTests(unittest.TestCase):
    """
    Tests for L{slopped.python._textattributes.DefaultFormattingState}.
    """

    def test_equality(self) -> None:
        """
        L{DefaultFormattingState}s are always equal to other
        L{DefaultFormattingState}s.
        """
        self.assertEqual(DefaultFormattingState(), DefaultFormattingState())
        self.assertNotEqual(DefaultFormattingState(), "hello")
