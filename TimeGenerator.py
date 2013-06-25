from Hours import Hours
from TimeRange import TimeRange
from Time import Time
from Week import Week

DEFAULT_EARLIEST_TIME = Time(7)
DEFAULT_LATEST_TIME = Time(20)
DEFAULT_LONGEST_DAY = Hours(10)

def generate_day(hours, taken = None, latest_time = None):
    if taken != None:
        start = taken.get_end()
    else:
        start = DEFAULT_EARLIEST_TIME
    new_end = start.add_hours(hours)

    if latest_time != None and new_end > latest_time:
        new_end = latest_time
    return TimeRange(start, new_end)

def generate_week(hours, taken_week = None, latest_time = None):
    latest_time = latest_time or DEFAULT_LATEST_TIME
    longest_day = DEFAULT_LONGEST_DAY

    week = Week()
    day = 0
    while hours > Hours(0):
        assert(day < 7)
        taken_hours = taken_week.get_day(day) if taken_week != None else None
        generated_day = generate_day(longest_day if hours > longest_day else hours,
                                     taken_hours,
                                     latest_time)
        if generated_day.get_length().get_total_minutes() > 0:
            week.set_day(day, generated_day)
        day += 1
        hours -= generated_day.get_length()

    return week
