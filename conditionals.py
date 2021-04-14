#!/usr/bin/env python3

# comparison operators
# <, >, <=, >=, !=, ==

x = 24
y = 24

#print(x > y)
#print(y == x)


# Logical operators
# and, or, not

#print(x >= 25 or x < 20)

if x <= 5:
    print('{x} is greater than five')
else:
    print(f'{x} is not less than or equal to five')

# print(__name__)

#score = int(input('Please enter a score: '))

# if...elif ...else


# if score >= 90 and score <= 100:
#     grade = 'A'
# elif score >= 80 and score <= 89:
#     grade = 'B'
# elif score >= 70 and score <= 79:
#     grade = 'C'
# elif score >= 60 and score <= 69:
#     grade = 'D'
# elif score >= 50 and score <= 59:
#     grade = 'E'
# else:
#     grade = 'F'

# print(f'Your grade is {grade}')


hungry = False

x = 'Go home ' if hungry else 'Stay and learn'

print(x)
