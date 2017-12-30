import unittest
from mock import Mock
from TCBuildStatuses import TCBuildLights
from LightProvider import LightProvider
from TeamCityProvider import Project


class Test_TCBuildStatuses(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        return super(Test_TCBuildStatuses, cls).setUpClass()

    def setUp(self):
        self.mocklights = Mock()
        self.mockteamcity = Mock()
        self.mocktimevalidator = Mock()

    def tearDown(self):
        self.mocklights = None
        self.mockteamcity = None
        self.mocktimevalidator = None

    def test_main_RunningAfterHours_CallIsDisplayTime(self):

        self.mocktimevalidator.IsDisplayTime.return_value = False
        buildLights = TCBuildLights(self.mocklights, self.mockteamcity, self.mocktimevalidator)

        buildLights.main()

        self.assertTrue(self.mocktimevalidator.IsDisplayTime.called)

    def test_main_RunningDuringBusinessHoursWithFailure_SetupGPIOAndGetStatusToDisplayLightUpRed(self):
        # setup
        self.mocktimevalidator.IsDisplayTime.return_value = True

        project1 = Project()
        project1.name = 'test1'
        project1.status = 'Success'
        project1.activity = 'Sleeping'
        project2 = Project()
        project2.name = 'test2'
        project2.status = 'Failure'
        project2.activity = 'Sleeping'

        self.mockteamcity.getTeamCityProjects.return_value = [project1, project2]
        buildLights = TCBuildLights(self.mocklights, self.mockteamcity, self.mocktimevalidator)

        # act
        buildLights.main()

        # test
        self.assertTrue(self.mocktimevalidator.IsDisplayTime.called)
        self.assertTrue(self.mocklights.setupGPIO.called)
        self.assertTrue(self.mockteamcity.getTeamCityProjects.called)
        self.assertTrue(self.mocklights.clearPins.called)
        self.mocklights.lightPin.assert_called_once_with(LightProvider.RED_PIN())

    def test_main_RunningDuringBusinessHoursWithAllSuccess_SetupGPIOAndGetStatusToDisplayLightUpGreen(self):
        # setup
        self.mocktimevalidator.IsDisplayTime.return_value = True

        project1 = Project()
        project1.name = 'test1'
        project1.status = 'Success'
        project1.activity = 'Sleeping'
        project2 = Project()
        project2.name = 'test2'
        project2.status = 'Success'
        project2.activity = 'Sleeping'

        self.mockteamcity.getTeamCityProjects.return_value = [project1, project2]
        buildLights = TCBuildLights(self.mocklights, self.mockteamcity, self.mocktimevalidator)

        # act
        buildLights.main()

        # test
        self.assertTrue(self.mocktimevalidator.IsDisplayTime.called)
        self.assertTrue(self.mocklights.setupGPIO.called)
        self.assertTrue(self.mockteamcity.getTeamCityProjects.called)
        self.assertTrue(self.mocklights.clearPins.called)
        self.mocklights.lightPin.assert_called_once_with(LightProvider.GREEN_PIN())

    def test_main_WhenDeployProjectFailedButAllCIBuildsAreSuccess_LightUpGreen(self):
        # setup
        self.mocktimevalidator.IsDisplayTime.return_value = True

        project1 = Project()
        project1.name = 'test1'
        project1.status = 'Success'
        project1.activity = 'Sleeping'
        project2 = Project()
        project2.name = 'test2'
        project2.status = 'Success'
        project2.activity = 'Sleeping'
        project3 = Project()
        project3.name = 'test3 :: Deploy'
        project3.status = 'Failure'
        project3.activity = 'Sleeping'

        self.mockteamcity.getTeamCityProjects.return_value = [project1, project2, project3]
        buildLights = TCBuildLights(self.mocklights, self.mockteamcity, self.mocktimevalidator)

        # act
        buildLights.main()

        # test
        self.assertTrue(self.mocktimevalidator.IsDisplayTime.called)
        self.assertTrue(self.mocklights.setupGPIO.called)
        self.assertTrue(self.mockteamcity.getTeamCityProjects.called)
        self.assertTrue(self.mocklights.clearPins.called)
        self.mocklights.lightPin.assert_called_once_with(LightProvider.GREEN_PIN())

    def test_main_WhenCIProjectPausedAndFailed_DoNotConsiderItForOverallStatus(self):
        # setup
        self.mocktimevalidator.IsDisplayTime.return_value = True

        project1 = Project()
        project1.name = 'project :: CI'
        project1.status = 'Failure'
        project1.activity = 'Paused'
        project2 = Project()
        project2.name = 'project2 :: CI'
        project2.status = 'Success'
        project2.activity = 'Sleeping'
        project3 = Project()
        project3.name = 'project3 :: CI'
        project3.status = 'Success'
        project3.activity = 'Sleeping'

        self.mockteamcity.getTeamCityProjects.return_value = [project1, project2, project3]
        buildLights = TCBuildLights(self.mocklights, self.mockteamcity, self.mocktimevalidator)

        # act
        buildLights.main()

        # test
        self.assertTrue(self.mocktimevalidator.IsDisplayTime.called)
        self.assertTrue(self.mocklights.setupGPIO.called)
        self.assertTrue(self.mockteamcity.getTeamCityProjects.called)
        self.assertTrue(self.mocklights.clearPins.called)
        self.mocklights.lightPin.assert_called_once_with(LightProvider.GREEN_PIN())

if __name__ == '__main__':
    unittest.main()
