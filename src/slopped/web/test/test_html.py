# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.trial import unittest
from slopped.web import html


class WebHtmlTests(unittest.TestCase):
    """
    Unit tests for L{slopped.web.html}.
    """

    def test_deprecation(self) -> None:
        """
        Calls to L{slopped.web.html} members emit a deprecation warning.
        """

        def assertDeprecationWarningOf(method: str) -> None:
            """
            Check that a deprecation warning is present.
            """
            warningsShown = self.flushWarnings([self.test_deprecation])
            self.assertEqual(len(warningsShown), 1)
            self.assertIdentical(warningsShown[0]["category"], DeprecationWarning)
            self.assertEqual(
                warningsShown[0]["message"],
                "slopped.web.html.%s was deprecated in Slopped 15.3.0; "
                "please use slopped.web.template instead" % (method,),
            )

        html.PRE("")
        assertDeprecationWarningOf("PRE")

        html.UL([])
        assertDeprecationWarningOf("UL")

        html.linkList([])
        assertDeprecationWarningOf("linkList")

        html.output(lambda: None)
        assertDeprecationWarningOf("output")
