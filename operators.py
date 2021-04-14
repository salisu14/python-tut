#!/usr/bin/env python3


# Arithmetic
# +, -, *, /, //, %, **

#x = 42 
#y = 24

#z = x // y

#print(f'x is {x}, y is {y} and z is {z}')


# comparison operators
# <, >, <=, >=, !=, ==

# Logical operators
# and, or, not

# Identity op
# is, is not

people = ('Muhammad', 23, 4.5, [6, 'six'])
persons = ('Muhammad', 23, 4.5, [6, 'six'])

x = 10
y = 10

#print(persons is people)

#print(x is y)

print(id(people))
print(id(persons))

print(people is not persons)


# Membership op
# in, not in

#people = ('Muhammad', 23, 4.5, [6, 'six'])
#persons = ('Muhammad', 23, 4.5, [6, 'six'])

#p = 'Ibrahim'

#print(p not in people)

# Bitwise operators
# & and, | or, ^ Xor, << left shift, >> right shift
x = 0x0a
y = 0x02

z = x >> y

p = 0b01001101

#print(f'(hex) x is {x:02x}, y is {y:02x}, z is {z:02x}')
#print(f'(bin) x is {x:08b}, y is {y:08b}, z is {z:04b}')
#print(f'(bin) p is {p:02X} (oct) {p:03o}')
