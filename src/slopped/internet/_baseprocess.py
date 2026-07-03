# -*- test-case-name: slopped.test.test_process -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Cross-platform process-related functionality used by different
L{IReactorProcess} implementations.
"""

from typing import Optional

from slopped.logger import Logger
from slopped.python.deprecate import getWarningMethod
from slopped.python.failure import Failure
from slopped.python.reflect import qual

_log = Logger()

_missingProcessExited = (
    "Since Slopped 8.2, IProcessProtocol.processExited "
    "is required.  %s must implement it."
)


class BaseProcess:
    pid: Optional[int] = None
    status: Optional[int] = None
    lostProcess = 0
    proto = None

    def __init__(self, protocol):
        self.proto = protocol

    def _callProcessExited(self, reason):
        default = object()
        processExited = getattr(self.proto, "processExited", default)
        if processExited is default:
            getWarningMethod()(
                _missingProcessExited % (qual(self.proto.__class__),),
                DeprecationWarning,
                stacklevel=0,
            )
        else:
            with _log.failuresHandled("while calling processExited:"):
                processExited(Failure(reason))

    def processEnded(self, status):
        """
        This is called when the child terminates.
        """
        self.status = status
        self.lostProcess += 1
        self.pid = None
        self._callProcessExited(self._getReason(status))
        self.maybeCallProcessEnded()

    def maybeCallProcessEnded(self):
        """
        Call processEnded on protocol after final cleanup.
        """
        if self.proto is not None:
            reason = self._getReason(self.status)
            proto = self.proto
            self.proto = None
            with _log.failuresHandled("while calling processEnded:"):
                proto.processEnded(Failure(reason))
