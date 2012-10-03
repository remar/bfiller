from Month import Month
from TimeGenerator import generate_week
from Hours import Hours
from ReportGenerator import ReportGenerator
from Year import Year
from Week import Week
from TimeRange import TimeRange
from Time import Time

m = Month(2012, 10)

h = Hours(48, 20)

weeks = {}

year = Year(2012)

blocked = Week()
blocked.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked.set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked.set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken = Week()
taken.set_day(0, TimeRange(Time(13, 30), Time(17)))
taken.set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken.set_day(2, TimeRange(Time(7), Time(17)))
taken.set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

for i in m.get_week_numbers():
    year.add_blocked(i, blocked)
    year.add_taken(i, taken)
#    m.add_week(i, generate_week(h))

report_gen = ReportGenerator()

report_gen.generate(year.generate_montly_report(10, h))
