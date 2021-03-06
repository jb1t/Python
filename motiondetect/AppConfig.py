import ConfigParser

class AppConfig:

    def __init__(self):
        self.EmailSettings = None
        self.IFTTT = None
        self.Settings = None

    def get_configuration(self):
        config = ConfigParser.ConfigParser()
        config.read('app.cfg')

        self.EmailSettings = EmailSettings(config)
        self.IFTTT = IFTTT(config)
        self.Settings = Settings(config)

        configurations = [self.EmailSettings, self.IFTTT, self.Settings]

        for c in configurations:
            c.get_configuration()


class EmailSettings:
    SETTINGS_KEY = 'Email'

    def __init__(self, config):
        self.config = config
        self.fromEmail = None
        self.toAddress = None
        self.userName = None
        self.smtpServer = None

    def get_configuration(self):
        self.fromEmail = self.config.get(self.SETTINGS_KEY, 'from_email')
        self.toAddress = self.config.get(self.SETTINGS_KEY, 'to_address')
        self.userName = self.config.get(self.SETTINGS_KEY, 'user_name')
        self.smtpServer = self.config.get(self.SETTINGS_KEY, 'smtp_server')


class IFTTT:
    SETTINGS_KEY = 'IFTTT'

    def __init__(self, config):
        self.config = config
        self.key = None

    def get_configuration(self):
        self.key = self.config.get(self.SETTINGS_KEY, 'key')


class Settings:
    SETTINGS_KEY = 'Settings'

    def __init__(self, config):
        self.config = config
        self.elapsedTimeSeconds = None
        self.pirPin = None
        self.mainThreadSleepSeconds = None

    def get_configuration(self):
        self.elapsedTimeSeconds = self.config.getint(self.SETTINGS_KEY, 'elapsed_time_seconds')
        self.pirPin = self.config.getint(self.SETTINGS_KEY, 'pir_pin')
        self.mainThreadSleepSeconds = self.config.getint(self.SETTINGS_KEY, 'main_thread_sleep_seconds')
