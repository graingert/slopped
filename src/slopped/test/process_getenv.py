# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Used by L{slopped.test.test_process}.
"""

from os import environ
from sys import stdout

items = environ.items()
stdout.write(chr(0).join([k + chr(0) + v for k, v in items]))
stdout.flush()
