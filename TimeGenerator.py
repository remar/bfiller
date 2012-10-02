from Hours import Hours
from TimeRange import TimeRange
from Time import Time
from Week import Week

DEFAULT_LATEST_TIME = Time(20)
DEFAULT_LONGEST_DAY = Hours(10)

def generate_day(hours, taken = None, latest_time = None):
    if taken != None:
        start = taken.get_end()
    else:
        start = Time(7, 0)
    new_end = start.add_hours(hours)

    if latest_time != None and new_end > latest_time:
        new_end = latest_time
    return TimeRange(start, new_end)

def generate_week(hours, taken_week = None, latest_time = None):
    latest_time = latest_time or DEFAULT_LATEST_TIME

    week = Week()
    day = 0
    while hours > Hours(0):
        taken_hours = taken_week.get_day(day) if taken_week != None else None
        if hours > DEFAULT_LONGEST_DAY:
            generated_day = generate_day(DEFAULT_LONGEST_DAY, taken_hours,
                                         latest_time)
        else:
            generated_day = generate_day(hours, taken_hours, latest_time)
        week.set_day(day, generated_day)
        day += 1
        hours -= generated_day.get_length()

    return week
