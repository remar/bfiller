from Hours import Hours

class Time(object):
    def __init__(self, hour, minute = 0):
        self.hour = hour
        self.minute = minute

    def get_hour(self):
        return self.hour

    def get_minute(self):
        return self.minute

    def get_total_minutes(self):
        return self.hour * 60 + self.minute

    def distance_to(self, other):
        diff = other.get_total_minutes() - self.get_total_minutes()
        hours = diff / 60
        minutes = diff % 60
        return Hours(hours, minutes)

    def add_hours(self, hours):
        minutes = self.get_total_minutes() + hours.get_total_minutes()
        return Time(minutes / 60, minutes % 60)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute
