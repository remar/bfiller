import unittest
from AnnotatedWeek import AnnotatedWeek

class AnnotatedWeekTest(unittest.TestCase):
    def test_exists(self):
        aw = AnnotatedWeek()

    def test_can_set_first_day_in_month_for_week(self):
        aw = AnnotatedWeek()
        aw.set_earliest_day_in_month(20)

    def test_can_get_first_day_in_month_for_week(self):
        aw = AnnotatedWeek()
        aw.set_earliest_day_in_month(20)
        self.assertEquals(aw.get_earliest_day_in_month(), 20)

    def test_can_set_first_weekday_inside_month(self):
        aw = AnnotatedWeek()
        aw.set_first_valid_day(2)

    def test_can_get_first_weekday_inside_month(self):
        aw = AnnotatedWeek()
        aw.set_first_valid_day(2)
        self.assertEquals(aw.get_first_valid_day(), 2)

    def test_can_set_last_weekday_inside_month(self):
        aw = AnnotatedWeek()
        aw.set_last_valid_day(5)

    def test_can_get_last_weekday_inside_month(self):
        aw = AnnotatedWeek()
        aw.set_last_valid_day(5)
        self.assertEquals(aw.get_last_valid_day(), 5)

    def test_has_sane_default_values(self):
        aw = AnnotatedWeek()
        self.assertEquals(aw.get_first_valid_day(), 0)
        self.assertEquals(aw.get_last_valid_day(), 6)

if __name__ == "__main__":
    unittest.main()
