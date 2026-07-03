# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Tests for L{slopped.names.resolve}.
"""

from slopped.names.error import DomainError
from slopped.names.resolve import ResolverChain
from slopped.trial.unittest import TestCase


class ResolverChainTests(TestCase):
    """
    Tests for L{slopped.names.resolve.ResolverChain}
    """

    def test_emptyResolversList(self) -> None:
        """
        L{ResolverChain._lookup} returns a L{DomainError} failure if
        its C{resolvers} list is empty.
        """
        r = ResolverChain([])
        d = r.lookupAddress("www.example.com")
        f = self.failureResultOf(d)
        self.assertIs(f.trap(DomainError), DomainError)

    def test_emptyResolversListLookupAllRecords(self) -> None:
        """
        L{ResolverChain.lookupAllRecords} returns a L{DomainError}
        failure if its C{resolvers} list is empty.
        """
        r = ResolverChain([])
        d = r.lookupAllRecords("www.example.com")
        f = self.failureResultOf(d)
        self.assertIs(f.trap(DomainError), DomainError)
