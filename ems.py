#!/usr/bin/env python38

# import date and time 
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


def get_birth_date():
    while True:
        birth_date_str = input("Enter date of birth(dd/mm/yyyy):\t\t")
        try:
            birth_date = datetime.strptime(birth_date_str, "%d/%m/%Y")
            return birth_date
        except ValueError:
            print("Invalid date format, Please try again!")
            continue

def get_service_date():
    while True:
        appointment_date_str = input("Enter date of first appointment (dd/mm/yyyy): ")
        try:
            appointment_date = datetime.strptime(appointment_date_str, "%d/%m/%Y")
            return appointment_date
        except ValueError:
            print("Invalid date format, Please try again!")
            continue

def main():
    print('Employee Management System')
    print()

    while True:
        # get date of birth
        dob = get_birth_date()
        current_date = date.today()
        
        # remove the time portion from dob
        date_of_birth = date(dob.year, dob.month, dob.day)

        # calculate employee's age
        year = timedelta(days=365)
        age = (current_date - date_of_birth).days // year.days

        # test if employee is greater than or equal to 60 years
        if age >= 60:
            print(f'You are {age} years old.')
            print('You are due for retirement.')
        else:
            # get date of first appointment
            dof = get_service_date()

            # remove the time portion from dob
            date_in_service = date(dof.year, dof.month, dof.day)

            # calculate total years in service
            service_years = (current_date - date_in_service).days // year.days

            if service_years >= 35:
                print('You are due for retirement.')
            else:

                print(f'You have worked for {service_years} years')
                print(f'And you will retire in the next {35 - service_years} years.')
                print()
        
        print()

        ans = input("Do you wish to continue? (y/n): ")
        if ans.lower() == 'y' or ans.lower() == "yes":
            continue
        else:
            break


if __name__ == '__main__':
    main()