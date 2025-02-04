#! /usr/bin/env python3
# Author: kdenisen
# Versionn: 1.0
# Description: F1

import math

no_laps = input ("Number of laps: ")

no_laps= int(no_laps)
fuel_consumption = 2.25
min_fuel_req = no_laps * fuel_consumption
fuel_req = min_fuel_req * 1.5 # extra 50% for contingency

print ("The minimum fuel requirement for", str(no_laps),"laps is",str(fuel_req),"kg.")

# qualifying lap time with 5 kg of fuel on board

qual_lap_time = 80.45

# each 10 kg of fuel increases the lap time by 0.35 sec

lap_time_increase = 0.35 * fuel_req/10
first_lap_time = qual_lap_time + lap_time_increase

print ("The lap time for the first lap with",str(fuel_req),"kg",\
       "of fuel on board will be", str(first_lap_time))

