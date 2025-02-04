#! /usr/bin/env python3
# Author: kdenisen
# Versionn: 1.0
# Description: ex2_3
from  math import pi, tan, cos

g = 9.81
v0 = input("initial velocity (m/s): ")
deg = input ("elevation angle in degrees: ")
x = input ("horizontal distance travelled(m): ")
y0 = input ("height of the barrel(m): ")

# convert input to float
v0 = float(v0)
x = float(x)
deg = float(deg)
y0 = float (y0)

# convert degrees to radians
theta = deg * (pi/180)

# height of the projectile

y = y0 + x*tan(theta) - (g * x**2) / (2 * (v0 * cos(theta))**2)

print ("At barrel height of",str(y0),"after horizontal distance of",str(x), ", an elevation of",str(deg),"degrees, and an initial velocity of",str(v0),"m/s the heght of the projectile will be",str(y),"m")

