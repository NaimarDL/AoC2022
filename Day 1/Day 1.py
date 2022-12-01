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
    for text_line in file:                              #calories is a list of each elf inventory
        if text_line == "\n":
            calories.append(elf)
            elf = []
        else: elf.append(int(text_line.strip()))
    calories.append(elf)                                #accounting for the last line in the file
    
    total = [sum(item) for item in calories]            #total is a list of each elf total calories carried
    total = sorted(total, reverse=True)
    
    print("Part 1: "+str(total[0]))                     #Part 1 asks the top calories carried
    print("Part 2: "+str(total[0]+total[1]+total[2]))   #Part 2 asks the sum of the top three
    