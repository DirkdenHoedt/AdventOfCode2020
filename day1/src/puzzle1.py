#!/bin/env python3
numbers = []

def puzzle1():
    # Read in all the numbers
    with open('input.txt', 'r') as input:
        for line in input:
            numbers.append(int(line))

    # Compare all the numbers
    for x in numbers:
        for y in numbers:
            if(x + y == 2020):
                print('{} + {} = {}'.format(x, y, x+y))
                print('{} * {} = {}'.format(x, y, x*y))
                return
            
if __name__ == "__main__":
    puzzle1()
