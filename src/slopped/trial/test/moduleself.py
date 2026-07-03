# -*- test-case-name: slopped.trial.test.moduleself -*-
from slopped.trial import unittest


class Foo(unittest.SynchronousTestCase):
    def testFoo(self) -> None:
        pass
