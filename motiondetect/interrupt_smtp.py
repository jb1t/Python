import smtplib
import getpass
import requests
import datetime
import time
from AppConfig import AppConfig
try:
    import RPi.GPIO as GPIO
except ImportError:
    from rpidevmocks import MockGPIO
    GPIO = MockGPIO()


def send_text():
    global password, appSettings

    from_address = appSettings.EmailSettings.fromEmail
    toaddrs = appSettings.EmailSettings.toAddress
    msg = "\r\n".join([
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
    try:
        r = requests.get('https://maker.ifttt.com/trigger/motion_detected/with/key/{0}'.format(appSettings.IFTTT.key))
        print 'Response: ' + r.text
    except:
        print("Unexpected error calling IFTTT: ", sys.exc_info()[0])
        raise


if __name__ == '__main__':
    try:

        # Get Configuration
        appSettings = AppConfig()
        appSettings.get_configuration()

        # Initialize variables
        last_status_time = datetime.datetime.now() - datetime.timedelta(seconds=appSettings.Settings.elapsedTimeSeconds)
        GPIO.setmode(GPIO.BOARD)
        PIR_PIN = appSettings.Settings.pirPin
        GPIO.setup(PIR_PIN, GPIO.IN)

        # Get user password for email account
        password = getpass.getpass()

        # Send notifications to verify everything is working
        send_text()
        send_ifttt()
        print "PIR Module Test (CTRL+C to exit)"
        time.sleep(2)
        print "Ready"

        # Start listening for events
        GPIO.add_event_detect(PIR_PIN, GPIO.RISING)

        while True:

            current_status_time = datetime.datetime.now()

            if GPIO.event_detected(PIR_PIN):
                elapsed_time = current_status_time - last_status_time

                print("{0} - Event detected on pin {1} - last event fired {2}".format(current_status_time, PIR_PIN, elapsed_time))

                last_status_time = datetime.datetime.now()
                if elapsed_time.total_seconds() > appSettings.Settings.elapsedTimeSeconds:
                    send_ifttt()
                    send_text()
            
            #print("sleeping... elapsed time seconds: {0}".format((current_status_time-last_status_time).total_seconds()))
            time.sleep(appSettings.Settings.mainThreadSleepSeconds)

    except KeyboardInterrupt:
        print "Quit"
        GPIO.cleanup()
