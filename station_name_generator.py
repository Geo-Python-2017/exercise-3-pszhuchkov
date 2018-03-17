# -*- coding: utf-8 -*-
"""
The script generates a list containing filenames that will be processed.

Author: Pavel Zhuchkov

Date: 17.03.2018
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
