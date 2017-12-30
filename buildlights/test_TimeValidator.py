import unittest
from TimeValidator import TimeValidator
from datetime import datetime
from mock import Mock


class Test_TimeValidator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        return super(Test_TimeValidator, cls).setUpClass()

    def test_IsWorkWeekDay_WhenFriday_ReturnTrue(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(year=2015, month=8, day=28)

        tv = TimeValidator(mockDateTime, None)
        self.assertTrue(tv.IsWorkWeekDay())

    def test_IsWorkWeekDay_WhenSaturday_ReturnFalse(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(year=2015, month=8, day=29)

        tv = TimeValidator(mockDateTime, None)
        self.assertFalse(tv.IsWorkWeekDay())

    def test_IsWorkHours_When3am_ReturnsFalse(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(hour=3, minute=0, second=0, microsecond=0)

        tv = TimeValidator(mockDateTime, None)
        self.assertFalse(tv.IsWorkHours())

    def test_IsWorkHours_When3pm_ReturnsTrue(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(hour=15, minute=0, second=0, microsecond=0)

        tv = TimeValidator(mockDateTime, None)
        self.assertTrue(tv.IsWorkHours())

    def test_IsDisplayTime_When6pm_ReturnsFalse(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(year=2015, month=8, day=28, hour=18, minute=0, second=0, microsecond=0)

        mockWEHolidays = Mock()
        mockWEHolidays.isHoliday.return_value = False

        tv = TimeValidator(mockDateTime, mockWEHolidays)
        self.assertFalse(tv.IsDisplayTime())

    def test_IsDisplayTime_When3pm_ReturnsTrue(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(year=2015, month=8, day=28, hour=15, minute=0, second=0, microsecond=0)

        mockWEHolidays = Mock()
        mockWEHolidays.isHoliday.return_value = False

        tv = TimeValidator(mockDateTime, mockWEHolidays)
        self.assertTrue(tv.IsDisplayTime())

    def test_IsDisplayTime_WhenIsWorkHoursAndIsWorkWeekDayAndIsHoliday_ReturnsFalse(self):
        mockDateTime = Mock()
        mockDateTime.now.return_value = datetime.now().replace(year=2015, month=12, day=24, hour=15, minute=0, second=0, microsecond=0)

        mockWEHolidays = Mock()
        mockWEHolidays.isHoliday.return_value = True

        tv = TimeValidator(mockDateTime, mockWEHolidays)
        self.assertTrue(tv.IsWorkHours())
        self.assertTrue(tv.IsWorkWeekDay())
        self.assertFalse(tv.IsDisplayTime())


if __name__ == '__main__':
    unittest.main()
