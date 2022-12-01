# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 17:43:31 2022

Advent of Code 2022
Day 1

@author: NaimarDL
"""

PATH = 'C:/Users/Utente/Desktop/Advent 2022/Day 1/'
TEST = "test.txt"
INPUT = "input.txt"

with open(PATH+INPUT) as file:
    calories = []
    elf = []
    for text_line in file:
        if text_line == "\n":
            calories.append(elf)
            elf = []
        else: elf.append(int(text_line.strip()))
        
    most = 0
    for item in calories:
        cal = sum(item)
        if cal > most: most = cal
    
    print("Part 1: "+str(most))
    