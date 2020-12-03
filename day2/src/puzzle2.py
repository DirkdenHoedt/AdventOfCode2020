#!/bin/env python3
rules = []

def puzzle2():
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
        one = rule[3][rule[0] - 1]
        two = rule[3][rule[1] - 1]
        if one == rule[2] and two != rule[2]:
            valid += 1
        if one != rule[2] and two == rule[2]:
            valid += 1
    
    print(valid)
            
if __name__ == "__main__":
    puzzle2()
