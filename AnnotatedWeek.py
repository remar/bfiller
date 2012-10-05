from Week import Week

class AnnotatedWeek(Week):
    def __init__(self):
        Week.__init__(self)
        self.set_first_valid_day(0)
        self.set_last_valid_day(6)

    def set_earliest_day_in_month(self, daynumber):
        self.earliest_daynumber = daynumber

    def get_earliest_day_in_month(self):
        return self.earliest_daynumber

    def set_first_valid_day(self, day):
        self.first_valid_day = day

    def get_first_valid_day(self):
        return self.first_valid_day

    def set_last_valid_day(self, day):
        self.last_valid_day = day

    def get_last_valid_day(self):
        return self.last_valid_day
