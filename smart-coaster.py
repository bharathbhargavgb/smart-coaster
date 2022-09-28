#! /usr/bin/python3

import time
import sys

import RPi.GPIO as GPIO
from hx711 import HX711


PRECALIBRATED_REFERENCE_UNIT = -6.6


def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    sys.exit()


hx = HX711(23, 24)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(PRECALIBRATED_REFERENCE_UNIT)
hx.reset()
hx.tare()
print("Tare done! Add weight now...")

while True:
    try:
        val = hx.get_weight(5)
        print(val)

        hx.power_down()
        hx.power_up()
        time.sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()
