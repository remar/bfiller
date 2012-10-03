from TimeGenerator import generate_week
from Week import Week
from TimeRange import TimeRange
from Time import Time
from WeekRecord import WeekRecord
from Hours import Hours
from Month import Month

class Year(object):
    def __init__(self, year):
        self.year = year
        self.weeks = {}

    def generate_montly_report(self, month_number, hours):
        m = Month(self.year, month_number)
        for w in m.get_week_numbers():
            m.add_week(w, self.get_schedule_for_week(w, hours))
        return m

    def get_schedule_for_week(self, week_number, hours):
        disallowed = self._get_disallowed_week(week_number)
        hours -= self._get_taken_time(week_number)

        return generate_week(hours, disallowed)

    def add_blocked(self, week_number, blocked):
        if week_number not in self.weeks:
            self._setup_week(week_number)
        self.weeks[week_number].set_blocked(blocked)

    def get_blocked(self, week_number):
        return self.weeks[week_number].get_blocked()

    def add_taken(self, week_number, taken):
        if week_number not in self.weeks:
            self._setup_week(week_number)
        self.weeks[week_number].set_taken(taken)

    def get_taken(self, week_number):
        return (self.weeks[week_number].get_taken() if week_number in self.weeks
                else None)

    def _setup_week(self, week_number):
        self.weeks[week_number] = WeekRecord()

    def _get_disallowed_week(self, week_number):
        combined = None
        if week_number in self.weeks:
            blocked = self.get_blocked(week_number)
            taken = self.get_taken(week_number)

            if blocked != None and taken != None:
                combined = blocked + taken
            else:
                combined = taken if taken != None else blocked
        return combined

    def _get_taken_time(self, week_number):
        taken_time = Hours(0)

        taken = self.get_taken(week_number)
        if taken != None:
            taken_time = taken.get_total_time()

        return taken_time
