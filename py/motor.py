#!/usr/bin/python
import sys
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(io.BOARD)

pin_a = 7
pin_b = 8

GPIO.setup(pin_a, GPIO.OUT)
GPIO.setup(pin_b, GPIO.OUT)

GPIO.output(pin_a, GPIO.HIGH)
sleep(1)
GPIO.output(pin_a, GPIO.LOW)
sleep(1)

GPIO.cleanup();