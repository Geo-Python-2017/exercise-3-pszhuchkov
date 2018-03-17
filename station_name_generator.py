# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 13:07:05 2018

@author: Pavel
"""
# Set variables
basename = 'Station'
filenames = []

# Iterate over the number range 0-20
for i in range(21):
    # Create a variable station
    station = basename + '_' + str(i) + '.txt'
    # Fill empty list by created filenames
    filenames.append(station)
# Print output list
print(filenames)
