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
year = {}

year[2012] = Year(2012)
year[2013] = Year(2013)

year[2012].set_next_year(year[2013])

# blocked2012 = Week()
# blocked2012.set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
# blocked2012.set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
# blocked2012.set_day(3, TimeRange(Time(8, 30), Time(13, 30)))
# 
# taken2012 = Week()
# taken2012.set_day(0, TimeRange(Time(13, 30), Time(17)))
# taken2012.set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
# taken2012.set_day(2, TimeRange(Time(7), Time(17)))
# taken2012.set_day(3, TimeRange(Time(6, 30), Time(8, 30)))
# 
# for i in m.get_week_numbers():
#     year[2012].add_blocked(i, blocked2012)
#     year[2012].add_taken(i, taken2012)
# 

blocked = {}
blocked[2012] = {}
blocked[2013] = {}
taken = {}
taken[2012] = {}
taken[2013] = {}

# October

blocked[2012][40] = Week()
blocked[2012][40].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][40].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][40].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][40] = Week()
taken[2012][40].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][40].set_day(2, TimeRange(Time(7), Time(17)))


blocked[2012][41] = Week()
blocked[2012][41].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][41].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][41].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][41] = Week()
taken[2012][41].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2012][41].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][41].set_day(2, TimeRange(Time(7), Time(17)))
taken[2012][41].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))


blocked[2012][42] = Week()
blocked[2012][42].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][42].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][42].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))


blocked[2012][43] = Week()
blocked[2012][43].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][43].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][43].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][43] = Week()
taken[2012][43].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2012][43].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][43].set_day(2, TimeRange(Time(7), Time(17)))
taken[2012][43].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))


blocked[2012][44] = Week()
blocked[2012][44].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][44].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][44] = Week()
taken[2012][44].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2012][44].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][44].set_day(2, TimeRange(Time(7), Time(17)))

# November

blocked[2012][45] = Week()
blocked[2012][45].set_day(0, TimeRange(Time(8, 30), Time(11, 0)))
blocked[2012][45].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][45].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][45] = Week()
taken[2012][45].set_day(0, TimeRange(Time(11, 0), Time(17)))
taken[2012][45].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][45].set_day(2, TimeRange(Time(7), Time(17)))
taken[2012][45].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2012][46] = Week()
blocked[2012][46].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][46].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][46].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][46] = Week()
taken[2012][46].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2012][46].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][46].set_day(2, TimeRange(Time(7), Time(17)))
taken[2012][46].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2012][47] = Week()
blocked[2012][47].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][47].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][47].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][47] = Week()
taken[2012][47].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2012][47].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2012][47].set_day(2, TimeRange(Time(7), Time(17)))
taken[2012][47].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2012][48] = Week()
blocked[2012][48].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][48].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2012][48].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2012][48] = Week()
taken[2012][48].set_day(0, TimeRange(Time(13, 30), Time(17))) # Linda

# December

taken[2012][49] = Week()
taken[2012][49].set_day(0, TimeRange(Time(11), Time(14, 30))) #3 -14.30
taken[2012][49].set_day(1, TimeRange(Time(6, 30), Time(12, 30))) #4
taken[2012][49].set_day(2, TimeRange(Time(7), Time(17))) #5
taken[2012][49].set_day(3, TimeRange(Time(6, 30), Time(12, 30))) #6

taken[2012][50] = Week()
taken[2012][50].set_day(0, TimeRange(Time(11), Time(14, 30))) #10
taken[2012][50].set_day(1, TimeRange(Time(7), Time(12, 30))) #11 07.00-

taken[2012][51] = Week()
taken[2012][51].set_day(2, TimeRange(Time(7), Time(17))) #19

# January

blocked[2013][2] = Week()
blocked[2013][2].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][2].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][2].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][2] = Week()
taken[2013][2].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2013][2].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2013][2].set_day(2, TimeRange(Time(7), Time(17)))
taken[2013][2].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2013][3] = Week()
blocked[2013][3].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][3].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][3].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][3] = Week()
taken[2013][3].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2013][3].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2013][3].set_day(2, TimeRange(Time(7), Time(17)))
taken[2013][3].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2013][4] = Week()
blocked[2013][4].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][4].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][4].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][4] = Week()
taken[2013][4].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2013][4].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2013][4].set_day(2, TimeRange(Time(7), Time(17))) #Maria
taken[2013][4].set_day(3, TimeRange(Time(6, 30), Time(8, 30))) #Maria

blocked[2013][5] = Week()
blocked[2013][5].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][5].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][5].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][5] = Week()
taken[2013][5].set_day(1, TimeRange(Time(6, 30), Time(8, 30))) #Linda
taken[2013][5].set_day(2, TimeRange(Time(7), Time(17))) #Maria
taken[2013][5].set_day(3, TimeRange(Time(6, 30), Time(8, 30))) #Maria

# February

blocked[2013][6] = Week()
blocked[2013][6].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][6].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][6].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][6] = Week()
taken[2013][6].set_day(1, TimeRange(Time(6, 30), Time(8, 30))) # Linda
taken[2013][6].set_day(2, TimeRange(Time(7), Time(17))) # Linda
taken[2013][6].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2013][7] = Week()
blocked[2013][7].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][7].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][7].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][7] = Week()
taken[2013][7].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2013][7].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2013][7].set_day(2, TimeRange(Time(7), Time(17)))
taken[2013][7].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2013][8] = Week()
blocked[2013][8].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][8].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][8].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][8] = Week()
taken[2013][8].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2013][8].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2013][8].set_day(2, TimeRange(Time(7), Time(17)))
taken[2013][8].set_day(3, TimeRange(Time(6, 30), Time(8, 30)))

blocked[2013][9] = Week()
blocked[2013][9].set_day(0, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][9].set_day(1, TimeRange(Time(8, 30), Time(13, 30)))
blocked[2013][9].set_day(3, TimeRange(Time(8, 30), Time(13, 30)))

taken[2013][9] = Week()
taken[2013][9].set_day(0, TimeRange(Time(13, 30), Time(17)))
taken[2013][9].set_day(1, TimeRange(Time(6, 30), Time(8, 30)))
taken[2013][9].set_day(2, TimeRange(Time(7), Time(17)))


for y in (2012, 2013):
     for i in blocked[y].keys():
          year[y].add_blocked(i, blocked[y][i])
     for i in taken[y].keys():
          year[y].add_taken(i, taken[y][i])

report_gen = ReportGenerator()

report_gen.generate(year[2013].generate_montly_report(2, h1))
