from datetime import datetime

class WEHolidays:

    def __init__(self):
        self.filename = 'weholidays.txt'
        self.readaccess = "r"

    def isHoliday(self, userdate):

        if type(userdate) is not datetime:
            raise TypeError("userdate is not a datetime data type")

        f = open(self.filename, self.readaccess)
        holidays = []

        for line in f:
            holidays.append(datetime.strptime(line.strip('\n'), "%Y-%m-%d"))

        return userdate in holidays
