#!/usr/bin/env python38


members = ['Muhammad', 'Salisu', 'Ali']
with open('files/members.txt', 'w') as file:
    for m in members:
        file.write(m + "\n")

#print(file.closed)

family = []
with open('files/members.txt') as outfile:
    for f in outfile:
        f = f.replace('\n', '')
        family.append(f)

print(family)