#!/bin/env python3

def oneRound(wMap):
    nIter = []
    width = len(wMap)
    height = len(wMap[0])
    for i in range(width):
        row = []
        for j in range(height):
            if wMap[i][j] == ".":
                row.append('.')
            elif wMap[i][j] == "L":
                emptySeats = 0
                if i > 0:
                    if wMap[i-1][j] != "#":
                        emptySeats += 1
                    if j > 0:
                        if wMap[i-1][j-1] != "#":
                            emptySeats += 1
                    else:
                        emptySeats += 1
                    if j < height - 1:
                        if wMap[i-1][j+1] != "#":
                            emptySeats += 1
                    else:
                        emptySeats += 1
                else:
                    emptySeats += 3
                if i < width - 1:
                    if wMap[i+1][j] != "#":
                        emptySeats += 1
                    if j > 0:
                        if wMap[i+1][j-1] != "#":
                            emptySeats += 1
                    else:
                        emptySeats += 1
                    if j < height - 1:
                        if wMap[i+1][j+1] != "#":
                            emptySeats += 1
                    else:
                        emptySeats += 1
                else:
                    emptySeats += 3
                if j > 0:
                    if wMap[i][j-1] != '#':
                        emptySeats += 1
                else:
                    emptySeats += 1
                if j < height - 1:
                    if wMap[i][j+1] != '#':
                        emptySeats += 1
                else:
                    emptySeats += 1
                
                if emptySeats == 8:
                    row.append('#')
                else:
                    row.append('L')
            elif wMap[i][j] == "#":
                filledSeats = 0
                if i > 0:
                    if wMap[i-1][j] == "#":
                        filledSeats += 1
                    if j > 0:
                        if wMap[i-1][j-1] == "#":
                            filledSeats += 1
                    if j < height - 1:
                        if wMap[i-1][j+1] == "#":
                            filledSeats += 1
                if i < width - 1:
                    if wMap[i+1][j] == "#":
                        filledSeats += 1
                    if j > 0:
                        if wMap[i+1][j-1] == "#":
                            filledSeats += 1
                    if j < height - 1:
                        if wMap[i+1][j+1] == "#":
                            filledSeats += 1
                if j > 0:
                    if wMap[i][j-1] == "#":
                        filledSeats += 1
                if j < height - 1:
                    if wMap[i][j+1] == "#":
                        filledSeats += 1
                
                if filledSeats >= 4:
                    row.append('L')
                else:
                    row.append('#')
        nIter.append(row)
    return nIter

def compLists(l1, l2):
    if len(l2) == 0:
        return False
    w = len(l1)
    h = len(l1[0])
    for i in range(w):
        for j in range(h):
            if l1[i][j] != l2[i][j]:
                return False
    return True

def puzzle1():
    wMap1 = []
    wMap2 = []
    with open('input.txt', 'r') as input:
        for line in input:
            if line[-1:] == "\n":
                line = line[:-1]
            row = []
            for c in line:
                row.append(c)
            wMap1.append(row)
    
    while compLists(wMap1, wMap2) == False:
        wMap2 = wMap1
        wMap1 = oneRound(wMap2)
    
        for row in wMap1:
            for r in row:
                print(r, end="")
            print()
        print()
    
    counter = 0
    for row in wMap1:
        for r in row:
            if r == '#':
                counter += 1
    print("Seats occupied: {}".format(counter))


if __name__ == "__main__":
    puzzle1()
