#!/usr/bin/env python

import logging
import logging.handlers
import argparse
import signal
import sys
import time  # this is only being used as part of the example
import RPi.GPIO as GPIO


class CancellationToken:
  cancel_now = False
  def __init__(self):
    signal.signal(signal.SIGINT, self.exit_gracefully)
    signal.signal(signal.SIGTERM, self.exit_gracefully)

  def exit_gracefully(self,signum, frame):
    self.cancel_now = True

# Deafults
LOG_FILENAME = "/tmp/lightservice.log"
LOG_LEVEL = logging.INFO  # Could be e.g. "DEBUG" or "WARNING"

# Define and parse command line arguments
parser = argparse.ArgumentParser(description="My simple build lights Python service")
parser.add_argument("-l", "--log", help="file to write log to (default '" + LOG_FILENAME + "')")

# If the log file is specified on the command line then override the default
args = parser.parse_args()
if args.log:
	LOG_FILENAME = args.log

# Configure logging to log to a file, making a new file at midnight and keeping the last 3 day's data
# Give the logger a unique name (good practice)
logger = logging.getLogger(__name__)
# Set the log level to LOG_LEVEL
logger.setLevel(LOG_LEVEL)
# Make a handler that writes to a file, making a new file at midnight and keeping 3 backups
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILENAME, when="midnight", backupCount=3)
# Format each log message like this
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
# Attach the formatter to the handler
handler.setFormatter(formatter)
# Attach the handler to the logger
logger.addHandler(handler)

# Make a class we can use to capture stdout and sterr in the log
class MyLogger(object):
	def __init__(self, logger, level):
		"""Needs a logger and a logger level."""
		self.logger = logger
		self.level = level

	def write(self, message):
		# Only log if there is a message (not just a new line)
		if message.rstrip() != "":
			self.logger.log(self.level, message.rstrip())

# Replace stdout with logging to file at INFO level
sys.stdout = MyLogger(logger, logging.INFO)
# Replace stderr with logging to file at ERROR level
sys.stderr = MyLogger(logger, logging.ERROR)

i = 0
gpio_start = 2
gpio_end = 5
GPIO.setmode(GPIO.BCM)

for x in range(gpio_start, gpio_end):
    GPIO.setup(x, GPIO.OUT)

request = CancellationToken()
# Loop forever, doing something useful hopefully:
while not request.cancel_now:
	logger.info("The counter is now " + str(i))
	print "This is a test print"
	i += 1

	try:

    	  for y in range(gpio_start, gpio_end):
       	    GPIO.output(y, True)
       	    print("{0} pin is on".format(y))
       	    time.sleep(0.5)

    	  for z in range(gpio_start, gpio_end):
            GPIO.output(z, False)
            print("{0} pin is off".format(z))
            time.sleep(0.5)

	except KeyboardInterrupt:

  	  print("Keyboard Interrupt Quitting...")
  	  GPIO.cleanup()

print("End of the program. Killed gracefully.")
GPIO.cleanup()
