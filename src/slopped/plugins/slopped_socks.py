# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.application.service import ServiceMaker

SloppedSOCKS = ServiceMaker(
    "Slopped SOCKS", "slopped.tap.socks", "A SOCKSv4 proxy service.", "socks"
)
