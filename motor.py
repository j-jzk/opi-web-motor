#!/usr/bin/python3
import OPi.GPIO as GPIO
from time import sleep

#piny podle civek
c11 = 37
c12 = 35
c21 = 33
c22 = 31

#funkce pro pohyb (jeden cyklus)
def fw(delay):
    GPIO.output(c11, 0)
    GPIO.output(c12, 1)
    sleep(delay)
    GPIO.output(c12, 0)

    GPIO.output(c21, 0)
    GPIO.output(c22, 1)
    sleep(delay)
    GPIO.output(c22, 0)

    GPIO.output(c11, 1)
    GPIO.output(c12, 0)
    sleep(delay)
    GPIO.output(c11, 0)

    GPIO.output(c21, 1)
    GPIO.output(c22, 0)
    sleep(delay)
    GPIO.output(c21, 0)

def bw(delay):
    GPIO.output(c21, 1)
    GPIO.output(c22, 0)
    sleep(delay)
    GPIO.output(c21, 0)

    GPIO.output(c11, 1)
    GPIO.output(c12, 0)
    sleep(delay)
    GPIO.output(c11, 0)

    GPIO.output(c21, 0)
    GPIO.output(c22, 1)
    sleep(delay)
    GPIO.output(c22, 0)

    GPIO.output(c11, 0)
    GPIO.output(c12, 1)
    sleep(delay)
    GPIO.output(c12, 0)

def setup():
    GPIO.setboard(GPIO.PCPCPLUS)
    GPIO.setmode(GPIO.BOARD)

    for pin in [c11, c12, c21, c22]:
        GPIO.setup(pin, GPIO.OUT)

def cleanup():
    for pin in [c11, c12, c21, c22]:
        GPIO.output(pin, 0)
    GPIO.cleanup()
