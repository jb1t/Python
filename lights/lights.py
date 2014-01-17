#!/usr/bin/env python
import signal
import sys
import bottle
from bottle import error
import lightsDAO
from lightPins import LightPins
from logger import MongoLogger
import time
from bson import json_util
import json

listen_addr = '192.168.1.100'
listen_port = '8088'
lights = lightsDAO.LightsDAO()
logger = MongoLogger("localhost", 27017)

def signal_handler(signal, frame):
    lights = None
    print 'You pressed Ctrl+C!'
    sys.exit(0)


@bottle.route('/')
def index():
    logger.write('index()')
    return bottle.template('lights.tpl')


@bottle.route('/cycle')
@bottle.route('/cycle/<count:int>/<onDuration:float>/<offDuration:float>')
def cycle(count, onDuration, offDuration):
    logger.write('cycle')
    if count > 0:
        loop_counter = count
    else: 
	loop_counter = 5
    for i in range(loop_counter):
	for key, value in LightPins.Pins.items():
            lights.turn_on(LightPins.Pins[key])
	    time.sleep(onDuration)
            lights.turn_off(LightPins.Pins[key])
	    time.sleep(offDuration)
    return 


@bottle.route('/blink')
@bottle.route('/blink/<count:int>/<onDuration:float>/<offDuration:float>')
def blink(count, onDuration, offDuration):
    logger.write('blink')
    if count > 0:
        loop_counter = count
    else: 
	loop_counter = 5
    for i in range(loop_counter):
        lights.turn_all_on()
        time.sleep(onDuration)
        lights.turn_all_off()
	time.sleep(offDuration)
    return 


@bottle.route('/red')
def red():
    logger.write('red')
    lights.turn_on(LightPins.Pins['RED'])
    return 


@bottle.route('/yellow')
def yellow():
    logger.write('yellow')
    lights.turn_on(LightPins.Pins['YELLOW'])
    return 


@bottle.route('/green')
def green():
    brequest = {'url': bottle.request.url, 'ip': bottle.request.remote_addr, 'something': bottle.request.json}
    logger.write(brequest)
    lights.turn_on(LightPins.Pins['GREEN'])
    return 


@bottle.route('/off')
def lights_off():
    logger.write('off')
    lights.turn_all_off()
    return 


@error(404)
def mistake404(code):
    logger.write('404 ' + bottle.request.url)
    return 'Sorry, this page does not exist!'


def main():
    logger.write('startup')

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
        lights = None
        print ex
        sys.exit(0)
