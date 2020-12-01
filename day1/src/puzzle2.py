#!/bin/env python3
numbers = []

def puzzle2():
    # Read in all the numbers
    with open('input.txt', 'r') as input:
        for line in input:
            numbers.append(int(line))

    # Compare all the numbers
    for x in numbers:
        for y in numbers:
            for z in numbers:
                if(x + y + z == 2020):
                    print('{} + {} + {} = {}'.format(x, y, z, x+y+z))
                    print('{} * {} * {} = {}'.format(x, y, z, x*y*z))
                    return
            
if __name__ == "__main__":
    puzzle2()
