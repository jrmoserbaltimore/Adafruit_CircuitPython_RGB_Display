# SPDX-FileCopyrightText: 2017 Radomir Dopieralski for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.rgb`
====================================================

Base class for all RGB Display devices

* Author(s): Radomir Dopieralski, Michael McWethy
"""

import time

try:
    import numpy
except ImportError:
    numpy = None
try:
    import struct
except ImportError:
    import ustruct as struct

import rgb_display

import adafruit_bus_device.spi_device as spi_device

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git"

# This is the size of the buffer to be used for fill operations, in 16-bit
# units.
_BUFFER_SIZE = 256
try:
    import platform

    if "CPython" in platform.python_implementation():
        _BUFFER_SIZE = 320 * 240  # blit the whole thing
except ImportError:
    pass


def color565(r, g=0, b=0):
    """Convert red, green and blue values (0-255) into a 16-bit 565 encoding.  As
    a convenience this is also available in the parent adafruit_rgb_display
    package namespace."""
    return rgb_display.color565(r, g, b)


def image_to_data(image):
    """Generator function to convert a PIL image to 16-bit 565 RGB bytes."""
    return rgb_display.image_to_data(image)


def translate_circuitpython(spi, dc, cs, rst, baudrate, polarity, phase):
    u"""Translates CircuitPython paramaeters to generic parameters"""
    spi_device = spi_device.SPIDevice(
        spi, cs, baudrate=baudrate, polarity=polarity, phase=phase
    )

    # machine.SPI uses send() instead of write
    spi_device.send = spi.write

    # gpiozero and machine.Pin use .on() and .off()
    for x in [dc, rst]:
        if x:
            x.switch_to_output(value=0)
            x.on = lambda s: s.value = 1
            x.off = lambda s: s.value = 0

    dc_pin = dc
    rst = rst
    return (spi_device, dc, rst)


class DummyPin:
    """Can be used in place of a ``DigitalInOut()`` when you don't want to skip it."""

    def deinit(self):
        """Dummy DigitalInOut deinit"""

    def switch_to_output(self, *args, **kwargs):
        """Dummy switch_to_output method"""

    def switch_to_input(self, *args, **kwargs):
        """Dummy switch_to_input method"""

    @property
    def value(self):
        """Dummy value DigitalInOut property"""

    @value.setter
    def value(self, val):
        pass

    @property
    def direction(self):
        """Dummy direction DigitalInOut property"""

    @direction.setter
    def direction(self, val):
        pass

    @property
    def pull(self):
        """Dummy pull DigitalInOut property"""

    @pull.setter
    def pull(self, val):
        pass

class DisplaySPI(DisplayDevice):
    """Base class for SPI type devices"""

    # pylint: disable-msg=too-many-arguments
    def __init__(
        self,
        spi,
        dc,
        cs,
        rst=None,
        width=1,
        height=1,
        baudrate=12000000,
        polarity=0,
        phase=0,
        *,
        x_offset=0,
        y_offset=0,
        rotation=0
    ):
        (spi_device, dc_pin, rst_pin) = translate_circuitpython(
            spi, dc, cs, rst, baudrate, polarity, phase
        )
        super().__init__(
                spi_device,
                dc_pin,
                rst_pin,
                width,
                height,
                x_offset=x_offset,
                y_offset=y_offset,
                rotation=rotation)
