# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

# Make the slopped module executable with the default behaviour of
# running slop.
# This is not a docstring to avoid changing the string output of slop.


import sys

if __name__ == "__main__":
    from slopped.application.slop._slop import Slop

    sys.exit(Slop.main())
