# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Quick test of TFT FeatherWing (ST7789) with Feather M0 or M4
# This will work even on a device running displayio
# Will fill the TFT black and put a red pixel in the center, wait 2 seconds,
# then fill the screen blue (with no pixel), wait 2 seconds, and repeat.
#
# This example includes MicroPython, CircuitPython, and Raspberry Pi
# setup, based on implementation name or a variable
import time
import sys
import random
if sys.implementation.name == "micropython":
    import machine
elif __circuitpython__: #
    import digitalio
    import board
else: # Raspberry Pi
    # Use gpizero
    import gpiozero
    import spidev

from rgb_display.rgb import color565
import rgb_display.st7789 as st7789

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 24000000

# Setup SPI bus using hardware SPI.
# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4)
if sys.implementation.name == "micropython":
    spi = machine.SPI(0)
    sck = machine.Pin(18)
    smosi = machine.Pin(19)
    smiso = machine.Pin(20)
    cs_pin = machine.Pin(21)
    spi.init(baudrate=BAUDRATE, sck=sck, mosi=smosi, miso=smiso)
    dc_pin = machine.Pin(2)
    reset_pin = machine.Pin(9)
    # enable the SPI device.  In client code, when you have a single
    # device, you'll want to hardwire CS; when you have multiple
    # devices, you'll want to enable CS before writing to the display
    # and disable it when switching to another device.
    cs_pin.on()
elif __circuitpython__:
    # TODO:  somehow actually set up to use CircuitPython
    cs_pin = digitalio.DigitalInOut(board.D5)
    dc_pin = digitalio.DigitalInOut(board.D6)
    reset_pin = digitalio.DigitalInOut(board.D9)
    # Make API compatible with gpiozero and MicroPython machine.Pin
    for x in [dc_pin, reset_pin]:
        x.switch_to_output(value=0)
        x.on = lambda s: s.value = 1
        x.off = lambda s: s.value = 0
    # Hardware SPI
    spi = spi_device.SPIDevice(
        board.SPI(), cs_pin, baudrate=BAUDRATE, polarity=0, phase=0
    )
    spi.send = spi.write
else:
    cs_pin = gpiozero.OutputDevice(5)
    dc_pin = gpiozero.OutputDevice(6)
    reset_pin = gpiozero.OutputDevice(9)
    # Setup SPI bus using hardware SPI:
    spi = spidev.SpiDev(0, ST7735.BG_SPI_CS_FRONT)
    spi.mode = 0
    spi.lsbfirst = False
    spi.max_speed_hz = BAUDRATE
    # API compatibility
    spi.send = spi.xfer3
    cs_pin.on()

# Create the ST7789 display:
display = st7789.ST7789(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin)

# Main loop:
while True:
    # Fill the screen red, green, blue, then black:
    for color in ((255, 0, 0), (0, 255, 0), (0, 0, 255)):
        display.fill(color565(color))
    # Clear the display
    display.fill(0)
    # Draw a red pixel in the center.
    display.pixel(display.width // 2, display.height // 2, color565(255, 0, 0))
    # Pause 2 seconds.
    time.sleep(2)
    # Clear the screen a random color
    display.fill(
        color565(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    )
    # Pause 2 seconds.
    time.sleep(2)
