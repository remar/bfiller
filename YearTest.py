import unittest
from Year import Year
from Hours import Hours
from TimeRange import TimeRange
from Time import Time
from Week import Week

class YearTest(unittest.TestCase):
    def test_can_give_schedule_for_week(self):
        y = Year(2012)
        w = y.get_schedule_for_week(40, Hours(57, 50))
        self.assertEquals(w.get_day(0), TimeRange(Time(7), Time(17)))

    def test_gives_none_if_no_taken_week_specified(self):
        y = Year(2012)
        self.assertEquals(y.get_taken(40), None)

    def test_can_hold_blocked_ranges(self):
        y = Year(2012)
        blocked = Week()
        y.add_blocked(40, blocked)
        self.assertEquals(y.get_blocked(40), blocked)

    def test_can_hold_taken_week(self):
        y = Year(2012)
        taken = Week()
        y.add_taken(40, taken)

    def test_can_retrieve_taken_week(self):
        y = Year(2012)
        taken = Week()
        y.add_taken(40, taken)
        self.assertEquals(y.get_taken(40), taken)

    def test_uses_blocked_week_when_scheduling(self):
        y = Year(2012)
        blocked = Week()
        blocked.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
        y.add_blocked(40, blocked)

        w = y.get_schedule_for_week(40, Hours(57, 50))

        self.assertEquals(w.get_day(0).get_start(), Time(13, 30))

    def test_uses_taken_week_when_scheduling(self):
        y = Year(2012)
        taken = Week()
        taken.set_day(0, TimeRange(Time(13, 30), Time(17)))
        y.add_taken(40, taken)

        w = y.get_schedule_for_week(40, Hours(57, 50))

        self.assertEquals(w.get_day(0).get_start(), Time(17))

    def test_doesnt_schedule_hours_scheduled_by_taken_week(self):
        y = Year(2012)
        taken = Week()
        taken.set_day(0, TimeRange(Time(13, 30), Time(17)))
        y.add_taken(40, taken)

        w = y.get_schedule_for_week(40, Hours(57, 50))

        self.assertEquals(w.get_total_time(), Hours(54, 20))

    def test_respects_both_blocked_and_taken_weeks(self):
        y = Year(2012)
        blocked = Week()
        blocked.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
        y.add_blocked(40, blocked)
        taken = Week()
        taken.set_day(1, TimeRange(Time(7), Time(17)))
        y.add_taken(40, taken)

        w = y.get_schedule_for_week(40, Hours(57, 50))

        self.assertEquals(w.get_day(0).get_start(), Time(13, 30))
        self.assertEquals(w.get_day(1).get_start(), Time(17))

    def test_can_generate_monthly_report(self):
        y = Year(2012)
        m = y.generate_montly_report(10, Hours(57, 50))
        self.assertEquals(m.get_day(1), TimeRange(Time(7), Time(17)))

    def test_can_generate_realistic_monthly_report(self):
        y = Year(2012)
        blocked = self._get_daycare_week()
        taken = self._get_assistance_week()
        for i in [40, 41, 42, 43, 44]:
            y.add_blocked(i, blocked)
            y.add_taken(i, taken)
        m = y.generate_montly_report(10, Hours(57, 50))
        self.assertEquals(m.get_day(1), TimeRange(Time(17), Time(20)))
        self.assertEquals(m.get_day(2), TimeRange(Time(13, 30), Time(20)))

#TODO test January and December

    def _get_daycare_week(self):
        w = Week()
        w.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
        w.set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
        w.set_day(3, TimeRange(Time(8, 30), Time(13, 30)))
        return w

    def _get_assistance_week(self):
        w = Week()
        w.set_day(0, TimeRange(Time(13, 30), Time(17)))
        w.set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
        w.set_day(2, TimeRange(Time(7), Time(17)))
        w.set_day(3, TimeRange(Time(6, 30), Time(8, 30)))
        return w

if __name__ == "__main__":
    unittest.main()
