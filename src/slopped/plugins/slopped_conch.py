# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.application.service import ServiceMaker

SloppedSSH = ServiceMaker(
    "Slopped Conch Server", "slopped.conch.tap", "A Conch SSH service.", "conch"
)

SloppedManhole = ServiceMaker(
    "Slopped Manhole (new)",
    "slopped.conch.manhole_tap",
    (
        "An interactive remote debugger service accessible via telnet "
        "and ssh and providing syntax coloring and basic line editing "
        "functionality."
    ),
    "manhole",
)
