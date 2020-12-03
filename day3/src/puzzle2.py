#!/bin/env python3
maze = []

def puzzle2(a, b):
    global maze
    trees = 0
    

    i = 0
    j = 0
    x = len(maze[0]) - 1
    y = len(maze) - 1
    while j <= y:
        if maze[j][i] == '#':
            trees += 1
        i += a
        j += b
        i = i % x
    
    return trees
            
if __name__ == "__main__":
    # Read in all the rules
    with open('input.txt', 'r') as input:
        for line in input:
            row = []
            for c in line:
                row.append(c)
            maze.append(row)

    result = 1
    result *= puzzle2(1, 1)
    result *= puzzle2(3, 1)
    result *= puzzle2(5, 1)
    result *= puzzle2(7, 1)
    result *= puzzle2(1, 2)
    print(result)
