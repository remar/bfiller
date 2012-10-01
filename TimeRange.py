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
