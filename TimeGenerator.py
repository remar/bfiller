from Hours import Hours
from TimeRange import TimeRange
from Time import Time

def generate(hours_per_week, taken_times):
    times = []

    hours = hours_per_week.get_hours()

    while hours >= 10:
        times.append(Hours(10))
        hours -= 10

    if hours > 0 or hours_per_week.get_minutes() > 0:
        times.append(Hours(hours, hours_per_week.get_minutes()))

    return times

def generate_day(hours, taken = None):
    if taken != None:
        start = taken.get_end()
    else:
        start = Time(7, 0)
    return TimeRange(start, start.add_hours(hours))

def generate_week(hours):
    times = []

    h = hours.get_hours()

    while h >= 10:
        times.append(generate_day(Hours(10)))
        h -= 10

    if h > 0 or hours.get_minutes() > 0:
        times.append(generate_day(Hours(h, hours.get_minutes())))

    pad_with_none(times)

    return times

def pad_with_none(times):
    while len(times) < 7:
        times.append(None)
