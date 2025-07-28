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
    print_calendar(calendar_array, month, year)


def print_calendar(calendar_array, month, year):
    """Build the 7x6 grid to show calendar"""
    reverse_month_hash = {value: key for key, value in month_hash.items()}
    month_word = reverse_month_hash.get(month)
    calendar_string = (
        f"                             {month_word.capitalize()}, {year}\n"
    )

    for day in week_days:
        if len(day) == 6:
            calendar_string += f"|  {day}  "
        elif len(day) == 7:
            calendar_string += f"| {day}  "
        elif len(day) == 8:
            calendar_string += f"| {day} "
        elif len(day) == 9:
            calendar_string += f"| {day}"
    calendar_string += f"|\n"

    # Build a dotted line to divide
    dotted_line = ("+----------" * 7) + f"+\n"

    # add initial dotted line
    calendar_string += dotted_line

    detail_array = ["|", "|", "|", "|", "|", "|"]

    j, i = 0, 0
    q = 0
    r = 6
    while j < 6:
        while i >= q and i <= r:
            if calendar_array[i].day > 9:
                detail_array[j] += f" {calendar_array[i].day}       |"
            elif calendar_array[i].day < 10:
                detail_array[j] += f" {calendar_array[i].day}        |"

            i += 1
        q += 7
        r += 7
        j += 1

    blank_line = (
        ("|" + ("          |" * 7))
        + f"\n"
        + ("|" + ("          |" * 7) + f"\n" + dotted_line)
    )

    for detail in detail_array:
        detail += f"\n"
        detail += blank_line
        calendar_string += detail

    print(calendar_string)


build_calendar()
