import unittest
from TimeGenerator import generate_day, generate_week
from Hours import Hours
from Time import Time
from TimeRange import TimeRange
from Week import Week

class TimeGeneratorTest(unittest.TestCase):
    def test_can_generate_day_schedule_given_no_taken_hours(self):
        self.assertEquals(generate_day(Hours(10)), TimeRange(Time(7), Time(17)))

    def test_places_range_after_given_range(self):
        day = generate_day(Hours(10), TimeRange(Time(7), Time(8)))
        self.assertEquals(day.get_start(), Time(8))
        self.assertEquals(day.get_end(), Time(18))

    def test_can_generate_week_schedule_given_no_taken_hours(self):
        week = generate_week(Hours(57, 50))
        for i in xrange(5):
            self.assertEquals(week.get_day(i), TimeRange(Time(7), Time(17)))
        self.assertEquals(week.get_day(5), TimeRange(Time(7), Time(14, 50)))

    def test_first_day_is_shorter_if_day_is_taken(self):
        taken_week = Week()
        taken_week.set_day(0, TimeRange(Time(7), Time(17)))
        week = generate_week(Hours(40), taken_week)
        ranges = [TimeRange(Time(17), Time(20)),
                  TimeRange(Time(7), Time(17)),
                  TimeRange(Time(7), Time(17)),
                  TimeRange(Time(7), Time(17)),
                  TimeRange(Time(7), Time(14))]
        for i in xrange(5):
            self.assertEquals(week.get_day(i), ranges[i])

    def test_generates_realistic_schedule(self):
        taken_week = Week()
        taken = [TimeRange(Time(8, 30), Time(13, 30)),
                 TimeRange(Time(6, 30), Time(13, 30)),
                 TimeRange(Time(7), Time(17)),
                 TimeRange(Time(6, 30), Time(13, 30))]
        for i in xrange(len(taken)):
            taken_week.set_day(i, taken[i])

        week = generate_week(Hours(30, 20), taken_week)

        ranges = [TimeRange(Time(13, 30), Time(20)), # 23:50 left
                  TimeRange(Time(13, 30), Time(20)), # 17:20 left
                  TimeRange(Time(17), Time(20)), # 14:20 left
                  TimeRange(Time(13, 30), Time(20)), # 7:50 left
                  TimeRange(Time(7), Time(14, 50))] # 0:00 left
        for i in xrange(len(ranges)):
            self.assertEquals(week.get_day(i), ranges[i])

    def test_can_be_modified_with_latest_time(self):
        taken_week = Week()
        taken_week.set_day(0, TimeRange(Time(7), Time(17)))
        week = generate_week(Hours(40), taken_week, Time(22))
        self.assertEquals(week.get_day(0), TimeRange(Time(17), Time(22)))

if __name__ == "__main__":
    unittest.main()
