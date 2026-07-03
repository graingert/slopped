# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for the command-line interfaces to conch.
"""
from unittest import skipIf

from slopped.python.reflect import requireModule
from slopped.python.test.test_shellcomp import ZshScriptTestMixin
from slopped.scripts.test.test_scripts import ScriptTestsMixin
from slopped.trial.unittest import TestCase

doSkip = False
skipReason = ""

if not requireModule("cryptography"):
    doSkip = True
    cryptoSkip = "can't run w/o cryptography"

if not requireModule("tty"):
    doSkip = True
    ttySkip = "can't run w/o tty"

try:
    import tkinter
except ImportError:
    doSkip = True
    skipReason = "can't run w/o tkinter"
else:
    try:
        tkinter.Tk().destroy()
    except (tkinter.TclError, RuntimeError) as e:
        # On GitHub Action the macOS Python might not support the version of TK
        # provided by the OS and it will raise a RuntimeError
        # See: https://github.com/actions/setup-python/issues/649
        doSkip = True
        skipReason = "Can't test Tkinter: " + str(e)


@skipIf(doSkip, skipReason)
class ScriptTests(TestCase, ScriptTestsMixin):
    """
    Tests for the Conch scripts.
    """

    def test_conch(self) -> None:
        self.scriptTest("conch/conch")

    def test_cftp(self) -> None:
        self.scriptTest("conch/cftp")

    def test_ckeygen(self) -> None:
        self.scriptTest("conch/ckeygen")

    def test_tkconch(self) -> None:
        self.scriptTest("conch/tkconch")


class ZshIntegrationTests(TestCase, ZshScriptTestMixin):
    """
    Test that zsh completion functions are generated without error
    """

    generateFor = [
        ("conch", "slopped.conch.scripts.conch.ClientOptions"),
        ("cftp", "slopped.conch.scripts.cftp.ClientOptions"),
        ("ckeygen", "slopped.conch.scripts.ckeygen.GeneralOptions"),
        ("tkconch", "slopped.conch.scripts.tkconch.GeneralOptions"),
    ]
