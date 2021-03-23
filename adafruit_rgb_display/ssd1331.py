# SPDX-FileCopyrightText: 2017 Radomir Dopieralski for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.ssd1331`
====================================================

A simple driver for the SSD1331-based displays.

* Author(s): Radomir Dopieralski, Michael McWethy
"""

from adafruit_rgb_display.rgb import translate_circuitpython
from rgb_display import SDD1331 as rgb_SDD1331

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display.git"


class SSD1331(rgb_SDD1331):
    """
    A simple driver for the SSD1331-based displays.

    .. code-block:: python

      import busio
      import digitalio
      import board
      from adafruit_rgb_display import color565
      import adafruit_rgb_display.ssd1331 as ssd1331
      spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
      display = ssd1331.SSD1331(spi, cs=digitalio.DigitalInOut(board.GPIO0),
                                  dc=digitalio.DigitalInOut(board.GPIO15),
                                  rst=digitalio.DigitalInOut(board.GPIO16))

      display.fill(0x7521)
      display.pixel(32, 32, 0)

    """

    # pylint: disable-msg=useless-super-delegation, too-many-arguments
    # super required to allow override of default values
    def __init__(
        self,
        spi,
        dc,
        cs,
        rst=None,
        width=96,
        height=64,
        baudrate=16000000,
        polarity=0,
        phase=0,
        *,
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

