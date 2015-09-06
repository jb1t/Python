import sys
import time
from datetime import datetime
from WEHolidays import WEHolidays
from LightProvider import LightProvider
from TeamCityProvider import TeamCityProvider
from TimeValidator import TimeValidator
import requests
try:
    import RPi.GPIO as GPIO
except ImportError:
    from rpidevmocks import MockGPIO
    GPIO = MockGPIO()


class TCBuildLights:
    def __init__(self, lights, teamCity, timevalidator):
        self.lights = lights
        self.teamCity = teamCity
        self.timevalidator = timevalidator
        self.isDisplayTime = False

    def getStatusToDisplay(self):

        projects = self.teamCity.getTeamCityProjects()
        overallStatus = 'Success'

        for project in projects:
            if (
                project.status != 'Success' and
                project.status != 'Unknown' and
                project.activity != 'Paused' and
                project.name.count(":: Deploy") == 0
            ):
                overallStatus = project.status
                break

        return overallStatus

    def getPinToLightUp(self, status):
        if status == 'Failure':
            return LightProvider.RED_PIN()
        elif status == 'Success':
            return LightProvider.GREEN_PIN()
        else:
            return LightProvider.YELLOW_PIN()

    def main(self):

        oldIsDisplayTime = self.isDisplayTime
        self.isDisplayTime = self.timevalidator.IsDisplayTime()
        if self.isDisplayTime <> oldIsDisplayTime:
            if self.isDisplayTime:
                self.lights.setupGPIO()
            else:
                self.lights.clearPins()
                self.lights.cleanup()

        if self.isDisplayTime:
            try:
                status = self.getStatusToDisplay()
                self.lights.clearPins()
                self.lights.lightPin(self.getPinToLightUp(status))
            except KeyboardInterrupt:
                self.lights.cleanup()
            except:
                print 'Unhandled error occurred: ', sys.exc_info()[0]


if __name__ == '__main__':
    try:

        lights = LightProvider(GPIO)
        tc = TeamCityProvider(requests, 'jgarrison', 'password')
        tv = TimeValidator(datetime, WEHolidays())
        buildLights = TCBuildLights(lights, tc, tv)

        lights.setupGPIO()

        while 1:
            buildLights.main()
            time.sleep(5)

    except KeyboardInterrupt:
        lights.cleanup()
