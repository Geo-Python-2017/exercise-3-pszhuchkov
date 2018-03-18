# -*- coding: utf-8 -*-
"""
The script outputs stars and flag of USA.

Usage: ./make_flag.py

Author: Pavel Zhuchkov - 18.03.2018
"""
# Set variables
star = '*'
text = ''
line = '-'
flag = ''

# Output stars
print('Stars')
for i in range(3):
    for j in range(7):
        text += star
    text += '\n'
print(text)
    
print('\nFlag')

# Output flag
for i in range(5):
    if i < 3:
        for j in range(19):
            if j < 7:
                flag += star
            else:
                flag += line
        flag += '\n'
    else:
        for k in range(19):
            flag += line
        flag += '\n'
print(flag)
    