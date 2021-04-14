#!/usr/bin/env python3


average = 0

score  = int(input('Enter first score: '))
score += int(input('Enter second score: '))
score += int(input('Enter third score: '))

average = score / 3.0

average = round(average, 2)

print(f'Total Score: {score}')
print(f'Average Score: {average}')

