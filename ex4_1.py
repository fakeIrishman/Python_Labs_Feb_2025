#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: 
"""
   Docstring:
"""


Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'


print ("-" * len(Belgium) + "...")
items = Belgium.split(',')
print (":".join(items))
print (int(items[1])+int(items[3]))
print ("-" * len(Belgium) + "...")