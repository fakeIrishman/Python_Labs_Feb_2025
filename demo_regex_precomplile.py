#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: 
"""
   Docstring:
"""#! /usr/bin/env python3
# Author: kdenisen
# Version:
# Description:
"""
   Docstring:
"""


#Open file handle for reading int TEXT mode
import re
fh_in = open(r"c:\labs\words", mode="rt")

#ITERATED throught file handle one line at a time

reobj = re.compile(r"([A-Z]).*\1$") # match lines which start and end with same capital

for line in fh_in:

   m = reobj.search(line)

   if m:
        print(line, end ="")


