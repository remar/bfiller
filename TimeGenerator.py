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
    start = Time(7, 0)

    if taken != None:
        return TimeRange(Time(8, 0), Time(18, 0))
    return TimeRange(Time(7, 0), Time(7 + hours.get_hours(), 0))
