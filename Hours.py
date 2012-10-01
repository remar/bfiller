class Hours(object):
    def __init__(self, hours, minutes = 0):
        self.hours = hours
        self.minutes = minutes

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def get_total_minutes(self):
        return self.hours * 60 + self.minutes

    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes
