#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: Demo of HOWTO define, name and call a user function
# with optional parameters and optionally return a value
"""
   Docstring:
"""

def say_hello(greeting, recepient):
    message = greeting + " " + recepient
    print (message)

say_hello("hello", "my friends")