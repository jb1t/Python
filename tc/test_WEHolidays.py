import unittest
from WEHolidays import WEHolidays
from datetime import datetime


class Test_WEHolidaysTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.weholiday = WEHolidays()
        return super(Test_WEHolidaysTests, cls).setUpClass()

    def test_isHoliday_WhenNotAValidHoliday_ReturnsFalse(self):
        self.assertFalse(self.weholiday.isHoliday(datetime(2015, 11, 8)))

    def test_isHoliday_WhenValidHoliday_ReturnsTrue(self):
        self.assertTrue(self.weholiday.isHoliday(datetime(2015, 12, 24)))

    def test_isHoliday_InvalidDatetimePassed_ThrowsException(self):
        with self.assertRaisesRegexp(TypeError, 'userdate is not a datetime data type'):
            self.weholiday.isHoliday("bad data")


if __name__ == '__main__':
    unittest.main()
