import unittest
from AppConfig import AppConfig


class Test_AppConfig(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     return super(Test_AppConfig, cls).setUpClass()

    def test_GetConfigurationForEmail(self):
        self.appConfiguration = AppConfig()
        self.appConfiguration.get_configuration()

        email_address = self.appConfiguration.EmailSettings.fromEmail

        self.assertEqual('your_email@gmail.com', email_address)

    def test_GetConfigurationForPirPin_VerifyIsInt(self):
        self.appConfiguration = AppConfig()
        self.appConfiguration.get_configuration()

        pin_number = self.appConfiguration.Settings.pirPin

        self.assertIsInstance(pin_number, int)
        self.assertEqual(13, pin_number)


if __name__ == '__main__':
    unittest.main()
