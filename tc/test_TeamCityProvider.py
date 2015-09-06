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
        response = type('Dummy', (object,), {"text": """
            <Projects>
                <Project name='testproject1' lastBuildStatus='Success' activity='NotPaused' />
                <Project name='testproject2' lastBuildStatus='Failed' activity='Paused' />
            </Projects>
            """})
        mockRequests.get.return_value = response
        tc = TeamCityProvider(mockRequests, 'username', 'password')

        # Act
        projects = tc.getTeamCityProjects()

        # Assert
        project1 = filter(lambda x: x.name == 'Coverage Router :: CI', projects)[0]
        project2 = filter(lambda x: x.name == 'Coverage TextAnalyzer :: CI', projects)[0]

        self.assertEqual(107, len(projects))
        self.assertEqual('Coverage Router :: CI', project1.name)
        self.assertEqual('Success', project1.status)
        self.assertEqual('Sleeping', project1.activity)
        self.assertEqual('Coverage TextAnalyzer :: CI', project2.name)
        self.assertEqual('Failure', project2.status)
        self.assertEqual('Sleeping', project2.activity)


if __name__ == '__main__':
    unittest.main()
