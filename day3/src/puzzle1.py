#!/bin/env python3
maze = []
trees = 0

def puzzle1():
    global maze, trees
    # Read in all the rules
    with open('input.txt', 'r') as input:
        for line in input:
            row = []
            for c in line:
                row.append(c)
            maze.append(row)

    i = 0
    j = 0
    x = len(maze[0]) - 1
    y = len(maze) - 1
    while j <= y:
        if maze[j][i] == '#':
            trees += 1
        i += 3
        j += 1
        i = i % x
    
    print(trees)
            
if __name__ == "__main__":
    puzzle1()
