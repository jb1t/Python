#!/usr/bin/env python
import signal
import sys
import bottle
from bottle import error
import lightsDAO
from lightPins import LightPins 
#import pymongo
import datetime

listen_addr = '192.168.1.17'
listen_port = '8088'
lights = lightsDAO.LightsDAO()

def signal_handler(signal, frame):
    lights = None
    print 'You pressed Ctrl+C!'
    sys.exit(0)

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
    lights.turn_on(LightPins.Pins['RED'])
    print 'red'

@bottle.route('/yellow')
def yellow():
    lights.turn_on(LightPins.Pins['YELLOW'])
    print 'yellow'

@bottle.route('/green')
def green():
    lights.turn_on(LightPins.Pins['GREEN'])
    print 'green'

@bottle.route('/off')
def lightsOff():
    lights.turn_all_off()
    print 'off'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'

def main():
#    connection_string = "mongodb://localhost"
#    connection = pymongo.MongoClient(connection_string)
#    log = connection.log

#    log.insert({'message': 'Starting up', 'created_date_utc': datetime.utcnow()})

    lights.print_all()

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
