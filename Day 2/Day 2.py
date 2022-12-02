# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:46:52 2022

Advent of Code 2022
Day 2

@author: NaimarDL
"""

EXAMPLE = "example.txt"
INPUT = "input.txt"

with open(EXAMPLE) as file:
    text = file.read().strip().split("\n")
    print(text)
    text = [tuple(item.split(" ")) for item in text]
    print(text)
    
    