#!/usr/bin/env python38

# import date and time 
from datetime import date
from datetime import time
from datetime import datetime


def get_birth_date():
    while True:
        birth_date_str = input("Enter date of birth(dd/mm/yyyy): ")
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
            return birth_date
        except ValueError:
            print("Invalid date format, Please try again!")
            continue

def main():
    date_of_birth = get_birth_date()
    print(date_of_birth.strftime("Your date of birth is: %A %B %d, %Y"))


if __name__ == '__main__':
    main()