#! /usr/bin/env python3
# Author: kdenisen
# Versionn: 1.0
# Description: F1

import math

no_laps = input ("Number of laps: ")

no_laps= int(no_laps)
fuel_consumption = 2.25
fuel_req = no_laps * fuel_consumption

print ("The minimum fuel requirement for", str(no_laps),"laps is",str(fuel_req),"kg.")



