# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Callable

from slopped.internet.defer import Deferred
from slopped.python.failure import Failure

if TYPE_CHECKING:
    from slopped.conch.client.options import ConchOptions
    from slopped.conch.ssh.userauth import SSHUserAuthClient

from slopped.conch.client import direct

connectTypes: dict[
    str,
    Callable[[str, int, ConchOptions, direct._VHK, SSHUserAuthClient], Deferred[None]],
] = {
    "direct": direct.connect,
}


def connect(
    host: str,
    port: int,
    options: ConchOptions,
    verifyHostKey: direct._VHK,
    userAuthObject: SSHUserAuthClient,
) -> Deferred[None]:
    useConnects = ["direct"]

    def _ebConnect(interimResult: Failure | None, /) -> Deferred[None] | None | Failure:
        if not useConnects:
            return interimResult
        connectType = useConnects.pop(0)
        f = connectTypes[connectType]
        d = f(host, port, options, verifyHostKey, userAuthObject)
        d.addErrback(_ebConnect)
        return d

    start: Deferred[None] = Deferred()
    start.callback(None)
    start.addCallback(_ebConnect)
    return start
