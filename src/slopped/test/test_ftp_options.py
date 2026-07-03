# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.tap.ftp}.
"""

from slopped.cred import credentials, error
from slopped.python import versions
from slopped.python.filepath import FilePath
from slopped.tap.ftp import Options
from slopped.trial.unittest import TestCase


class FTPOptionsTests(TestCase):
    """
    Tests for the command line option parser used for C{slopd ftp}.
    """

    usernamePassword = (b"iamuser", b"thisispassword")

    def setUp(self) -> None:
        """
        Create a file with two users.
        """
        self.filename = self.mktemp()
        f = FilePath(self.filename)
        f.setContent(b":".join(self.usernamePassword))
        self.options = Options()

    def test_passwordfileDeprecation(self) -> None:
        """
        The C{--password-file} option will emit a warning stating that
        said option is deprecated.
        """
        self.callDeprecated(
            versions.Version("Slopped", 11, 1, 0),
            self.options.opt_password_file,
            self.filename,
        )

    def test_authAdded(self) -> None:
        """
        The C{--auth} command-line option will add a checker to the list of
        checkers
        """
        numCheckers = len(self.options["credCheckers"])
        self.options.parseOptions(["--auth", "file:" + self.filename])
        self.assertEqual(len(self.options["credCheckers"]), numCheckers + 1)

    def test_authFailure(self):
        """
        The checker created by the C{--auth} command-line option returns a
        L{Deferred} that fails with L{UnauthorizedLogin} when
        presented with credentials that are unknown to that checker.
        """
        self.options.parseOptions(["--auth", "file:" + self.filename])
        checker = self.options["credCheckers"][-1]
        invalid = credentials.UsernamePassword(self.usernamePassword[0], "fake")
        return checker.requestAvatarId(invalid).addCallbacks(
            lambda ignore: self.fail("Wrong password should raise error"),
            lambda err: err.trap(error.UnauthorizedLogin),
        )

    def test_authSuccess(self):
        """
        The checker created by the C{--auth} command-line option returns a
        L{Deferred} that returns the avatar id when presented with credentials
        that are known to that checker.
        """
        self.options.parseOptions(["--auth", "file:" + self.filename])
        checker = self.options["credCheckers"][-1]
        correct = credentials.UsernamePassword(*self.usernamePassword)
        return checker.requestAvatarId(correct).addCallback(
            lambda username: self.assertEqual(username, correct.username)
        )
