#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: 
"""
   Docstring:
"""

for line in open ('messier.txt', encoding = 'latin_1'):
    if not line :
        break
    if not line.startswith("M")   :
        break
    messier_num = line[0:6].rstrip()
    common_name = line [6:40]