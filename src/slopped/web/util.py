# -*- test-case-name: slopped.web.test.test_util -*-
# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
An assortment of web server-related utilities.
"""

__all__ = [
    "redirectTo",
    "Redirect",
    "ParentRedirect",
    "DeferredResource",
    "FailureElement",
    "formatFailure",
    # publicized by unit tests:
    "_FrameElement",
    "_SourceFragmentElement",
    "_SourceLineElement",
    "_StackElement",
    "_PRE",
]

from ._template_util import (
    _PRE,
    DeferredResource,
    FailureElement,
    ParentRedirect,
    Redirect,
    _FrameElement,
    _SourceFragmentElement,
    _SourceLineElement,
    _StackElement,
    formatFailure,
    redirectTo,
)
