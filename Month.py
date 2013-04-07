from datetime import date, timedelta
import calendar
from TimeRange import TimeRange
from Time import Time
from Hours import Hours
from Week import Week
from AnnotatedWeek import AnnotatedWeek

class Month(object):
    def __init__(self, year, month):
        self.year = year
        self.month = month
        self.days = {}
        self.weeks = {}

    def add_week(self, week_number, week):
        if self.month == 12 and week_number == 1:
            day = self._get_monday_number_for_week(week_number, self.year + 1)
        else:
            day = self._get_monday_number_for_week(week_number)

        first_weekday = 1
        last_weekday = 7

        if self._first_week(week_number):
            first_weekday = self._weekday_for_first_day()
            day = 1
        if self._last_week(week_number):
            last_weekday = self._weekday_for_last_day()

        stored_week = self._create_annotated_week(day, first_weekday, last_weekday)

        for i in xrange(first_weekday - 1, last_weekday):
            self.days[day] = week.get_day(i)
            stored_week.set_day(i, week.get_day(i))
            day += 1

        self.weeks[week_number] = stored_week

    def get_week(self, week_number):
        return self.weeks[week_number]

    def get_day(self, day):
        return self.days[day] if day in self.days else None

    def get_week_numbers(self):
        if self.month == 12 and self.get_last_week_number() == 1:
            r = range(self.get_first_week_number(),
                      self._get_last_week_number_for_year() + 1)
            r.append(1)
            return r

        if (self.month == 1
            and self.get_first_week_number() > self.get_last_week_number()):
            r = [52] # TODO: can also be [52, 53] for some years...
            r.extend(range(1, self.get_last_week_number() + 1))
            return r

        return range(self.get_first_week_number(),
                     self.get_last_week_number() + 1)

    def get_total_time(self):
        total = Hours(0)
        
        for i in xrange(1, self._get_last_day_number() + 1):
            day = self.get_day(i)
            if day != None:
                total += day.get_length()

        return total

    def _get_last_week_number_for_year(self):
        return 52

    def get_first_week_number(self):
        return self._get_week_number_for_day(1)

    def get_last_week_number(self):
        return self._get_week_number_for_day(self._get_last_day_number())

    def _get_week_number_for_day(self, day):
        return self._get_date_for_day(day).isocalendar()[1]

    def _get_date_for_day(self, day):
        return date(self.year, self.month, day)

    def _get_last_day_number(self):
        return calendar.monthrange(self.year, self.month)[1]

    def _first_monday(self, year, week):
        # http://stackoverflow.com/a/3314360
        d = date(year, 1, 4)  # The Jan 4th must be in week 1  according to ISO
        return d + timedelta(weeks=(week-1), days=-d.weekday())

    def _get_monday_date_for_week(self, week, year):
        return self._first_monday(year, week)

    def _get_monday_number_for_week(self, week, year = None):
        year = self.year if year == None else year
        return self._get_monday_date_for_week(week, year).day

    def _weekday_for_first_day(self):
        return date(self.year, self.month, 1).isoweekday()

    def _weekday_for_last_day(self):
        return date(self.year, self.month, self._get_last_day_number()).isoweekday()

    def _first_week(self, week_number):
        return week_number == self.get_first_week_number()

    def _last_week(self, week_number):
        return week_number == self.get_last_week_number()

    def __str__(self):
        lines = []
        mondays = []
        week = 0
        week_numbers = self.get_week_numbers()

        if self._get_monday_number_for_week(self.get_first_week_number()) == 1:
            mondays.append(1)
        else:
            week = 1

        for i in week_numbers[1:]:
            monday_number = self._get_monday_number_for_week(i)
            if len(mondays) > 0 and monday_number < mondays[0]:
                continue
            mondays.append(monday_number)

        lines.append(str(self.year) + " - " + str(self.month))

        for i in xrange(1, self._get_last_day_number() + 1):
            if i in mondays:
                lines.append("Week " + str(week_numbers[week]))
                week += 1
            day = self.get_day(i)
            if day != None:
                lines.append(str(i) + ": " + str(day))
        return "\n".join(lines)

    def _create_annotated_week(self, day, first_weekday, last_weekday):
        aw = AnnotatedWeek()
        aw.set_earliest_day_in_month(day)
        aw.set_first_valid_day(first_weekday - 1)
        aw.set_last_valid_day(last_weekday - 1)
        return aw
