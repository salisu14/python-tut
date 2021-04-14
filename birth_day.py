#!/usr/bin/env python3

from datetime import datetime



def get_birth_date():
    while True:
        dob = input('Enter your birth date (dd/mm/yyyy): ')
        try:
            birth_date = datetime.strptime(dob, '%d/%m/%Y')
            return birth_date
        except ValueError:
            print('Invalid date format. Please try again.')
            continue
    #return birth_date

def main():
    dob = get_birth_date()

    print(dob.strftime("Your birth date is: %A, %d %B %Y"))

if __name__ == '__main__': 
    main()
