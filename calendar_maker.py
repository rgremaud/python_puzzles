# import datetime
from datetime import date, timedelta

month_hash = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

week_days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def get_month():
    """Request month for calendar."""
    while True:
        month = str(input("Please enter the month: ").lower())
        try:
            month_value = month_hash[month]
            return month_value
        except KeyError:
            print("Invalid input. Please enter a valid month.")


def get_year():
    """Request year for calendar."""
    while True:
        year = input("Please enter the year: ")
        try:
            year_value = int(year)
            return year_value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def days_in_month(year, month_number):
    """Calculate total days in a month"""
    target_month = date(year, month_number, 1)
    next_month = date(year, month_number + 1, 1)
    total_days = next_month - target_month
    return total_days.days


def day_of_week(year, month, day):
    """Calculate the day of the week"""
    my_date = date(year, month, day)
    day_number = my_date.weekday()
    return day_number


def calendar_list(first_day):
    """Build an array for the days that need to be user for calendar"""
    shift_amount = day_of_week(first_day.year, first_day.month, first_day.day)
    calendar_array = []
    first_day_of_calendar = first_day - timedelta(shift_amount)
    i = 0
    while i < 42:
        calendar_array.append(first_day_of_calendar)
        first_day_of_calendar += timedelta(1)
        i += 1

    return calendar_array


def build_calendar():
    """Request the month and year for calendar"""
    month = get_month()
    year = get_year()
    first_day = date(year, month, 1)
    calendar_array = calendar_list(first_day)
    print_calendar(calendar_array)


def print_calendar(calendar_array):
    """Build the 7x6 grid to show calendar"""
    # Build the top line with week days
    week_day_line = ""
    for day in week_days:
        if len(day) == 6:
            week_day_line += f"|  {day}  "
        elif len(day) == 7:
            week_day_line += f"| {day}  "
        elif len(day) == 8:
            week_day_line += f"| {day} "
        elif len(day) == 9:
            week_day_line += f"| {day}"
    week_day_line += "|"

    # Build a dotted line to divide
    dotted_line = ("+----------" * 7) + "+"

    detail_line = f"| {calendar_array[0].day}        | 2        | 3        | 4        | 5        | 6        | 7        |"
    blank_line = (
        "|          |          |          |          |          |          |          |"
    )

    # Top line
    print(week_day_line)
    print(dotted_line)
    # Detail 1
    print(detail_line)
    print(blank_line)
    print(blank_line)
    print(dotted_line)
    print(detail_line)
    print(blank_line)
    print(blank_line)
    print(dotted_line)
    print(detail_line)
    print(blank_line)
    print(blank_line)
    print(dotted_line)
    print(detail_line)
    print(blank_line)
    print(blank_line)
    print(dotted_line)
    print(detail_line)
    print(blank_line)
    print(blank_line)
    print(dotted_line)
    print(detail_line)
    print(blank_line)
    print(blank_line)
    print(dotted_line)


build_calendar()
