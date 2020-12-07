#!/bin/env python3


def puzzle1():
    yesCount = 0
    yesAnswers = {}
    with open('input.txt', 'r') as input:
        for line in input:
            if line == "\n":
                # print(yesAnswers)
                yesCount += len(yesAnswers)
                yesAnswers = {}
                continue
            if line[-1:] == "\n":
                line = line[:-1]
            
            for x in line:
                yesAnswers[x] = True
    # print(yesAnswers)
    yesCount += len(yesAnswers)
    yesAnswers = {}
    print(yesCount)

if __name__ == "__main__":
    puzzle1()
