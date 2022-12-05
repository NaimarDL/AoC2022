# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 13:33:17 2022

Advent of Code 2022
Day 4

@author: NaimarDL
"""

EXAMPLE = "example.txt"
INPUT = "input.txt"

def contain(item):
    if item[0][0] <= item[1][0] and item[0][1] >= item[1][1]: return True
    elif item[1][0] <= item[0][0] and item[1][1] >= item[0][1]: return True
    return False

def overlap(item):
    if item[0][0] <= item[1][0] and item[0][1] >= item[1][0]: return True
    elif item[0][0] <= item[1][1] and item[0][1] >= item[1][1]: return True
    elif item[1][0] <= item[0][0] and item[1][1] >= item[0][0]: return True
    elif item[1][0] <= item[0][1] and item[1][1] >= item[0][1]: return True
    return False

with open(INPUT) as file:
    text = file.read().split("\n")
    text = [list(list(int(item) for item in tup.split("-")) for tup in tup.split(",")) for tup in text]
    contains = 0
    overlaps = 0
    for item in text:
        if contain(item): 
            contains+=1
            overlaps+=1
        elif overlap(item):
            overlaps+=1
    
    print(contains)
    print(overlaps)