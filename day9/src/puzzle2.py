#!/bin/env python3

def puzzle2():
    numbers = []
    with open('input.txt', 'r') as input:
        for line in input:
            numbers.append(int(line))
        
        numberLen = len(numbers)
        for i in range(numberLen):
            cont = 0
            for j in range(i, numberLen):
                cont += numbers[j]
                if cont == 167829540 and numbers[j] != cont:
                    # Found the number
                    minN = min(numbers[i:j])
                    maxN = max(numbers[i:j])
                    print("{} + {} = {}".format(minN, maxN, minN + maxN))

                if cont > 167829540:
                    break
            

if __name__ == "__main__":
    puzzle2()