#!/usr/bin/env python3

# types of files
# 1. text file (html, text)
# 2. binary file (images, vedios, etc)

# text files
# open - opening file for either reading or writing
# mode - 'r', 'w', 'a', 'b', 
# methods - read, readline, readlines, write, close
# properties - closed

infile = open('files/test.txt', 'w')
infile.write('Welcome to files manipulation in python\n')
infile.write('Wrinting to files in python is very easy.\n')
infile.close()

#print(infile.closed)


outfile = open('files/test.txt', 'r')
#print(outfile.read())
contents = outfile.readlines()
outfile.close()

print(type(contents))
print(contents)
