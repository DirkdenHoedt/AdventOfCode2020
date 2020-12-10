#!/bin/env python3

def puzzle2():
    jolts = []
    helper = []
    with open('input.txt', 'r') as input:
        for line in input:
            jolts.append(int(line))
            helper.append(0)
    jolts.append(0)
    jolts.append(max(jolts) + 3)
    helper.append(0)
    helper.append(0)
    jolts.sort()
    helper[-1] = 1
    helper[-2] = 1
    helper[-3] = 1
    for i in range(len(jolts) - 4, -1, -1):
        if jolts[i + 3] - jolts[i] == 3:
            helper[i] += helper[i + 3]
        if jolts[i + 2] - jolts[i] <= 2:
            helper[i] += helper[i + 2]
        if jolts[i + 1] - jolts[i] <= 3:
            helper[i] += helper[i + 1]
    print(helper[0])

if __name__ == "__main__":
    puzzle2()