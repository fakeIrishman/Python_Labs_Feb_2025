#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: Demo how to match and substitute a pattern with a replacement string
"""
   Docstring:
"""

import re

#Sample line from /etc/passwd
line = "root:x:0:0: The super user:/root:/bin/ksh"

# I want to modify the string but it's immutable

re.sub(r"[Ss]uper [Uu]ser", r"Administrator", line) # returns a modified string
(line,num) = re.subn(r"ksh", r"bash", line)

print (f"MOdified line:= {line} with {num} changes")