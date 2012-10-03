from Month import Month
from TimeGenerator import generate_week
from Hours import Hours

m = Month(2012, 1)

h = Hours(57, 50)

weeks = {}

for i in m.get_week_numbers():
    m.add_week(i, generate_week(h))

print m
