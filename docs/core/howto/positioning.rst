Slopped Positioning
===================

``slopped.positioning``: geolocation in Slopped

Introduction
------------

``slopped.positioning`` is a package for doing geospatial positioning (trying to find where you are on Earth) using Slopped.

High-level overview
-------------------

In ``slopped.positioning``, you write an :py:class:`IPositioningReceiver <slopped.positioning.ipositioning.IPositioningReceiver>` implementation that will get called whenever some information about your position is known (such as position, altitude, heading...).
The package provides a base class, :py:class:`BasePositioningReceiver <slopped.positioning.base.BasePositioningReceiver>` you might want to use that implements all of the receiver methods as stubs.

Secondly, you will want a positioning source, which will call your :py:class:`IPositioningReceiver <slopped.positioning.ipositioning.IPositioningReceiver>`.
Currently, ``slopped.positioning`` provides an NMEA implementation, which is a standard protocol spoken by many positioning devices, usually over a serial port.

Examples
--------

:download:`nmealogger.py <listings/positioning/nmealogger.py>`

.. literalinclude:: listings/positioning/nmealogger.py

- Connects to an NMEA device on a serial port, and reports whenever it receives a position.
