# SPDX-FileCopyrightText: 2017 Radomir Dopieralski for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.st7735`
====================================================

A simple driver for the ST7735-based displays.

* Author(s): Radomir Dopieralski, Michael McWethy
"""

from adafruit_rgb_display.rgb import translate_circuitpython
from rgb_display import ST7735 as rgb_ST7735
from rgb_display import ST7735R as rgb_ST7735R
from rgb_display import ST7735S as rgb_ST7735S

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git"


class ST7735(rgb_ST7735):
    """
    A simple driver for the ST7735-based displays.

    >>> import busio
    >>> import digitalio
    >>> import board
    >>> from adafruit_rgb_display import color565
    >>> import adafruit_rgb_display.st7735 as st7735
    >>> spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    >>> display = st7735.ST7735(spi, cs=digitalio.DigitalInOut(board.GPIO0),
    ...    dc=digitalio.DigitalInOut(board.GPIO15), rst=digitalio.DigitalInOut(board.GPIO16))
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
        width=128,
        height=128,
        baudrate=16000000,
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


class ST7735R(rgb_ST7735R):
    """A simple driver for the ST7735R-based displays."""
    # pylint: disable-msg=useless-super-delegation, too-many-arguments
    def __init__(
        self,
        port,
        dc,
        rst=None,
        width=128,
        height=160,
        *,
        x_offset=0,
        y_offset=0,
        rotation=0,
        bgr=False
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
                rotation=rotation,
                bgr=bgr)


class ST7735S(rgb_ST7735S):
    """A simple driver for the ST7735S-based displays."""

    # pylint: disable-msg=useless-super-delegation, too-many-arguments
    def __init__(
        self,
        port,
        dc,
        bl,
        rst=None,
        width=128,
        height=160,
        *,
        x_offset=2,
        y_offset=1,
        rotation=0
    ):
        (spi_device, dc_pin, rst_pin) = translate_circuitpython(
            spi, dc, cs, rst, baudrate, polarity, phase
        )
        bl.on = lambda s: s.value = 1
        bl.off = lambda s: s.value = 0

        super().__init__(
                spi_device,
                dc_pin,
                rst_pin,
                width,
                height,
                x_offset=x_offset,
                y_offset=y_offset,
                rotation=rotation,
                bl=bl)
