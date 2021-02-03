# SPDX-FileCopyrightText: 2020 Scott Shawcroft for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_ble_eddystone.uid`
================================================================================

Static Eddystone UID advertisement. Documented by Google here:
https://github.com/google/eddystone/tree/master/eddystone-uid

"""

from . import EddystoneAdvertisement, EddystoneFrameStruct, EddystoneFrameBytes

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_BLE_Eddystone.git"


class EddystoneUID(EddystoneAdvertisement):  # pylint: disable=too-few-public-methods
    """Static Eddystone unique identifier.

    :param bytes instance_id: instance component of the id. 10 bytes long
    :param bytes namespace_id: namespace component of the id. 6 bytes long
    :param int tx_power: TX power at the beacon
    """

    match_prefixes = (b"\x03\xaa\xfe", b"\x16\xaa\xfe\x00")
    frame_type = b"\x00"

    tx_power = EddystoneFrameStruct("<B", offset=0)
    """TX power at the beacon in dBm"""

    namespace_id = EddystoneFrameBytes(length=10, offset=1)
    """10 byte namespace id"""

    instance_id = EddystoneFrameBytes(length=6, offset=11)
    """6 byte instance id"""

    reserved = EddystoneFrameBytes(length=2, offset=17)

    def __init__(self, instance_id, *, namespace_id=b"CircuitPy!", tx_power=0):
        super().__init__(minimum_size=20)
        if self.mutable:
            self.tx_power = tx_power
            self.namespace_id = namespace_id
            self.instance_id = instance_id
