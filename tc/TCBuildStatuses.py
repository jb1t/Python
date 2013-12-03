import requests
import xmltodict
import sys
import RPi.GPIO as GPIO
import time
from datetime import datetime

tc_url = "http://servernamegoeshere:90/httpAuth/app/rest/cctray/projects.xml"

greenPin = 7
yellowPin = 11
redPin = 12

def clearPins():
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.LOW)

def setupGPIO():
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

def getTCProjectsXML():
	response = requests.get(tc_url, timeout=10.000, auth=('username', 'password'))
	doc = xmltodict.parse(response.text)
	return doc['Projects']['Project']

def displayTime():
	now = datetime.now()
	today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
	today5pm = now.replace(hour=23, minute=59, second=59, microsecond=0)

	isDisplayTime = now > today8am and now < today5pm
	print 'now=', now, 'today8am=', today8am, 'today5pm', today5pm, isDisplayTime

	return isDisplayTime

def main():
	isDisplayTime = False

	setupGPIO()

	while 1:
		oldIsDisplayTime = isDisplayTime
		isDisplayTime = displayTime()
		if isDisplayTime <> oldIsDisplayTime:
			if isDisplayTime:
				setupGPIO()
			else:
				clearPins()
				GPIO.cleanup()
		
		if isDisplayTime:
			try:
				projects = getTCProjectsXML()	
				overallStatus = "Success"
	
				for project in projects:
    					projectName = project['@name']
	    				buildStatus = project['@lastBuildStatus']
					activity = project['@activity']

    					if buildStatus != 'Success' and buildStatus != 'Unknown' and activity != 'Paused' and projectName.count(":: Deploy") == 0:
	        				print(projectName, buildStatus)
	        				overallStatus = buildStatus 
			        		#break

				print overallStatus, datetime.now()
				clearPins()
				lightPin(overallStatus)
			except KeyboardInterrupt:
				GPIO.cleanup()
			except:
				print "Unhandled error occurred: ", sys.exc_info()[0]
		
		time.sleep(2)



if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		GPIO.cleanup()
