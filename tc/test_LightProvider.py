import unittest
from mock import Mock
from LightProvider import LightProvider


class Test_LightProvider(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        return super(Test_LightProvider, cls).setUpClass()

    def test_setupGPIO(self):
        mockGPIO = Mock()

        lp = LightProvider(mockGPIO)
        lp.setupGPIO()

        self.assertTrue(mockGPIO.output.called)
        mockGPIO.setmode.assert_any_call(mockGPIO.BOARD)
        mockGPIO.setup.assert_any_call(LightProvider.RED_PIN(), mockGPIO.OUT)
        mockGPIO.setup.assert_any_call(LightProvider.GREEN_PIN(), mockGPIO.OUT)
        mockGPIO.setup.assert_any_call(LightProvider.YELLOW_PIN(), mockGPIO.OUT)
        mockGPIO.output.assert_any_call(LightProvider.RED_PIN(), mockGPIO.LOW)
        mockGPIO.output.assert_any_call(LightProvider.GREEN_PIN(), mockGPIO.LOW)
        mockGPIO.output.assert_any_call(LightProvider.YELLOW_PIN(), mockGPIO.LOW)

    def test_clearPins(self):
        mockGPIO = Mock()

        lp = LightProvider(mockGPIO)
        lp.clearPins()

        mockGPIO.output.assert_any_call(LightProvider.RED_PIN(), mockGPIO.LOW)
        mockGPIO.output.assert_any_call(LightProvider.GREEN_PIN(), mockGPIO.LOW)
        mockGPIO.output.assert_any_call(LightProvider.YELLOW_PIN(), mockGPIO.LOW)

    def test_lightPin_WhenCalled_PinSetToHigh(self):
        mockGPIO = Mock()

        lp = LightProvider(mockGPIO)
        lp.lightPin(LightProvider.RED_PIN())

        mockGPIO.output.assert_called_once_with(LightProvider.RED_PIN(), mockGPIO.HIGH)

    def test_cleanup_WhenCalled_GPIOCleanupIsCalled(self):
        mockGPIO = Mock()

        lp = LightProvider(mockGPIO)
        lp.cleanup()

        self.assertTrue(mockGPIO.cleanup.called)


if __name__ == '__main__':
    unittest.main()
