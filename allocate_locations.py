# -*- coding: utf-8 -*-
"""
Prints the names of FMI weather stations separated into four geographical zones in Finland (NW, NE, SW, SE) based on
the coordinates of the stations. Additionally, prints the information about the how equally distributed the station
network is in Finland. 

Description:
    This script is only a test for a planned version that would read in all operative station data 
    from a file and allow users to analyze also analyze weather observations from those stations. 

Note:
    The data only includes stations that were operative 70 years ago (started before 1948).   

Limitations:
    -

Usage:
    ./allocate_locations.py

Author:
    Henrikki Tenkanen - 19.9.2017

Modified by:
    None
"""

# Station names
stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 
            'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho', 
            'Juuka Niemelä', 'Jyväskylä airport', 'Kaarina Yltöinen', 'Kauhava airfield', 
            'Kemi Kemi-Tornio airport', 'Kotka Rankki', 'Kouvola Anjala', 
            'Kouvola Utti airport', 'Kuopio Maaninka', 'Kuusamo airport', 
            'Lieksa Lampela', 'Mustasaari Valassaaret', 'Parainen Utö', 'Pori airport', 
            'Rovaniemi Apukka', 'Salo Kärkkä', 'Savonlinna Punkaharju Laukansaari', 
            'Seinäjoki Pelmaa', 'Siikajoki Ruukki', 'Siilinjärvi Kuopio airport', 
            'Tohmajärvi Kemie', 'Utsjoki Nuorgam', 'Vaala Pelso', 'Vaasa airport', 
            'Vesanto Sonkari', 'Vieremä Kaarakkala', 'Vihti Maasoja', 'Ylitornio Meltosjärvi']

# Latitude coordinates of Weather stations  
lat = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4,
       60.39, 63.12, 65.78, 60.38, 60.7, 60.9, 63.14, 65.99,
       63.32, 63.44, 59.78, 61.47, 66.58, 60.37, 61.8, 62.94,
       64.68, 63.01, 62.24, 70.08, 64.5, 63.06, 62.92, 63.84,
       60.42, 66.53]

# Longitude coordinates of Weather stations 
lon = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67, 
       22.55, 23.04, 24.58, 26.96, 26.81, 26.95, 27.31, 29.23, 
       30.05, 21.07, 21.37, 21.79, 26.01, 23.11, 29.32, 22.49, 
       25.09, 27.8, 30.35, 27.9, 26.42, 21.75, 26.42, 27.22, 
       24.4, 24.65]

# 


