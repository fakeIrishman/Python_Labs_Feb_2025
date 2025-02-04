#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: This script will simulate a high street bank ATM PIN machine
"""
   Docstring:
"""


master_pin = "0123"
pin = None
attempts = 0

# Loop whilst PIN is incorrect

while pin != master_pin and attempts < 3:
    pin = input ("Enter PIN: ")
    if pin == master_pin:
        print ("Valid PIN")
    else:
        print ("Invalid PIN")
        attempts += 1
print ("Done")