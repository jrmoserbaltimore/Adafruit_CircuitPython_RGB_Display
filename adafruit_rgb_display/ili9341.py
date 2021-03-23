# SPDX-FileCopyrightText: 2017 Radomir Dopieralski for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.ili9341`
====================================================

A simple driver for the ILI9341/ILI9340-based displays.

* Author(s): Radomir Dopieralski, Michael McWethy
"""

from adafruit_rgb_display.rgb import translate_circuitpython
from rgb_display import ILI9341 as rgb_ILI9341

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git"


class ILI9341(rgb_ILI9341):
    """
    A simple driver for the ILI9341/ILI9340-based displays.

    >>> import busio
    >>> import digitalio
    >>> import board
    >>> from adafruit_rgb_display import color565
    >>> import adafruit_rgb_display.ili9341 as ili9341
    >>> spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    >>> display = ili9341.ILI9341(spi, cs=digitalio.DigitalInOut(board.GPIO0),
    ...    dc=digitalio.DigitalInOut(board.GPIO15))
    >>> display.fill(color565(0xff, 0x11, 0x22))
    >>> display.pixel(120, 160, 0)
    """

    # pylint: disable-msg=too-many-arguments
    def __init__(
        self,
        spi,
        dc,
        cs,
        rst=None,
        width=240,
        height=320,
        baudrate=16000000,
        polarity=0,
        phase=0,
        rotation=0,
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

