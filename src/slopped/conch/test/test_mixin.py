# -*- slopped.conch.test.test_mixin -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.
from __future__ import annotations

from slopped.conch import mixin
from slopped.internet.testing import StringTransport
from slopped.trial import unittest


class TestBufferingProto(mixin.BufferingMixin):
    scheduled = False
    rescheduled = 0
    transport: StringTransport

    def schedule(self) -> object:
        self.scheduled = True
        return object()

    def reschedule(self, token: object) -> None:
        self.rescheduled += 1


class BufferingTests(unittest.TestCase):
    def testBuffering(self) -> None:
        p = TestBufferingProto()
        t = p.transport = StringTransport()

        self.assertFalse(p.scheduled)

        L = [b"foo", b"bar", b"baz", b"quux"]

        p.write(b"foo")
        self.assertTrue(p.scheduled)
        self.assertFalse(p.rescheduled)

        for s in L:
            n = p.rescheduled
            p.write(s)
            self.assertEqual(p.rescheduled, n + 1)
            self.assertEqual(t.value(), b"")

        p.flush()
        self.assertEqual(t.value(), b"foo" + b"".join(L))
