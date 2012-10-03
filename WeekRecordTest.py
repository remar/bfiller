import unittest
from WeekRecord import WeekRecord
from Week import Week

class WeekRecordTest(unittest.TestCase):
    def test_exists(self):
        wr = WeekRecord()

    def test_can_hold_blocked_week(self):
        blocked = Week()
        wr = WeekRecord()
        wr.set_blocked(blocked)

    def test_can_get_blocked_week(self):
        blocked = Week()
        wr = WeekRecord()
        wr.set_blocked(blocked)
        self.assertEquals(wr.get_blocked(), blocked)

    def test_can_hold_taken_week(self):
        taken = Week()
        wr = WeekRecord()
        wr.set_taken(taken)

    def test_can_get_taken_week(self):
        taken = Week()
        wr = WeekRecord()
        wr.set_taken(taken)
        self.assertEquals(wr.get_taken(), taken)

    def test_get_blocked_returns_none_if_not_set(self):
        wr = WeekRecord()
        self.assertEquals(wr.get_blocked(), None)

if __name__ == "__main__":
    unittest.main()
