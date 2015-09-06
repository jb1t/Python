import unittest
from mock import Mock
from TeamCityProvider import TeamCityProvider


class Test_TeamCityProvider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        return super(Test_TeamCityProvider, cls).setUpClass()

    def test_getTeamCityProjects_WhenProjects_ReturnedValidated(self):
        # Setup
        mockRequests = Mock()
        response = """
            <Projects>
                <Project name='testproject1' lastBuildStatus='Success' activity='Sleeping' />
                <Project name='testproject2' lastBuildStatus='Failure' activity='Paused' />
            </Projects>
            """
        mockRequests.get.return_value = response
        tc = TeamCityProvider(mockRequests, 'username', 'password')

        # Act
        projects = tc.getTeamCityProjects()

        # Assert
        project1 = filter(lambda x: x.name == 'testproject1', projects)[0]
        project2 = filter(lambda x: x.name == 'testproject2', projects)[0]

        self.assertEqual(2, len(projects))
        self.assertEqual('testproject1', project1.name)
        self.assertEqual('Success', project1.status)
        self.assertEqual('Sleeping', project1.activity)
        self.assertEqual('testproject2', project2.name)
        self.assertEqual('Failure', project2.status)
        self.assertEqual('Paused', project2.activity)


if __name__ == '__main__':
    unittest.main()
