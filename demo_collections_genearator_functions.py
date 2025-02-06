#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: 
"""
   Docstring:
"""
from operator import truediv


def get_numbers():

    numbers = []
    for x in range (0,10):
        numbers.append(x)
    return numbers


def generate_numbers():

    numbers = []
    for x in range (0,10):
        yield x



for z in generate_numbers():
    print(z)



gen = generate_numbers()

while True:
   num = next(gen, -1)
   if num != -1:
       print (num)
   else:
       break


gen = generate_numbers()

num1 = next(gen)
num2 = next(gen)
num3 = next(gen)

print (num1,num2,num3)