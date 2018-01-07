import xmltodict


class Project:
    def __init__(self):
        self.test = ""


class TeamCityProvider:
    def __init__(self, requests, appConfig, username, password):
        self.requests = requests
        self.username = username
        self.password = password
        self.config = appConfig

    def getTeamCityProjects(self):
        response = self.getprojectxml()

        doc = xmltodict.parse(response.content)
        projects = []

        for project in doc['Projects']['Project']:
            MyProject = Project()
            MyProject.name = project['@name']
            MyProject.status = project['@lastBuildStatus']
            MyProject.activity = project['@activity']
            projects.append(MyProject)

        return projects

    def getprojectxml(self):
        if self.config.getUseLocalFile():
            with open(self.config.getLocalFile(), "r") as myfile:
                response = myfile.read().replace('\n', '')
        else:
            response = self.requests.get(self.config.getTeamCityUrl(), timeout=10.000, auth=(self.username, self.password))
        return response
