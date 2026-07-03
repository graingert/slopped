# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.application.service import ServiceMaker

SloppedINETD = ServiceMaker(
    "Slopped INETD Server",
    "slopped.runner.inetdtap",
    "An inetd(8) replacement.",
    "inetd",
)
