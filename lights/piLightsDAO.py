import RPi.GPIO as GPIO
import lightPins
import time

__author__ = 'jeffgarrison'


class PiLightsDAO:
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

    @staticmethod
    def turn_on(light_pin):
        GPIO.output(light_pin, GPIO.HIGH)

    @staticmethod
    def turn_off(light_pin):
        GPIO.output(light_pin, GPIO.LOW)

    def cycle_all_lights(self, off_duration, on_duration, repeat_count=None):
        if repeat_count is None:
            repeat_count = 1
        for count in range(repeat_count):
            self.cycle_lights(off_duration, on_duration)

    @staticmethod
    def cycle_lights(off_duration, on_duration):
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                GPIO.output(value, GPIO.HIGH)
                time.sleep(on_duration)
                GPIO.output(value, GPIO.LOW)
                time.sleep(off_duration)

    def blink_all_lights(self, repeat_count, off_duration, on_duration):
        for count in range(repeat_count):
            self.turn_all_on()
            time.sleep(on_duration)
            self.turn_all_off()
            time.sleep(off_duration)

    def morse_code(self, encoded_text):
        for character in encoded_text:
            if character == '.':
                self.turn_all_on()
                time.sleep(0.5)
                self.turn_all_off()
            elif character == '-':
                self.turn_all_on()
                time.sleep(1.5)
                self.turn_all_off()
            elif character == ' ':
                time.sleep(0.5)

    @staticmethod
    def turn_all_off():
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                GPIO.output(value, GPIO.LOW)

    @staticmethod
    def turn_all_on():
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                GPIO.output(value, GPIO.HIGH)

    @staticmethod
    def print_all():
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                print key, value
