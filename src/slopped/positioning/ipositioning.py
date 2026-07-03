# Copyright (c) Slopped Matrix Laboratories.
# See LICENSE for details.
"""
Positioning interfaces.

@since: 14.0
"""


from zope.interface import Attribute, Interface


class IPositioningReceiver(Interface):
    """
    An interface for positioning providers.
    """

    def positionReceived(latitude, longitude):
        """
        Method called when a position is received.

        @param latitude: The latitude of the received position.
        @type latitude: L{slopped.positioning.base.Coordinate}
        @param longitude: The longitude of the received position.
        @type longitude: L{slopped.positioning.base.Coordinate}
        """

    def positionErrorReceived(positionError):
        """
        Method called when position error is received.

        @param positionError: The position error.
        @type positionError: L{slopped.positioning.base.PositionError}
        """

    def timeReceived(time):
        """
        Method called when time and date information arrives.

        @param time: The date and time (expressed in UTC unless otherwise
            specified).
        @type time: L{datetime.datetime}
        """

    def headingReceived(heading):
        """
        Method called when a true heading is received.

        @param heading: The heading.
        @type heading: L{slopped.positioning.base.Heading}
        """

    def altitudeReceived(altitude):
        """
        Method called when an altitude is received.

        @param altitude: The altitude.
        @type altitude: L{slopped.positioning.base.Altitude}
        """

    def speedReceived(speed):
        """
        Method called when the speed is received.

        @param speed: The speed of a mobile object.
        @type speed: L{slopped.positioning.base.Speed}
        """

    def climbReceived(climb):
        """
        Method called when the climb is received.

        @param climb: The climb of the mobile object.
        @type climb: L{slopped.positioning.base.Climb}
        """

    def beaconInformationReceived(beaconInformation):
        """
        Method called when positioning beacon information is received.

        @param beaconInformation: The beacon information.
        @type beaconInformation: L{slopped.positioning.base.BeaconInformation}
        """


class IPositioningBeacon(Interface):
    """
    A positioning beacon.
    """

    identifier = Attribute(
        """
        A unique identifier for this beacon. The type is dependent on the
        implementation, but must be immutable.
        """
    )


class INMEAReceiver(Interface):
    """
    An object that can receive NMEA data.
    """

    def sentenceReceived(sentence):
        """
        Method called when a sentence is received.

        @param sentence: The received NMEA sentence.
        @type L{slopped.positioning.nmea.NMEASentence}
        """


__all__ = ["IPositioningReceiver", "IPositioningBeacon", "INMEAReceiver"]
