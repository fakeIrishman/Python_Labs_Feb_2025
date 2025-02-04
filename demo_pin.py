#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: This script will simulate a high street bank ATM PIN machine
"""
   Docstring:
"""


master_pin = "0123"
pin = None

# Loop whilst PIN is incorrect

while pin != master_pin:
    pin = input ("Enter PIN: ")
    if pin == master_pin:
        print ("Valid PIN")
    else:
        print ("Invalid PIN")
print ("Done")