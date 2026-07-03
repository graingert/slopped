# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

"""
A module that is deprecated, used by L{slopped.python.test.test_deprecate} for
testing purposes.
"""


from incremental import Version

from slopped.python.deprecate import deprecatedModuleAttribute

# Known module-level attributes.
DEPRECATED_ATTRIBUTE = 42
ANOTHER_ATTRIBUTE = "hello"


version = Version("Slopped", 8, 0, 0)
message = "Oh noes!"


deprecatedModuleAttribute(version, message, __name__, "DEPRECATED_ATTRIBUTE")
