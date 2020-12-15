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
                emptySeats = 8
                # Left
                for x in range(1, j + 1):
                    if wMap[i][j - x] == '#':
                        emptySeats -= 1
                        break
                # Right
                for x in range(1, height - j):
                    if wMap[i][j + x] == '#':
                        emptySeats -= 1
                        break

                # Up
                for y in range(1, i + 1):
                    if wMap[i - y][j] == '#':
                        emptySeats -= 1
                        break
                # Down
                for y in range(1, width - i):
                    if wMap[i + y][j] == '#':
                        emptySeats -= 1
                        break

                # Left up
                for k in range(1, min(i + 1, j + 1)):
                    if wMap[i - k][j - k] == '#':
                        emptySeats -= 1
                        break

                # Left down
                for k in range(1, min(i + 1, height - j)):
                    if wMap[i - k][j + k] == '#':
                        emptySeats -= 1
                        break

                # Right up
                for k in range(1, min(width - i, j + 1)):
                    if wMap[i + k][j - k] == '#':
                        emptySeats -= 1
                        break

                # Right down
                for k in range(1, min(width - i, height - j)):
                    if wMap[i + k][j + k] == '#':
                        emptySeats -= 1
                        break
                
                if emptySeats == 8:
                    row.append('#')
                else:
                    row.append('L')
            elif wMap[i][j] == "#":
                filledSeats = 0
                # Left
                for x in range(1, j + 1):
                    if wMap[i][j - x] == '#':
                        filledSeats += 1
                        break
                # Right
                for x in range(1, height - j):
                    if wMap[i][j + x] == '#':
                        filledSeats += 1
                        break

                # Up
                for y in range(1, i + 1):
                    if wMap[i - y][j] == '#':
                        filledSeats += 1
                        break
                # Down
                for y in range(1, width - i):
                    if wMap[i + y][j] == '#':
                        filledSeats += 1
                        break

                # Left up
                for k in range(1, min(i + 1, j + 1)):
                    if wMap[i - k][j - k] == '#':
                        filledSeats += 1
                        break

                # Left down
                for k in range(1, min(i + 1, height - j)):
                    if wMap[i - k][j + k] == '#':
                        filledSeats += 1
                        break

                # Right up
                for k in range(1, min(width - i, j + 1)):
                    if wMap[i + k][j - k] == '#':
                        filledSeats += 1
                        break

                # Right down
                for k in range(1, min(width - i, height - j)):
                    if wMap[i + k][j + k] == '#':
                        filledSeats += 1
                        break
                
                if filledSeats >= 5:
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

def puzzle2():
    wMap1 = []
    wMap2 = []
    with open('test.txt', 'r') as input:
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
    puzzle2()