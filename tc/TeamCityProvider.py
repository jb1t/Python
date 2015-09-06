import xmltodict
import ConfigParser
import io


class Project:
    def __init__(self):
        self.test = ""


class TeamCityProvider:
    def __init__(self, requests, username, password):
        self.getconfiguration()

        self.requests = requests
        self.username = username
        self.password = password

    def getconfiguration(self):
        config = ConfigParser.ConfigParser()
        config.read('app.cfg')
        self.uselocalfile = config.getboolean('TeamCity', 'uselocalfile')
        self.localfile = config.get('TeamCity', 'localfile')
        self.url = config.get('TeamCity', 'url')

    def getTeamCityProjects(self):
        response = self.getprojectxml()

        doc = xmltodict.parse(response)
        projects = []

        for project in doc['Projects']['Project']:
            MyProject = Project()
            MyProject.name = project['@name']
            MyProject.status = project['@lastBuildStatus']
            MyProject.activity = project['@activity']
            projects.append(MyProject)

        return projects

    def getprojectxml(self):
        if self.uselocalfile:
            with open(self.localfile, "r") as myfile:
                response = myfile.read().replace('\n', '')
        else:
            response = self.requests.get(self.tc_url, timeout=10.000, auth=(self.username, self.password))
        return response
