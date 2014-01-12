import RPi.GPIO as GPIO
import lightPins

__author__ = 'jeffgarrison'

class LightsDAO:

    # constructor for the class
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
	for key, value in lightPins.LightPins.Pins.items():
  		if not key.startswith("_"):
            		GPIO.setup(value, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        GPIO.cleanup()

    def turn_on(self, lightPin):
        GPIO.output(lightPin, GPIO.HIGH)

    def turn_off(self, lightPin):
        GPIO.output(lightPin, GPIO.LOW)

    def turn_all_off(self):
	for key, value in lightPins.LightPins.Pins.items():
  		if not key.startswith("_"):
			GPIO.output(value, GPIO.LOW)

    def turn_all_on(self):
	for key, value in lightPins.LightPins.Pins.items():
  		if not key.startswith("_"):
			GPIO.output(value, GPIO.HIGH)

    def print_all(self):
	for key, value in lightPins.LightPins.Pins.items():
  		if not key.startswith("_"):
			print key, value	
