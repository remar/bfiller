from Hours import Hours
from Time import Time

class TimeRange(object):
    def __init__(self, start = Time(0), end = Time(0)):
        assert(type(start) == Time and type(end) == Time)
        self.start = start
        self.end = end

    def get_length(self):
        return self.start.distance_to(self.end)

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def __str__(self):
        return str(self.start) + "-" + str(self.end)

    def __eq__(self, other):
        if other == None:
            return False
        return self.start == other.start and self.end == other.end

    def __add__(self, other):
        start = other.start if self.start > other.start else self.start
        end = self.end if self.end > other.end else other.end
        return TimeRange(start, end)
