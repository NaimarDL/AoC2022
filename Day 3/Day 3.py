# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:07:04 2022

Advent of Code 2022
Day 3

@author: NaimarDL
"""

EXAMPLE = "example.txt"
INPUT = "input.txt"

def charScore(char):
    if char.islower(): return ord(char)-96          #lowercase's score goes from 1 to 26
    else: return ord(char)-38                       #uppercase's score goes from 27 to 52

with open(INPUT) as file:
    text = file.read().split("\n")
    
    score = 0
    for item in text:                               #looking for the same char in both halves of each string
        for char in item[:len(item)//2]:
            if char in item[len(item)//2:]:
                score+=charScore(char)
                break
            
    print("Part 1: "+str(score))
    
    score2 = 0
    for i in range(0, len(text), 3):                        #looking for the same char in each three lines
        for char in text[i]:
            if char in text[i+1] and char in text[i+2]:
                score2+=charScore(char)
                break
    print("Part 2: "+str(score2))
    