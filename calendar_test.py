#!/usr/bin/env python3

from datetime import date
import calendar

# get the current year and month
today = date.today()
current_year = today.year
current_month = today.month

# print TextCalendar - 2020
c = calendar.TextCalendar(calendar.MONDAY)
c.setfirstweekday(0)
st = c.formatmonth(current_year, current_month, 3, 1)
print(st)

# print all days of the month
for d in calendar.day_name:
    print(d)

# print all months of the current year
for m in calendar.month_name:
    print(m)