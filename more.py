#!/usr/bin/env python3

import threading

from datetime import date
from datetime import time
from datetime import datetime

# for i in range(65, 91):
#     print(f'{chr(i)} = {i}')


# letters = ['A', 'B', 'C']

# for l in letters:
#     print(f'{l} = {ord(l)}')


# alpha = [x for x in range(65, 91)]

# for a in alpha:
#     print(f'{a} - {chr(a)}')



def gfg():
    print('Welcome to timer')


timer = threading.Timer(10000.0, gfg)
timer.start()

print('.', end='')

print("Cancelling timer\n")
timer.cancel()

print('Exit\n')



try:
    date_str = input('Enter birth date (MM/DD/YYYY): ')
    birthdate = datetime.strptime(date_str, "%m/%d/%Y")
    print("Date of birth:", birthdate)
    print(birthdate.strftime("Date of birth details: %a, %d %B %Y"))
except ValueError as ve:
    print('Invalid date format, please use %m/%d/%Y date format')
