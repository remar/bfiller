class WeekRecord(object):
    def __init__(self):
        self.blocked = None
        self.taken = None

    def set_blocked(self, blocked):
        self.blocked = blocked

    def get_blocked(self):
        return self.blocked

    def set_taken(self, taken):
        self.taken = taken

    def get_taken(self):
        return self.taken
