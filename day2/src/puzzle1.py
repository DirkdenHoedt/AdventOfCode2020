#!/bin/env python3
rules = []

def puzzle1():
    valid = 0
    # Read in all the rules
    with open('input.txt', 'r') as input:
        for line in input:
            (minmax, letter, seq) = line.split(' ')
            letter = letter[:-1]
            # seq = seq[:-1]
            (minC, maxC) = minmax.split("-")
            rules.append((int(minC), int(maxC), letter, seq))

    # Check every rule for correctness
    for rule in rules:
        letterCount = rule[3].count(rule[2])
        if letterCount >= rule[0] and letterCount <= rule[1]:
            valid += 1
    
    print(valid)
            
if __name__ == "__main__":
    puzzle1()
