#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: This is an ULTRA REALISTIC Calculator App with tons of features
"""
   Docstring:
"""
import sys
import basic
import adv

menu = """
       Calculator App
        ---------------
        1. Test Basic
        2. Test Adv
"""

print (menu)
option = input ("Choose 1 or 2 :")
if option ==1:
    print(f"100 + 50 + 25 + 12.5 = {add(100,50,25,12.5)}")
    print(f"100 * 50 * 25 * 12.5 = {mul(100,50,25,12.5)}")
elif option == 2:
    print(f"Modulus of 100 by 45 = {mod(100,45)}")
    print(f"Square root of 25 = {sqrt(25)}")
else:
    print("Invalid option")

sys.exit()