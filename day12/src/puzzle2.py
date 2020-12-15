#!/bin/env python3

def puzzle2():
    with open('input.txt', 'r') as input:
        x = 0
        y = 0
        xw = 10
        yw = 1

        for line in input:
            print(x, y, xw, yw)
            line = line.rstrip()
            if line[0] == 'N':
                yw += int(line[1:])
            if line[0] == 'S':
                yw -= int(line[1:])
            if line[0] == 'E':
                xw += int(line[1:])
            if line[0] == 'W':
                xw -= int(line[1:])
            if line[0] == 'L':
                d = int(line[1:])
                if d == 90:
                    temp = yw
                    yw = xw
                    xw = -temp
                if d == 180:
                    xw = -xw
                    yw = -yw
                if d == 270:
                    temp = xw
                    xw = yw
                    yw = -temp
            if line[0] == 'R':
                d = int(line[1:])
                if d == 90:
                    temp = xw
                    xw = yw
                    yw = -temp
                if d == 180:
                    xw = -xw
                    yw = -yw
                if d == 270:
                    temp = yw
                    yw = xw
                    xw = -temp
            if line[0] == 'F':
                d = int(line[1:])
                x += d * xw
                y += d * yw
                
    print("Manhattan distance: {}".format(abs(x) + abs(y)))

if __name__ == "__main__":
    puzzle2()