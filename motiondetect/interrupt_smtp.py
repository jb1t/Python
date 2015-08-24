import RPi.GPIO as GPIO
import time
import datetime
import smtplib
import getpass


start_time = time.time()

GPIO.setmode(GPIO.BOARD)
PIR_PIN = 13
GPIO.setup(PIR_PIN, GPIO.IN)


def send_text():
    global password
    from_address = 'jeff.l.garrison@gmail.com'
    toaddrs = '5033510304@txt.att.net'
    msg = "\r\n".join([
        "From: jeff.l.garrison@gmail.com",
        "To: 5033510304@txt.att.net",
        "Subject: Motion Detected",
        "",
        "http://www.ustream.tv/channel/rpi-cam"
    ])
    username = 'jeff.l.garrison@gmail.com'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(from_address, toaddrs, msg)
    server.quit()


def motion_detected(pin):
    global start_time
    if GPIO.input(pin):
        print "Motion Detected @ " + str(datetime.datetime.now())
        elapsed_time = time.time() - start_time
        if elapsed_time > 180:
            print "Elapsed Time: " + str(elapsed_time)
            send_text()
    else:
        print "Motion Stopped @ " + str(datetime.datetime.now())
    
    start_time = time.time()


password = getpass.getpass()
send_text()
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
