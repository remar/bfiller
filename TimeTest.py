import unittest
from Time import Time
from Hours import Hours

class TimeTest(unittest.TestCase):
    def test_can_specify_simple_time(self):
        time = Time(7)
        self.assertEquals(time.get_hour(), 7)

    def test_can_specify_minute(self):
        time = Time(10, 30)
        self.assertEquals(time.get_minute(), 30)

    def test_can_calculate_time_distance(self):
        t1 = Time(7)
        t2 = Time(8)
        self.assertEquals(t1.distance_to(t2), Hours(1))

    def test_can_calculate_time_distance_for_half_hour(self):
        t1 = Time(7)
        t2 = Time(7, 30)
        self.assertEquals(t1.distance_to(t2), Hours(0, 30))

    def test_can_be_compared_for_equality(self):
        self.assertEquals(Time(7), Time(7))

    def test_can_be_moved_by_hours(self):
        self.assertEquals(Time(7).add_hours(Hours(10)), Time(17))

    def test_can_be_printed(self):
        self.assertEquals(str(Time(7)), "7:00")

if __name__ == "__main__":
    unittest.main()
