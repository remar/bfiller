import unittest
from TimeRange import TimeRange
from Hours import Hours
from Time import Time

class TimeRangeTest(unittest.TestCase):
    def test_can_be_empty(self):
        time_range = TimeRange()
        self.assertEquals(time_range.get_length(), Hours(0))

    def test_simple_range_from_9_to_17_is_8_hours(self):
        time_range = TimeRange(Time(9, 0), Time(17, 0))
        self.assertEquals(time_range.get_length(), Hours(8))

    def test_can_give_length_for_9_to_10_30(self):
        time_range = TimeRange(Time(9), Time(10, 30))
        self.assertEquals(time_range.get_length(), Hours(1, 30))

    def test_can_return_start_time(self):
        time_range = TimeRange(Time(9), Time(10))
        self.assertEquals(time_range.get_start(), Time(9))

    def test_can_return_end_time(self):
        time_range = TimeRange(Time(9), Time(10))
        self.assertEquals(time_range.get_end(), Time(10))

    def test_can_be_printed(self):
        time_range = TimeRange(Time(9), Time(10, 30))
        self.assertEquals(str(time_range), "9:00-10:30")

    def test_can_be_compared_with_timerange(self):
        self.assertEquals(TimeRange(Time(7), Time(10)), TimeRange(Time(7), Time(10)))

    def test_can_be_concatenated(self):
        t1 = TimeRange(Time(8, 30), Time(13, 30))
        t2 = TimeRange(Time(13, 30), Time(17))
        t3 = t1 + t2
        self.assertEquals(t3, TimeRange(Time(8, 30), Time(17)))

    def test_addition_handles_associativity(self):
        t1 = TimeRange(Time(8, 30), Time(13, 30))
        t2 = TimeRange(Time(13, 30), Time(17))
        t3 = t2 + t1
        self.assertEquals(t3, TimeRange(Time(8, 30), Time(17)))

    def test_returns_false_when_compared_to_none(self):
        self.assertFalse(TimeRange(Time(7), Time(17)) == None)

if __name__ == "__main__":
    unittest.main()
