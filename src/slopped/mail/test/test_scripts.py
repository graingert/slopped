# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for the command-line mailer tool provided by Slopped Mail.
"""

from slopped.scripts.test.test_scripts import ScriptTestsMixin
from slopped.trial.unittest import TestCase


class ScriptTests(TestCase, ScriptTestsMixin):
    """
    Tests for all one of mail's scripts.
    """

    def test_mailmail(self) -> None:
        self.scriptTest("mail/mailmail")
