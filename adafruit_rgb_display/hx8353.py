# SPDX-FileCopyrightText: 2017 Radomir Dopieralski for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.hx8353`
====================================================

A simple driver for the HX8353-based displays.

* Author(s): Radomir Dopieralski, Michael McWethy
"""
from adafruit_rgb_display.rgb import translate_circuitpython
from rgb_display import HX8353 as rgb_HX8353

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git"


class HX8353(rgb_HX8353):
    """
    A simple driver for the HX8353-based displays.

    >>> import busio
    >>> import digitalio
    >>> import board
    >>> from adafruit_rgb_display import color565
    >>> import adafruit_rgb_display.hx8353 as hx8353
    >>> spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
    >>> display = hx8353.HX8383(spi, cs=digitalio.DigitalInOut(board.GPIO0),
    ...    dc=digitalio.DigitalInOut(board.GPIO15))
    >>> display.fill(0x7521)
    >>> display.pixel(64, 64, 0)
    """

    # pylint: disable-msg=useless-super-delegation, too-many-arguments
    def __init__(self, spi, dc, cs, rst=None, width=128, height=128, rotation=0):
        
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
