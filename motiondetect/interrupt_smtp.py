import RPi.GPIO as GPIO
import time
import datetime
import smtplib
import getpass
import requests
from AppConfig import AppConfig


appSettings = AppConfig()
appSettings.get_configuration()

start_time = time.time()
GPIO.setmode(GPIO.BOARD)
PIR_PIN = appSettings.Settings.pirPin
GPIO.setup(PIR_PIN, GPIO.IN)
last_status = 'start_motion'


def send_text():
    global password, appSettings
    from_address = appSettings.EmailSettings.fromEmail
    toaddrs = appSettings.EmailSettings.toAddress
    msg = "\r\n".join([
        "From: homeautomation.garrison@gmail.com",
        "To: {0}".format(appSettings.EmailSettings.toAddress),
        "Subject: Motion Detected",
        "",
        "http://www.ustream.tv/channel/rpi-cam"
    ])
    username = appSettings.EmailSettings.userName
    server = smtplib.SMTP(appSettings.EmailSettings.smtpServer)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, toaddrs, msg)
    server.quit()


def send_ifttt():
    global appSettings
    print 'Making request to IFTTT'
    r = requests.get('https://maker.ifttt.com/trigger/motion_detected/with/key/{0}'.format(appSettings.IFTTT.key))
    print 'Response: ' + r.text


def motion_detected(pin):
    global start_time, last_status, appSettings

    if GPIO.input(pin):
        print "Motion Detected @ " + str(datetime.datetime.now())
        elapsed_time = time.time() - start_time
        if elapsed_time > appSettings.Settings.elapsedTime:
            print "Elapsed Time: " + str(elapsed_time)
            send_text()
            send_ifttt()
        last_status = 'start_motion'
    else:
        if last_status != 'stop_motion':
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
        time.sleep(appSettings.Settings.mainThreadSleep)

except KeyboardInterrupt:
    print "Quit"
    GPIO.cleanup()
