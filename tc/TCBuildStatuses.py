import requests, xmltodict

tc_url = "http://pc21568:90/httpAuth/app/rest/cctray/projects.xml"
response = requests.get(tc_url, auth=('username', 'password'))
doc = xmltodict.parse(response.text)
projects = doc['Projects']['Project']

overallStatus = "Success"

for project in projects:
    projectName = project['@name']
    buildStatus = project['@lastBuildStatus']
    if buildStatus != 'Success' and buildStatus != 'Unknown' and projectName.count(":: Deploy") == 0:
        overallStatus = "Failure"
        print(projectName, buildStatus)
        #break

print(overallStatus)
