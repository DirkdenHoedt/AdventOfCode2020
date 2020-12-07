#!/bin/env python3


def puzzle2():
    yesCount = 0
    groupCount = 0
    yesAnswers = {}
    with open('input.txt', 'r') as input:
        for line in input:
            if line == "\n":
                # print(yesAnswers)
                # print(groupCount)
                for val in yesAnswers:
                    if yesAnswers[val] == groupCount:
                        yesCount += 1
                yesAnswers = {}
                groupCount = 0
                continue
            if line[-1:] == "\n":
                line = line[:-1]
            
            for x in line:
                try:
                    yesAnswers[x] += 1
                except KeyError as e:
                    yesAnswers[x] = 1
            groupCount += 1
    # print(yesAnswers)
    for val in yesAnswers:
        if yesAnswers[val] == groupCount:
            yesCount += 1
    yesAnswers = {}
    groupCount = 0
    print(yesCount)

if __name__ == "__main__":
    puzzle2()