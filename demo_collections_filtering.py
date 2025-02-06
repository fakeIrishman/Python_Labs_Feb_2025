#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: How to copy and optionally filter soruce collection
# to a dest collection using different methods
"""
   Docstring:
"""

students = ['euler','jorge','aram','elizabeth','jeremy','erik','javonn','kirill','aram','euler']


wee_names = []

for  name in students:
    if len(name)<=5:
        wee_names.append(name.upper())
print (f"1.Short names = {wee_names}")


def filter_names(name):
    if len(name) <= 5:
        return True
    else:
        return False


wee_names = []

for name in students:
    if filter_names(name):
        wee_names.append(name.upper())


print (f"2.Short names = {wee_names}")


wee_names = list(filter (filter_names, students))

print(f"3.Short names = {wee_names}")

wee_names = list(filter (lambda name:len(name) <= 5, students))

wee_names = list(filter (filter_names, students))
print(f"4.Short names = {wee_names}")



wee_names = [ name.upper() for  name in students if len(name) <= 5 ] # List comprehension

print(f"5.Short names = {wee_names}")


wee_names = [ (name.upper(), len(name)) for  name in students if len(name) <= 5 ] # List comprehension

print(f"5.1.Short names = {wee_names}")

wee_names = {name.upper(): len(name) for  name in students if len(name) <= 5} # Dictionary comprehension - removes duplicates

print(f"5.2.Short names = {wee_names}")


wee_names = {name.upper() for  name in students if len(name) <= 5} # Set comprehension - removes dupliclates

print(f"5.3.Short names = {wee_names}")