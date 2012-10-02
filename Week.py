from TimeRange import TimeRange

class Week(object):
    def __init__(self):
        self.days = [None, None, None, None, None, None, None]

    def get_day(self, day):
        return self.days[day]

    def set_day(self, day, time_range):
        self.days[day] = time_range

    def __str__(self):
        titles = ["M", "T", "O", "T", "F", "L", "S"]
        return "\n".join(map(lambda t, d: t + ": " + str(d), titles, self.days))
