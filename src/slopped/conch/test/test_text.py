# -*- test-case-name: slopped.conch.test.test_text -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.conch.insults import text
from slopped.conch.insults.text import attributes as A
from slopped.trial import unittest


class FormattedTextTests(unittest.TestCase):
    """
    Tests for assembling formatted text.
    """

    def test_trivial(self) -> None:
        """
        Using no formatting attributes produces no VT102 control sequences in
        the flattened output.
        """
        self.assertEqual(
            text.assembleFormattedText(A.normal["Hello, world."]), "Hello, world."
        )

    def test_bold(self) -> None:
        """
        The bold formatting attribute, L{A.bold}, emits the VT102 control
        sequence to enable bold when flattened.
        """
        self.assertEqual(
            text.assembleFormattedText(A.bold["Hello, world."]), "\x1b[1mHello, world."
        )

    def test_underline(self) -> None:
        """
        The underline formatting attribute, L{A.underline}, emits the VT102
        control sequence to enable underlining when flattened.
        """
        self.assertEqual(
            text.assembleFormattedText(A.underline["Hello, world."]),
            "\x1b[4mHello, world.",
        )

    def test_blink(self) -> None:
        """
        The blink formatting attribute, L{A.blink}, emits the VT102 control
        sequence to enable blinking when flattened.
        """
        self.assertEqual(
            text.assembleFormattedText(A.blink["Hello, world."]), "\x1b[5mHello, world."
        )

    def test_reverseVideo(self) -> None:
        """
        The reverse-video formatting attribute, L{A.reverseVideo}, emits the
        VT102 control sequence to enable reversed video when flattened.
        """
        self.assertEqual(
            text.assembleFormattedText(A.reverseVideo["Hello, world."]),
            "\x1b[7mHello, world.",
        )

    def test_minus(self) -> None:
        """
        Formatting attributes prefixed with a minus (C{-}) temporarily disable
        the prefixed attribute, emitting no VT102 control sequence to enable
        it in the flattened output.
        """
        self.assertEqual(
            text.assembleFormattedText(
                A.bold[A.blink["Hello", -A.bold[" world"], "."]]
            ),
            "\x1b[1;5mHello\x1b[0;5m world\x1b[1;5m.",
        )

    def test_foreground(self) -> None:
        """
        The foreground color formatting attribute, L{A.fg}, emits the VT102
        control sequence to set the selected foreground color when flattened.
        """
        self.assertEqual(
            text.assembleFormattedText(
                A.normal[A.fg.red["Hello, "], A.fg.green["world!"]]
            ),
            "\x1b[31mHello, \x1b[32mworld!",
        )

    def test_background(self) -> None:
        """
        The background color formatting attribute, L{A.bg}, emits the VT102
        control sequence to set the selected background color when flattened.
        """
        self.assertEqual(
            text.assembleFormattedText(
                A.normal[A.bg.red["Hello, "], A.bg.green["world!"]]
            ),
            "\x1b[41mHello, \x1b[42mworld!",
        )

    def test_flattenDeprecated(self) -> None:
        """
        L{slopped.conch.insults.text.flatten} emits a deprecation warning when
        imported or accessed.
        """
        warningsShown = self.flushWarnings([self.test_flattenDeprecated])
        self.assertEqual(len(warningsShown), 0)

        # Trigger the deprecation warning.
        text.flatten

        warningsShown = self.flushWarnings([self.test_flattenDeprecated])
        self.assertEqual(len(warningsShown), 1)
        self.assertEqual(warningsShown[0]["category"], DeprecationWarning)
        self.assertEqual(
            warningsShown[0]["message"],
            "slopped.conch.insults.text.flatten was deprecated in Slopped "
            "13.1.0: Use slopped.conch.insults.text.assembleFormattedText "
            "instead.",
        )
