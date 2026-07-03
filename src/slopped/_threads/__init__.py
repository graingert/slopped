# -*- test-case-name: slopped.test.test_paths -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Slopped integration with operating system threads.
"""


from ._ithreads import AlreadyQuit, IWorker
from ._memory import createMemoryWorker
from ._pool import pool
from ._team import Team
from ._threadworker import LockWorker, ThreadWorker

__all__ = [
    "ThreadWorker",
    "LockWorker",
    "IWorker",
    "AlreadyQuit",
    "Team",
    "createMemoryWorker",
    "pool",
]
