# -*- coding: utf-8 -*-
"""
Prints the years since an FMI observation station has begun operation.

Description:
    This script is only a test for a planned version that would read in station
    information from a file and allow users to get the operational ages of any
    observation station in the FMI network. Currently, the user should specify
    the desired station at the start of the script as input and the age is
    written to the screen as output.

Note:
    All of the stations in this test version of the script are in Helsinki, so
    "Helsinki" has been removed from the station name for simplicity.

Limitations:
    This code will not work if the station is not in list of station names.

Usage:
    ./station_ages.py

Author:
    Henrikki Tenkanen - 19.9.2017

Modified by:
    None


"""

# A list of night-time (00-08), day-time (08-16) and evening (16-24) temperatures for April 2013 
# measured in Helsinki Malmi Airport
temperatures = [-5.4, 1.0, -1.3, -4.8, 3.9, 0.1, -4.4, 4.0, -2.2, -3.9, 4.4,
                -2.5, -4.6, 5.1, 2.1, -2.4, 1.9, -3.3, -4.8, 1.0, -0.8, -2.8,
                -0.1, -4.7, -5.6, 2.6, -2.7, -4.6, 3.4, -0.4, -0.9, 3.1, 2.4,
                1.6, 4.2, 3.5, 2.6, 3.1, 2.2, 1.8, 3.3, 1.6, 1.5, 4.7, 4.0,
                3.6, 4.9, 4.8, 5.3, 5.6, 4.1, 3.7, 7.6, 6.9, 5.1, 6.4, 3.8,
                4.0, 8.6, 4.1, 1.4, 8.9, 3.0, 1.6, 8.5, 4.7, 6.6, 8.1, 4.5,
                4.8, 11.3, 4.7, 5.2, 11.5, 6.2, 2.9, 4.3, 2.8, 2.8, 6.3, 2.6,
                -0.0, 7.3, 3.4, 4.7, 9.3, 6.4, 5.4, 7.6, 5.2]

# Task 1 - Create empty lists for different temperature classes
# i.e. freezing, cold, slippery, comfortable, warmish, warm
# -------------------------------------------------------------

# Add your code here.


# Task 2 - Iterate over temperatures and add temperatures to different temperature classes
# as defined below:
#  1. Cold --> temperatures below -2 degrees (Celsius)
#  2. Slippery --> temperatures between -2 and +2 degrees (Celsius)
#  3. Comfortable --> temperatures between +2 and +15 degrees (Celsius)
#  4. Warm --> temperatures above +15 degrees (Celsius)
# ------------------------------------------------------------------------------------------

# Add your code here. 


# Task 3 - Questions - Print the answers
# --------------------------------------

# 1. How many times was it slippery during the sudy period?

slippery_times = XXX
print("In April 2013 it was slippery ", slippery_times, "times.")

# 2. How many times was it warmish?
warm_times = XXX
print("In April 2013 it was warmish ", warm_times, "times.")

# 3. How many times was it cold?
cold_times = XXX
print("In April 2013 it was cold ", cold_times, "times.")



# Task 3 - EXTRA (optional)
# --------------------------

# Data values in the 'temperatures' list are grouped in a way that three values always comprise
# a single day. I.e. 
# The first value in the list is temperature for night-time (00-08) at day 1, 
# the second for day-time (08-16) at day 1, 
# and the third for evening (16-24) temperatures at day 1,
# whereas the fourth value is temperature for night-time (00-08) on the next day (day 2), etc.

# 1. Create empty lists for night, day, and evening temperatures

# Add your code here

# 2. Iterate over the temperature values and add the temperatures to corresponding lists

# Add your code here

# 3. What was the mean temperature during the daytime in April 2013?

# Add your code here that answers to the question
                                                         
                                                         