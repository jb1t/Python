import RPi.GPIO as GPIO
import time
import datetime
import smtplib
import getpass
import requests

start_time = time.time()

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 13
GPIO.setup(PIR_PIN, GPIO.IN)
last_status = 'start_motion'

def send_text():
    global password
    from_address = 'homeautomation.garrison@gmail.com'
    toaddrs = '5033510304@txt.att.net'
    msg = "\r\n".join([
        "From: homeautomation.garrison@gmail.com",
        "To: 5033510304@txt.att.net",
        "Subject: Motion Detected",
        "",
        "http://www.ustream.tv/channel/rpi-cam"
    ])
    username = 'homeautomation.garrison@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, toaddrs, msg)
    server.quit()

def send_ifttt():
    print 'Making request to IFTTT'
    r = requests.get('https://maker.ifttt.com/trigger/motion_detected/with/key/m-Acy3kB1m8rVL4DVA6rqEbyJ2NUn7HiuQ1fAMXa-u8') 
    print 'Response: ' + r.text

def motion_detected(pin):
    global start_time
    global last_status
    if GPIO.input(pin):
        print "Motion Detected @ " + str(datetime.datetime.now())
        elapsed_time = time.time() - start_time
        if elapsed_time > 180:
            print "Elapsed Time: " + str(elapsed_time)
            send_text()
            send_ifttt()
        last_status = 'start_motion'
    else:
	if(last_status != 'stop_motion'):
	    last_status = 'stop_motion'
            print "Motion Stopped @ " + str(datetime.datetime.now())
            start_time = time.time()

password = getpass.getpass()
send_text()
send_ifttt()
print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:

    GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=motion_detected)
    while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
