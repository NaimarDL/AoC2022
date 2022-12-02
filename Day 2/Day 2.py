# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:46:52 2022

Advent of Code 2022
Day 2

@author: NaimarDL
"""
def myScore(result, shape):
    if result == 0: return numVal(shape) + 3                          #draw
    elif result == -1 or result == 2: return numVal(shape) + 6        #win
    elif result == -2 or result == 1: return numVal(shape) + 0        #lose
    
def myShape(result, oShape):
    if result == 0: return lose(oShape)
    elif result == 3: return oShape
    elif result == 6: return win(oShape)
    
def myScore2(result, shape):
    return numVal(shape)+result

def lose(oShape):
    if oShape == "A": return "C"
    elif oShape == "B": return "A"
    elif oShape == "C": return "B"
    
def win(oShape):
    if oShape == "A": return "B"
    elif oShape == "B": return "C"
    elif oShape == "C": return "A"
    
def numVal(char):
    if char == "A" or char == "X": return 1
    elif char == "B" or char == "Y": return 2
    elif char == "C" or char == "Z": return 3
    
def numRes(char):
    if char == "X": return 0                                            #lose
    elif char == "Y": return 3                                          #draw
    elif char == "Z": return 6                                          #win

EXAMPLE = "example.txt"
INPUT = "input.txt"

with open(INPUT) as file:
    text = file.read().strip().split("\n")
    text = [tuple(item.split(" ")) for item in text]
    
    score = 0
    for item in text:
        result = numVal(item[0])-numVal(item[1])
        score += myScore(result, item[1])
    
    print("Part 1: "+str(score))
    
    score2 = 0
    for item in text:
        score2 += myScore2(numRes(item[1]), myShape(numRes(item[1]), item[0]))
    print("Part 2: "+str(score2))
    