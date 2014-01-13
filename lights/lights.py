#!/usr/bin/env python
import signal
import sys
import bottle
from bottle import error
import lightsDAO
from lightPins import LightPins
from logger import MongoLogger
import time

listen_addr = '192.168.1.6'
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


@bottle.route('/blink')
@bottle.route('/blink/<count:int>')
def blink(count):
    logger.write('blink')
    if count > 0:
        loop_counter = count
    else: 
	loop_counter = 5
    for i in range(loop_counter):
        lights.turn_all_on()
        time.sleep(0.5)
        lights.turn_all_off()
	time.sleep(0.5)
    return bottle.template('lights.tpl')


@bottle.route('/red')
def red():
    logger.write('red')
    lights.turn_on(LightPins.Pins['RED'])
    return bottle.template('lights.tpl')


@bottle.route('/yellow')
def yellow():
    logger.write('yellow')
    lights.turn_on(LightPins.Pins['YELLOW'])
    return bottle.template('lights.tpl')


@bottle.route('/green')
def green():
    logger.write('green')
    lights.turn_on(LightPins.Pins['GREEN'])
    return bottle.template('lights.tpl')


@bottle.route('/off')
def lights_off():
    logger.write('off')
    lights.turn_all_off()
    return bottle.template('lights.tpl')


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
