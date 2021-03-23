# SPDX-FileCopyrightText: 2019 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.hx8357`
====================================================

A simple driver for the HX8357-based displays.

* Author(s): Melissa LeBlanc-Williams
"""
from adafruit_rgb_display.rgb import translate_circuitpython
from rgb_display import HX8357 as rgb_HX8357

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git"


class HX8357(rgb_HX8357):
    """
    A simple driver for the HX8357-based displays.

    >>> import busio
    >>> import digitalio
    >>> import board
    >>> from adafruit_rgb_display import color565
    >>> import adafruit_rgb_display.hx8357 as hx8357
    >>> spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    >>> display = hx8357.HX8357(spi, cs=digitalio.DigitalInOut(board.GPIO0),
    ...    dc=digitalio.DigitalInOut(board.GPIO15))
    >>> display.fill(0x7521)
    >>> display.pixel(64, 64, 0)
    """

    # pylint: disable-msg=useless-super-delegation, too-many-arguments
    def __init__(
        self,
        spi,
        dc,
        cs,
        rst=None,
        width=480,
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
