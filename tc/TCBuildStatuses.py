import requests
import xmltodict
import sys
import RPi.GPIO as GPIO
import time

tc_url = "http://pc21568:90/httpAuth/app/rest/cctray/projects.xml"

greenPin = 7
yellowPin = 11
redPin = 12
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(yellowPin, GPIO.OUT)
GPIO.setup(redPin, GPIO.OUT)

def clearPins():
	GPIO.output(greenPin, GPIO.LOW)
	GPIO.output(yellowPin, GPIO.LOW)
	GPIO.output(redPin, GPIO.LOW)

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

def main():

	while 1:
		try:
			projects = getTCProjectsXML()	
			overallStatus = "Success"

			for project in projects:
    				projectName = project['@name']
	    			buildStatus = project['@lastBuildStatus']
    				if buildStatus != 'Success' and buildStatus != 'Unknown' and projectName.count(":: Deploy") == 0:
	        			#print(projectName, buildStatus)
        				overallStatus = buildStatus 
		        		#break

			print(overallStatus)
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
