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
    #split all the inventories
    calories = file.read().split("\n\n")           
    #create tuples from the inventories            
    calories = [tuple(map(int, elf.split())) for elf in calories]   
    
    #total is the list of the sum of each inventory sorted from highest to lowest
    total = sorted([sum(item) for item in calories], reverse=True)
    
    #Part 1 asks the highest calories carried
    print("Part 1: "+str(total[0]))                     
    #Part 2 asks the sum of the highest three        
    print("Part 2: "+str(sum(total[:3])))                           
    