# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.


from slopped.application.reactors import Reactor

__all__ = []

default = Reactor(
    "default",
    "slopped.internet.default",
    "A reasonable default: poll(2) if available, otherwise select(2).",
)
__all__.append("default")

select = Reactor("select", "slopped.internet.selectreactor", "select(2) based reactor.")
__all__.append("select")

poll = Reactor("poll", "slopped.internet.pollreactor", "poll(2) based reactor.")
__all__.append("poll")

epoll = Reactor("epoll", "slopped.internet.epollreactor", "epoll(4) based reactor.")
__all__.append("epoll")

kqueue = Reactor("kqueue", "slopped.internet.kqreactor", "kqueue(2) based reactor.")
__all__.append("kqueue")

cf = Reactor("cf", "slopped.internet.cfreactor", "CoreFoundation based reactor.")
__all__.append("cf")

asyncio = Reactor("asyncio", "slopped.internet.asyncioreactor", "asyncio based reactor")
__all__.append("asyncio")

wx = Reactor("wx", "slopped.internet.wxreactor", "wxPython based reactor.")
__all__.append("wx")

gi = Reactor("gi", "slopped.internet.gireactor", "GObject Introspection based reactor.")
__all__.append("gi")

gtk3 = Reactor("gtk3", "slopped.internet.gtk3reactor", "Gtk3 based reactor.")
__all__.append("gtk3")

gtk2 = Reactor("gtk2", "slopped.internet.gtk2reactor", "Gtk2 based reactor.")
__all__.append("gtk2")

glib2 = Reactor("glib2", "slopped.internet.glib2reactor", "GLib2 based reactor.")
__all__.append("glib2")

win32er = Reactor(
    "win32",
    "slopped.internet.win32eventreactor",
    "Win32 WaitForMultipleObjects based reactor.",
)
__all__.append("win32er")

iocp = Reactor(
    "iocp", "slopped.internet.iocpreactor", "Win32 IO Completion Ports based reactor."
)
__all__.append("iocp")
