class TimeValidator:
    def __init__(self, datetime, weholidays):
        self.datetime = datetime
        self.weholidays = weholidays

    def IsWorkWeekDay(self):
        now = self.datetime.now()

        return 0 <= now.weekday() < 5

    def IsWorkHours(self):
        now = self.datetime.now()

        today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
        today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)

        return today8am < now < today5pm

    def IsDisplayTime(self):
        now = self.datetime.now()

        return self.IsWorkHours() and self.IsWorkWeekDay() and not self.weholidays.isHoliday(now)

    def DisplayInfo(self):
        now = self.datetime.now()
        print 'now=', now, 'weekday()=', now.weekday(), ' where Monday=0, Sunday=6', 'isHoliday=', self.weholidays.isHoliday(
            now), 'isDisplayTime=', self.IsDisplayTime()
