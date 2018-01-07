import ConfigParser


class AppConfig():

    def __init__(self):
        self.datetime = None
        self.weholidays = None
        self.tc_url = None
        self.uselocalfile = False
        self.localfile = None
        self.getconfiguration()

    def getUseLocalFile(self):
        return self.uselocalfile

    def getLocalFile(self):
        return self.localfile

    def getTeamCityUrl(self):
        return self.tc_url

    def getconfiguration(self):
        config = ConfigParser.ConfigParser()
        config.read('app.cfg')
        self.uselocalfile = config.getboolean('TeamCity', 'uselocalfile')
        self.localfile = config.get('TeamCity', 'localfile')
        self.tc_url = config.get('TeamCity', 'url')
