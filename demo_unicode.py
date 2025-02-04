#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: Demo how to display the entire Unicode set
"""
   Docstring:
"""

for pos in range(0,65536):
    try:
        print (pos,chr(pos), end = " ")
        if pos % 16 == 0:
            print ()
    except UnicodeError:
        print(" ", end = " " )

