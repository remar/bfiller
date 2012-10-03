import unittest
from Week import Week
from Time import Time
from TimeRange import TimeRange

class WeekTest(unittest.TestCase):
    def test_can_be_empty(self):
        w = Week()
        for i in xrange(7):
            self.assertEquals(w.get_day(i), None)

    def test_can_set_day(self):
        w = Week()
        w.set_day(0, TimeRange(Time(7), Time(17)))
        self.assertEquals(w.get_day(0), TimeRange(Time(7), Time(17)))

    def test_can_be_printed(self):
        w = Week()
        for i in xrange(7):
            w.set_day(i, TimeRange(Time(7), Time(17)))
        self.assertEquals(str(w), """M: 7:00-17:00
T: 7:00-17:00
O: 7:00-17:00
T: 7:00-17:00
F: 7:00-17:00
L: 7:00-17:00
S: 7:00-17:00""")

    def test_can_be_concatenated(self):
        w1 = Week()
        w2 = Week()
        w1.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
        w2.set_day(0, TimeRange(Time(13, 30), Time(17)))

        w1.set_day(1, TimeRange(Time(7), Time(12)))

        w2.set_day(2, TimeRange(Time(8), Time(13)))

        w3 = w1 + w2
        self.assertEquals(w3.get_day(0), TimeRange(Time(8, 30), Time(17)))
        self.assertEquals(w3.get_day(1), TimeRange(Time(7), Time(12)))
        self.assertEquals(w3.get_day(2), TimeRange(Time(8), Time(13)))

if __name__ == "__main__":
    unittest.main()
