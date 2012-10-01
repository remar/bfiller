import unittest
from Hours import Hours

class HoursTest(unittest.TestCase):
    def test_create_simple_hour_object(self):
        hours = Hours(10)
        self.assertEquals(hours.get_hours(), 10)

    def test_can_be_created_with_minutes(self):
        hours = Hours(10, 30)
        self.assertEquals(hours.get_minutes(), 30)

    def test_can_return_total_minutes(self):
        hours = Hours(1, 10)
        self.assertEquals(hours.get_total_minutes(), 70)

    def test_can_be_compared_with_other_hours_object(self):
        self.assertEquals(Hours(10), Hours(10))

if __name__ == "__main__":
    unittest.main()
