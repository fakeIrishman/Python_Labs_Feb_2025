#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description:  gen.py
"""
   Docstring:
"""

def frange(start, stop=None , step = 0.25):
    if stop is None:
        stop=start
        current = 0.0
    else:
         current = float(start)

    while current < stop:
        yield current
        current +=step

for num in frange(3.142, 12):
    print(f"{num:05.2f}")


one = list(frange(0,3.5,0.25))
two = list(frange(3.5))
if one ==two:
    print("defaults worked")
else:
    print("oops! defaults didn't work")
    print(f"one: {one}")
    print(f"two: {two}")

print (frange(1,2))