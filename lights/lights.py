#!/usr/bin/env python
import signal
import sys
import RPi.GPIO as GPIO
import bottle
from bottle import error

greenPin = 7
yellowPin = 11
redPin = 12
listen_addr = '192.168.1.8'
listen_port = '8088'

def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
	GPIO.cleanup()
        sys.exit(0)

def clearPins():
    GPIO.output(greenPin, GPIO.LOW)
    GPIO.output(yellowPin, GPIO.LOW)
    GPIO.output(redPin, GPIO.LOW)

def setupGPIO():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(greenPin, GPIO.OUT)
    GPIO.setup(yellowPin, GPIO.OUT)
    GPIO.setup(redPin, GPIO.OUT)
    clearPins()

def lightPin(status):
    if status == 'Failure':
        GPIO.output(redPin, GPIO.HIGH)
    elif status == 'Success':
        GPIO.output(greenPin, GPIO.HIGH)
    else:
        GPIO.output(yellowPin, GPIO.HIGH)

@bottle.route('/')
def index():
	html = '<html><body><ul>'
	html = html + '<li><a href="/red">red</a></li>'
	html = html + '<li><a href="/yellow">yellow</a></li>'
	html = html + '<li><a href="/green">green</a></li>'
	html = html + '<li><a href="/off">off</a></li>'
        html = html + '</ul></body></html>'
	return html

@bottle.route('/red')
def red():
	lightPin('Failure')
	print 'red'

@bottle.route('/yellow')
def yellow():
	lightPin('Investigate')
	print 'yellow'

@bottle.route('/green')
def green():
	lightPin('Success')
	print 'green'

@bottle.route('/off')
def lightsOff():
	print 'off'
	clearPins()

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

def main():
	setupGPIO()
	
	signal.signal(signal.SIGINT, signal_handler)
	print 'Press Ctrl+C'

	print 'starting web server on ' + listen_addr + ':' + listen_port
	bottle.debug(True)
	bottle.run(host=listen_addr, port=listen_port)
	signal.pause()


if __name__ == "__main__":
	try:
		main()
	except Exception as ex:
		GPIO.cleanup()
		print ex
		sys.exit(0)
