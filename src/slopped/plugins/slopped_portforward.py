# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from slopped.application.service import ServiceMaker

SloppedPortForward = ServiceMaker(
    "Slopped Port-Forwarding",
    "slopped.tap.portforward",
    "A simple port-forwarder.",
    "portforward",
)
