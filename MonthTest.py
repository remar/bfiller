import unittest
from Month import Month
from Week import Week
from TimeRange import TimeRange
from Time import Time

class MonthTest(unittest.TestCase):
    def test_can_give_week_numbers_for_month(self):
        m = Month(2012, 10)
        self.assertEquals(m.get_week_numbers(), [40, 41, 42, 43, 44])

    def test_can_enter_times_from_week(self):
        m = Month(2012, 10)
        w = Week()
        w.set_day(0, TimeRange(Time(7), Time(17)))
        m.add_week(40, w)
        self.assertEquals(m.get_day(1), TimeRange(Time(7), Time(17)))

    def test_can_enter_times_from_second_week(self):
        m = Month(2012, 10)
        w = Week()
        w.set_day(0, TimeRange(Time(7), Time(17)))
        m.add_week(41, w)
        self.assertEquals(m.get_day(8), TimeRange(Time(7), Time(17)))

    def test_can_enter_times_from_last_week_in_month(self):
        m = Month(2012, 10)
        w = Week()
        w.set_day(2, TimeRange(Time(7), Time(17)))
        w.set_day(3, TimeRange(Time(7), Time(17)))
        m.add_week(44, w)
        self.assertEquals(m.get_day(31), TimeRange(Time(7), Time(17)))
        self.assertNotEquals(m.get_day(32), TimeRange(Time(7), Time(17)))

    def test_can_enter_times_into_first_incomplete_week(self):
        m = Month(2012, 11)
        w = Week()
        w.set_day(0, TimeRange(Time(7), Time(17)))
        w.set_day(3, TimeRange(Time(8), Time(18)))
        m.add_week(44, w)
        self.assertEquals(m.get_day(1), TimeRange(Time(8), Time(18)))

    def test_returns_correct_week_range_for_december(self):
        m = Month(2012, 12)
        self.assertEquals(m.get_week_numbers(), [48, 49, 50, 51, 52, 1])

    def test_can_add_week_1_of_next_year_to_december(self):
        m = Month(2012, 12)
        w = Week()
        w.set_day(0, TimeRange(Time(7), Time(10)))
        m.add_week(1, w)
        self.assertEquals(m.get_day(31), TimeRange(Time(7), Time(10)))

    def test_returns_correct_week_range_for_january(self):
        m = Month(2012, 1)
        self.assertEquals(m.get_week_numbers(), [52, 1, 2, 3, 4, 5])

    def test_can_add_week_52_of_previous_year_to_january(self):
        m = Month(2012, 1)
        w = Week()
        w.set_day(6, TimeRange(Time(7), Time(10)))
        m.add_week(52, w)
        self.assertEquals(m.get_day(1), TimeRange(Time(7), Time(10)))
        print m

if __name__ == "__main__":
    unittest.main()