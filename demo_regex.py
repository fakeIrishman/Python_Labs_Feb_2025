#! /usr/bin/env python3
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

for line in fh_in:
   # example of string testing
   # if line.startswith("Y") and line.rstrip("\n").endswith("n") and "town" in line:
   # m = re.search(r"^the",line) # match lines starting with "the"
   # m = re.search(r"ing$", line)  # match lines ending with "ing"
   # m = re.search(r"^ring$", line) # match lines matching "ring"
   # m = re.search(r"^.ing$", line)  # match lines of 4 characters ending  with "ing"
   # m = re.search(r"^.{19}$", line)  # match lines of exactly 19 characters
   # m = re.search(r"^[adr]ing$", line)  # match lines with [adr] followed by 'ing'
   # m = re.search(r"^[A-Z]", line)  # match lines starting with capital
   # m = re.search(r"[aeiou][aeiou][aeiou]", line)  # match lines with 3 consecutive vowels
   # m = re.search(r"[0-9][0-9]", line)  # match lines with 2 consecutive digits
   # m = re.search(r"\.", line)  # match lines with a DOT
   # m = re.search(r"[.]", line)  # match lines with a DOT -- different escape technique
   # m = re.search(r"^[A-Z].*[A-Z]$", line)  # match lines which start and end with capital
   # m = re.search(r"^[A-Z].{4}[A-Z]$", line)  # match lines of 4 characters which start and end with capital
   # m = re.match(r"[A-Z].{4}[A-Z]$", line)  # MATCH automatically matches lines starting with .... - use search instead
   # m = re.fullmatch(r"^[A-Z].{4}[A-Z]\n$", line) # match ENTIRE LINE including HIDDEN characters!
   # m = re.search(r"^(.)(.).\2\1$", line ) # match 5-letter palindromes
   # m = re.search(r"([A-Z]).*\1$", line) # match lines which start and end with same capital
   m = re.search(r"([A-Z]).*\1$", line, flags =re.IGNORECASE) # match lines which start and end with same capital

   if m:
        print(f"Matched {m.group()} on {line.rstrip()} at {m.start()} - {m.end()}, " 
              f"Groupings = {m.groups()}, Group 1 = {m.group(1)}")
