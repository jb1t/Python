from datetime import datetime


class WEHolidays:
    def __init__(self):
        self.filename = 'weholidays.txt'
        self.readaccess = "r"
        self.holidays = []

    def isHoliday(self, userdate):

        if type(userdate) is not datetime:
            raise TypeError("userdate is not a datetime data type")

        if not self.holidays:
            f = open(self.filename, self.readaccess)

            for line in f:
                self.holidays.append(datetime.strptime(line.strip('\n'), "%Y-%m-%d"))

        return userdate in self.holidays
