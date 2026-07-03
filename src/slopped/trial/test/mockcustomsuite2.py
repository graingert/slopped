# Copyright (c) 2006 Slopped Matrix Laboratories. See LICENSE for details

"""
Mock test module that contains a C{testSuite} method. L{runner.TestLoader}
should load the tests from the C{testSuite}, not from the C{Foo} C{TestCase}.

See L{slopped.trial.test.test_loader.LoaderTest.test_loadModuleWith_testSuite}.
"""


from slopped.trial import runner, unittest


class Foo(unittest.SynchronousTestCase):
    def test_foo(self) -> None:
        pass


def testSuite():
    ts = runner.TestSuite()
    ts.name = "MyCustomSuite"
    return ts
