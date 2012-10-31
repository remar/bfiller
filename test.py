from Month import Month
from TimeGenerator import generate_week
from Hours import Hours
from ReportGenerator import ReportGenerator
from Year import Year
from Week import Week
from TimeRange import TimeRange
from Time import Time

#m = Month(2012, 11)

h1 = Hours(48, 20)

weeks = {}

year = Year(2012)

# blocked = Week()
# blocked.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
# blocked.set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
# blocked.set_day(3, TimeRange(Time(8, 30), Time(13, 30)))
# 
# taken = Week()
# taken.set_day(0, TimeRange(Time(13, 30), Time(17)))
# taken.set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
# taken.set_day(2, TimeRange(Time(7), Time(17)))
# taken.set_day(3, TimeRange(Time(6, 30), Time(8, 30)))
# 
# for i in m.get_week_numbers():
#     year.add_blocked(i, blocked)
#     year.add_taken(i, taken)
# 

blocked = {}
taken = {}

blocked[40] = Week()
blocked[40].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[40].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[40].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[40] = Week()
taken[40].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[40].set_day(2, TimeRange(Time(7), Time(17)))


blocked[41] = Week()
blocked[41].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[41].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[41].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[41] = Week()
taken[41].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[41].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[41].set_day(2, TimeRange(Time(7), Time(17)))
taken[41].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))


blocked[42] = Week()
blocked[42].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[42].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[42].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))


blocked[43] = Week()
blocked[43].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[43].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[43].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[43] = Week()
taken[43].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[43].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[43].set_day(2, TimeRange(Time(7), Time(17)))
taken[43].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))


blocked[44] = Week()
blocked[44].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[44].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))

taken[44] = Week()
taken[44].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[44].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[44].set_day(2, TimeRange(Time(7), Time(17)))


for i in blocked.keys():
     year.add_blocked(i, blocked[i])

for i in taken.keys():
     year.add_taken(i, taken[i])

report_gen = ReportGenerator()

report_gen.generate(year.generate_montly_report(10, h1))
