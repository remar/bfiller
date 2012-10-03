from Month import Month
from TimeGenerator import generate_week
from Hours import Hours
from ReportGenerator import ReportGenerator

m = Month(2012, 10)

h = Hours(48)

weeks = {}

for i in m.get_week_numbers():
    m.add_week(i, generate_week(h))

report_gen = ReportGenerator()

report_gen.generate(m)
