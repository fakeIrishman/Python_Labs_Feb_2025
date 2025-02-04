#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: Demo how to split and rejoin strings using the .split() and .join() methods
"""
   Docstring:
"""

line = "root:x:0:0:The Super User:/root:/bin/ksh"

# I want to modify this string but strings are immutable

fields = line.split(":") # Return a LIST - LISTS are mutable

fields[4] = "The Admin"
fields[6] = "/bin/bash"

line =  ":".join(fields)

print (line)