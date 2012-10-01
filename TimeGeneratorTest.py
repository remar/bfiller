import unittest
from TimeGenerator import generate, generate_day
from Hours import Hours
from Time import Time
from TimeRange import TimeRange

class TimeGeneratorTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_no_times_input_gives_full_week(self):
        times = generate(Hours(57, 50), [])
        self.assertEquals(len(times), 6)
        for i in xrange(5):
            self.assertEquals(times[i], Hours(10))
        self.assertEquals(times[5], Hours(7, 50))

    def test_can_generate_day_schedule_given_no_taken_hours(self):
        day = generate_day(Hours(10))
        self.assertEquals(day.get_start(), Time(7, 0))
        self.assertEquals(day.get_end(), Time(17, 0))

    def test_pushes_day_one_hour_forward_if_hour_taken(self):
        day = generate_day(Hours(10), TimeRange(Time(7), Time(8)))
        self.assertEquals(day.get_start(), Time(8))
        self.assertEquals(day.get_end(), Time(18))

if __name__ == "__main__":
    unittest.main()
