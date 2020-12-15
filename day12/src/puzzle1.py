#!/bin/env python3

def puzzle1():
    with open('input.txt', 'r') as input:
        x = 0
        y = 0
        d = 90
        for line in input:
            line = line.rstrip()
            if line[0] == 'N':
                y += int(line[1:])
            if line[0] == 'S':
                y -= int(line[1:])
            if line[0] == 'E':
                x += int(line[1:])
            if line[0] == 'W':
                x -= int(line[1:])
            if line[0] == 'L':
                d -= int(line[1:])
                d = d % 360
            if line[0] == 'R':
                d += int(line[1:])
                d = d % 360
            if line[0] == 'F':
                if d == 90:
                    x += int(line[1:])
                elif d == 180:
                    y -= int(line[1:])
                elif d == 270:
                    x -= int(line[1:])
                elif d == 0:
                    y += int(line[1:])
    print("Manhattan distance: {}".format(abs(x) + abs(y)))
                

if __name__ == "__main__":
    puzzle1()
