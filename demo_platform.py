#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: This script will demo how to check which platform is your script running on
"""
   Docstring:
"""
import sys
import os

if sys.platform == "win32":
    home_dir = os.environ["HOMEPATH"]
else:
    home_dir = os.environ["HOME"]

print(home_dir)