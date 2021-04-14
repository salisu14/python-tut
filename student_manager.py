#!/usr/bin/env python3

from os import path

FILENAME = 'students.txt'

def write_student(students_list):
    if path.exists(FILENAME) and path.isfile(FILENAME):
        with open(FILENAME, 'w') as file:
            for student in students_list:
                file.write(student + "\n")

def get_students():
    students = []
    if path.exists(FILENAME) and path.isfile(FILENAME):
        with open(FILENAME, 'r') as file:
            for f in file:
                f = f.replace("\n", "")
                students.append(f)
        return students

# display the main menu
def display_menu():
    print()
    print('\tCOMMAND MENU ')
    print('*' * 30)
    print('list - Display all students')
    print('add  - Add a student')
    print('del  - Delete a student')
    print('help - Display this menu')
    print('exit - Exit application')
    print()

# show all students
def display_all(students_list):
    '''A function to show all students'''
    print('\tLIST OF STUDENTS')
    print('-' * 30)
    if len(students_list):
        i = 0
        for student in students_list:
            print(f'{str(i+1)}. {student}')
            i += 1
        print()
    else:
        print('No students found!')

# add a new student
def add_student(students_list):
    '''A function to add new student'''
    print()
    print('\tADD NEW STUDENT')
    print('-' * 30)
    name = input('Enter full name: ')
    if len(name):
        students_list.append(name)
        write_student(students_list)
        print(f'{name} was added successfully!')
        print()
    else:
        print('Name is required.')
        print()

# delete a student
def delete(students_list):
    '''A function to delete a student'''
    print()
    print('\tDELETE A STUDENT')
    print('-' * 30)
    number = int(input('Enter number: '))
    if number < 1 or number > len(students_list):
        print('No such student')
    else:
        name = students_list.pop(number - 1)
        write_student(students_list)
        print(f'{name} was deleted successfully!')
        print()


def main():
    print('-' * 70)
    print('\t\t\tStudent Management Software - v1.0'.upper())
    print('-' * 70)
    
    students_list = get_students()

    display_menu()

    while True:
        command = input('Enter command: ').lower()
        if command == 'list' or command == 'ls':
            display_all(students_list)
        elif command == 'add':
            add_student(students_list)
        elif command == 'del':
            delete(students_list)
        elif command == 'help':
            display_menu()
        elif command == 'exit':
            break
        else:
            print('Invalid command. Please enter again!')
            print()

    print('Bye!')
        
if __name__ == '__main__': main()