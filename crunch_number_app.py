#!/usr/bin/env python3

import random

def crunch_numbers(data):
    total = 0
    for number in data:
        total += number
    
    average = round(total / len(data))
    median_index = len(data) // 2
    median = data[median_index]
    minimum = min(data)
    maximum = max(data)
    dups = get_duplicates(data)

    print(f'Average = {average}, Median = {median}, Min = {minimum}, ' +
           f'Max = {maximum}, Dups = {dups}')

def get_duplicates(data):
    dups = []
    for i in range(51):
        count = data.count(i)
        if count >= 2:
            dups.append(i)
    return dups

def main():
    print('\t\tNumber Crunch Application')
    print('-' * 55) 
    fixed_tuple = (0,5,10,15,20,25,30,35,40,45,50)
    random_list = [0] * 11
    for i in range(len(random_list)):
        random_list[i] = random.randint(0, 50)
    random_list.sort()

    print(f"TUPLE DATA: {fixed_tuple}")
    crunch_numbers(fixed_tuple)
    print()
    print(f"RANDOM DATA: {random_list}")
    crunch_numbers(random_list)

if __name__ == '__main__': main()