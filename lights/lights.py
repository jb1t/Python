#!/usr/bin/env python
import signal
import sys
import bottle
from bottle import error, static_file, request
import piLightsDAO
#import consoleLightsDAO
from lightPins import LightPins
from logger import MongoLogger
import morseCode


#listen_addr = '192.168.1.100'
listen_addr = '0.0.0.0'
listen_port = '8088'
lights = piLightsDAO.PiLightsDAO()
#lights = consoleLightsDAO.ConsoleLightsDAO()
logger = MongoLogger("localhost", 27017)


def signal_handler(signal, frame):
    lights = None
    print 'You pressed Ctrl+C!'
    sys.exit(0)

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root="./")

@bottle.route('/')
def index():
    logger.write('index()', bottle.request)
    return bottle.template('lights.tpl')


@bottle.route('/cycle')
@bottle.route('/cycle/<count:int>/<on_duration:float>/<off_duration:float>')
def cycle(count, on_duration, off_duration):
    logger.write('cycle', bottle.request)
    lights.cycle_all_lights(off_duration, on_duration, count)
    return


@bottle.route('/blink')
@bottle.route('/blink/<count:int>/<on_duration:float>/<off_duration:float>')
def blink(count, on_duration, off_duration):
    logger.write('blink', bottle.request)
    lights.blink_all_lights(count, off_duration, on_duration)
    return


@bottle.route('/red')
def red():
    logger.write('red', bottle.request)
    lights.turn_on(LightPins.Pins['RED'])
    return


@bottle.route('/yellow')
def yellow():
    logger.write('yellow', bottle.request)
    lights.turn_on(LightPins.Pins['YELLOW'])
    return


@bottle.route('/green')
def green():
    logger.write('green', bottle.request)
    lights.turn_on(LightPins.Pins['GREEN'])
    return


@bottle.route('/off')
def lights_off():
    logger.write('off', bottle.request)
    lights.turn_all_off()
    return

@bottle.route('/mc')
def morse_code():
    return bottle.template('morse_code.tpl', message='', encoded_message='')

@bottle.route('/mc', method='POST')
def morse_code():
    message = request.forms.get('message')
    morse_code_instance = morseCode.MorseCode()
    encoded_message = morse_code_instance.encode(message)
    lights.morse_code(encoded_message)
    return bottle.template('morse_code.tpl', message=message, encoded_message=encoded_message)


@error(404)
def mistake404(code):
    logger.write('404 ', bottle.request)
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
