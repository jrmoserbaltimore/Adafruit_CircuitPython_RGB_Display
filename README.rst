Introduction
============

.. image:: https://readthedocs.org/projects/adafruit-circuitpython-rgb_display/badge/?version=latest
    :target: https://circuitpython.readthedocs.io/projects/rgb_display/en/latest/
    :alt: Documentation Status

.. image :: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display/actions/
    :alt: Build Status

Generalization of display drivers from https://github.com/adafruit/adafruit-circuitpython-rgb-display to remove platform dependencies.

This driver currently supports displays that use the following display-driver chips: HX8353, HX8357, ILI9341, S6D02A1, ST7789, SSD1331, SSD1351, and ST7735 (including variants ST7735R and ST7735S).

Dependencies
=============
This driver has no particular dependencies.  It accepts pins and SPI devices compatible with MicroPython `machine.Pin` and `machine.SPI`, including `gpiozero.OutputDevice` pins.  Objects can be adapted to fit, for example with `spidev` the SPI object can be given `spi.send = spi.xfer3`, or `digitalio` pins can have `pin.on = lambda s: s.value = 1` to create a `pin.on()` member.

For improved performance consider installing NumPy.

Installing from PyPI
====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-rgb-display/>`_. To install for current user:

.. code-block:: shell

    pip3 install rgb-display

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install rgb-display

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .env
    source .env/bin/activate
    pip3 install rgb-display

Usage Example
=============

see `examples` for usage examples.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_RGB_Display/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
