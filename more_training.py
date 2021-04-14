#!/usr/bin/env python38

import os
import getpass
from os import path
from datetime import datetime
import uuid
# name, rename, listdir, mkdir, rmdir, unlink, getcwd, getlogin()

# print(os.name)
# # print(os.listdir())

# dir_list = os.listdir()

# for dir in dir_list:
#     print(dir)
    

# # os.mkdir('Horrible')\

# print(os.getcwd())

# print(os.getlogin())


# # my_pass = getpass.getpass("Enter your password: ")

# # print(my_pass)

# user = getpass.getuser()
# print("System user: ", user)

# # os.rmdir('Horrible')

# print(path.exists('score.py'))


# print(os.environ)

#print(datetime.fromtimestamp(path.getmtime('score.py')))

#print(datetime.fromtimestamp(path.getctime('score.py')))

#print(path.realpath('score.py'))

file = path.realpath('score.py')

_dir, f = path.split(file)

print(_dir)
print(f)

ext = f.split('.')[-1]
print(ext)

body = str(uuid.uuid4())

body = body + "." + ext

newname = body
print(newname)



