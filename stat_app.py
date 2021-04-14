#!/usr/bin/env python3
import random

def crunch_data(data):
    total = 0
    for d in data:
        total += d
    
    average = round(total / len(data))
    median_index = len(data) // 2
    median = data[median_index]
    minimum = min(data)
    maximum = max(data)
    dups = get_duplicates(data)

    print("Average = ", average, end=", ")
    print("Median = ", median, end=", ")
    print("Minimum =", minimum, end=", ")
    print("Maximum =", maximum, end=", ")
    print("Dups = ", dups)
    print()

def get_duplicates(data):
    dups = []
    for i in range(51):
        count = data.count(i)
        if count >= 2:
            dups.append(i)
    return dups

def main():
    my_tuple = (0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50)
    numbers_list = [0] * 11

    for i in range(len(numbers_list)):
        numbers_list[i] = random.randint(0, 50)
    numbers_list.sort()
    
    print('TUPLE DATA: ', my_tuple)
    crunch_data(my_tuple)
    print(f'RANDOM NUMS: ', numbers_list)
    crunch_data(numbers_list)

if __name__ == '__main__': main()