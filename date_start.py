#!/usr/bin/env python38

# import date and time 
from datetime import date
from datetime import time
from datetime import datetime


# create current date
today = date.today()
# print(today)




# print individual date components (year, month, day, weekday)
# print('Date individual components: Year: {0}, Month: {1}, Day: {2}'.format(today.year, today.month, today.day))

# extract days of the week
# print(today.weekday())

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# print('Which is: ', days[today.weekday()])

                                   # How to get the current date and time
# now = datetime.now()
# print("it's ", now, ' today')

# print(now.microsecond)
# print('Time Zone: ', now.tzinfo)


# How to create a date object
birthdate = date(1980, 11, 12)

# print('Your date of birth: ', birthdate)

# How to create a datetime object
dob = datetime(1978, 1, 12, 15, 30, 0)

# print('Your date and time of birth: ', dob)

# Can extract (year, month, day, hour, minute, second, microsecond, and tzinfo)
# print('Your birth minute: ', dob.minute)

# how to work with date formatting
# Format strings %a/%A - weekday, %d -day, %b/%B - month, %y/%y - year 
# print(dob.strftime('Your dob: %A %B %d, %Y :T: %H:%M'))


# How to work with time
time_now = time(0, 4, 1)
# print(time_now.strftime('Time is: %I:%M:%S %p'))

#daTe = localtime()
#print(now.daTe())

def get_birth_date():
    while True:
        birth_date_str = input("Enter date of birth(dd/mm/yyyy): ")
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
            return birth_date
        except ValueError:
            print("Invalid date format, Please try again!")
            continue