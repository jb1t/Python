import RPi.GPIO as GPIO
import time


gpio_start = 2
gpio_end = 5
GPIO.setmode(GPIO.BCM)

for x in range(gpio_start, gpio_end):
    GPIO.setup(x, GPIO.OUT)

try:

  while True:

    for y in range(gpio_start, gpio_end):
        GPIO.output(y, True)
        print("{0} pin is on".format(y))
        time.sleep(0.5)

    for z in range(gpio_start, gpio_end):
        GPIO.output(z, False)
        print("{0} pin is off".format(z))
        time.sleep(0.5)

except KeyboardInterrupt:

  print("Quit")
  GPIO.cleanup()


