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



