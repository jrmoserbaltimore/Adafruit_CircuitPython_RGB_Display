# SPDX-FileCopyrightText: 2017 Radomir Dopieralski for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_rgb_display.hx8353`
====================================================

A simple driver for the HX8353-based displays.

* Author(s): Radomir Dopieralski, Michael McWethy
"""
try:
    from micropython import const
except ImportError:
    def const(n): return n
from rgb_display.rgb import DisplayDevice

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/jrmoser/RGB_Display.git"

_SWRESET = const(0x01)
_NORON = const(0x13)
_INVOFF = const(0x20)
_INVON = const(0x21)
_DISPOFF = const(0x28)
_DISPON = const(0x29)
_CASET = const(0x2A)
_PASET = const(0x2B)
_RAMWR = const(0x2C)
_RAMRD = const(0x2E)
_MADCTL = const(0x36)
_COLMOD = const(0x3A)


class HX8353(DisplayDevice):
    """
    A simple driver for the HX8353-based displays.
    """

    _COLUMN_SET = _CASET
    _PAGE_SET = _PASET
    _RAM_WRITE = _RAMWR
    _RAM_READ = _RAMRD
    _INIT = (
        (_SWRESET, None),
        (_DISPON, None),
    )
    _ENCODE_PIXEL = ">H"
    _ENCODE_POS = ">HH"

    # pylint: disable-msg=useless-super-delegation, too-many-arguments
    def __init__(
        self,
        port,
        dc,
        rst=None,
        width=128,
        height=128,
        x_offset=0,
        y_offset=0,
        rotation=0
    ):
        super().__init__(
            port,
            dc,
            rst,
            width,
            height,
            x_offset=x_offset,
            y_offset=y_offset,
            rotation=rotation,
        )
