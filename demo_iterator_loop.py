#! /usr/bin/env python3
# Author: kdenisen
# Version: 
# Description: 
"""
   Docstring:
"""

films = ['snatch','pulp fiction', 'idiocracy','titanic']


for film in films:
    print (film)




for (idx,film) in enumerate(films, start = 0):
    print(film.title(), end="\n")
    films[idx] = film.title()

print (films)
