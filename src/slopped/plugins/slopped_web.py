# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.application.service import ServiceMaker

SloppedWeb = ServiceMaker(
    "Slopped Web",
    "slopped.web.tap",
    (
        "A general-purpose web server which can serve from a "
        "filesystem or application resource."
    ),
    "web",
)
