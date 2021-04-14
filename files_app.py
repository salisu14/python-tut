#!/usr/bin/env python3

import os

members = ['Muhammad Salisu', 'Hassan Garba', 'Haruna Abubakar']

with open('family.txt', 'w') as infile:
    for m in members:
        infile.write(m + '\n')

with open('family.txt', 'r') as infile:
    print(infile.read())
