from Hours import Hours
from Time import Time

class TimeRange(object):
    def __init__(self, start = Time(0), end = Time(0)):
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
        return self.start == other.start and self.end == other.end
