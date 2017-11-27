try:
    import RPi.GPIO as GPIO
except ImportError:
    from rpidevmocks import MockGPIO
    GPIO = MockGPIO()


class LightProvider:
    @staticmethod
    def GREEN_PIN():
        return 7

    @staticmethod
    def YELLOW_PIN():
        return 11

    @staticmethod
    def RED_PIN():
        return 12

    def __init__(self, GPIO):
        self.GPIO = GPIO

    def clearPins(self):
        print 'set all lights off'
        self.GPIO.output(LightProvider.GREEN_PIN(), self.GPIO.LOW)
        self.GPIO.output(LightProvider.YELLOW_PIN(), self.GPIO.LOW)
        self.GPIO.output(LightProvider.RED_PIN(), self.GPIO.LOW)

    def setupGPIO(self):
        print 'setup the GPIO'
        self.GPIO.setmode(self.GPIO.BOARD)
        self.GPIO.setup(LightProvider.GREEN_PIN(), self.GPIO.OUT)
        self.GPIO.setup(LightProvider.YELLOW_PIN(), self.GPIO.OUT)
        self.GPIO.setup(LightProvider.RED_PIN(), self.GPIO.OUT)
        self.clearPins()

    def cleanup(self):
        print 'cleanup the GPIO'
        self.GPIO.cleanup()

    def lightPin(self, pin):
        print 'turn on pin', pin
        self.GPIO.output(pin, self.GPIO.HIGH)
