import RPi.GPIO as GPIO
import time
import datetime

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 13 
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
  if(GPIO.input(PIR_PIN)):
    print "Motion Detected @ " + str(datetime.datetime.now())
  else:
    print "Motion Stopped @ " + str(datetime.datetime.now())

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
  
  GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
  while 1:
    time.sleep(100)

except KeyboardInterrupt:
  print "Quit"
  GPIO.cleanup()
