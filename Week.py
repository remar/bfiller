from TimeRange import TimeRange
from Hours import Hours

class Week(object):
    def __init__(self):
        self.days = [None, None, None, None, None, None, None]

    def get_day(self, day):
        return self.days[day]

    def set_day(self, day, time_range):
        self.days[day] = time_range

    def get_total_time(self):
        total = Hours(0)

        for day in self.days:
            if day != None:
                total += day.get_length()

        return total

    def __str__(self):
        titles = ["M", "T", "O", "T", "F", "L", "S"]
        return "\n".join(map(lambda t, d: t + ": " + str(d), titles, self.days))

    def __add__(self, other):
        new_week = Week()
        for i in xrange(7):
            d1 = self.get_day(i)
            d2 = other.get_day(i)
            if d1 != None and d2 != None:
                new_week.set_day(i, d1 + d2)
            else:
                new_week.set_day(i, d1 if d1 != None else d2)
        return new_week
