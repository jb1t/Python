import lightPins
import time

__author__ = 'jeffgarrison'


class ConsoleLightsDAO:
    # constructor for the class
    def __init__(self):
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                print 'Setup pin ' + key

    def __del__(self):
        print 'GPIO.cleanup()'

    def __enter__(self):
        print '__enter__'
        return self

    def __exit__(self, type, value, traceback):
        print 'GPIO.cleanup()'

    @staticmethod
    def turn_on(light_pin):
        print 'GPIO.output(' + str(light_pin) + ', GPIO.HIGH)'

    @staticmethod
    def turn_off(light_pin):
        print 'GPIO.output(' + str(light_pin) + ', GPIO.LOW)'

    def cycle_all_lights(self, off_duration, on_duration, repeat_count=None):
        if repeat_count is None:
            repeat_count = 1
        for count in range(repeat_count):
            self.cycle_lights(off_duration, on_duration)

    @staticmethod
    def cycle_lights(off_duration, on_duration):
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                print 'GPIO.output(' + str(value) + ', GPIO.HIGH)'
                time.sleep(on_duration)
                print 'GPIO.output(' + str(value) + ', GPIO.LOW)'
                time.sleep(off_duration)

    def blink_all_lights(self, repeat_count, off_duration, on_duration):
        for count in range(repeat_count):
            print 'self.turn_all_on()'
            time.sleep(on_duration)
            print 'self.turn_all_off()'
            time.sleep(off_duration)

    @staticmethod
    def turn_all_off():
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                print 'GPIO.output(' + str(value) + ', GPIO.LOW)'

    @staticmethod
    def turn_all_on():
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                print 'GPIO.output(' + str(value) + ', GPIO.HIGH)'

    @staticmethod
    def print_all():
        for key, value in lightPins.LightPins.Pins.items():
            if not key.startswith("_"):
                print key, value
