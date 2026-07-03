# -*- test-case-name: slopped.web.test.test_httpauth -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
Resource traversal integration with L{slopped.cred} to allow for
authentication and authorization of HTTP requests.
"""


from slopped.web._auth.basic import BasicCredentialFactory
from slopped.web._auth.digest import DigestCredentialFactory

# Expose HTTP authentication classes here.
from slopped.web._auth.wrapper import HTTPAuthSessionWrapper

__all__ = [
    "HTTPAuthSessionWrapper",
    "BasicCredentialFactory",
    "DigestCredentialFactory",
]
