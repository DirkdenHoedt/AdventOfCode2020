#!/bin/env python3


def puzzle1():
    sid = []
    with open('input.txt', 'r') as input:
        for line in input:
            minr = 0
            maxr = 127
            minc = 0
            maxc = 8
            if line[0] == 'F':
                maxr -= 64
            else:
                minr += 64
            if line[1] == 'F':
                maxr -= 32
            else:
                minr += 32
            if line[2] == 'F':
                maxr -= 16
            else:
                minr += 16
            if line[3] == 'F':
                maxr -= 8
            else:
                minr += 8
            if line[4] == 'F':
                maxr -= 4
            else:
                minr += 4
            if line[5] == 'F':
                maxr -= 2
            else:
                minr += 2
            if line[6] == 'F':
                maxr -= 1
            else:
                minr += 1
            if line[7] == 'L':
                maxc -= 4
            else:
                minc += 4
            if line[8] == 'L':
                maxc -= 2
            else:
                minc += 2
            if line[9] == 'L':
                maxc -= 1
            else:
                minc += 1
            # print(maxr * 8 + maxc)
            # print(minr * 8 + minc)
            sid.append(minr * 8 + minc)
    print(max(sid))

if __name__ == "__main__":
    puzzle1()
