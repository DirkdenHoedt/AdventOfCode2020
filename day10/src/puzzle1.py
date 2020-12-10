#!/bin/env python3

def puzzle1():
    jolts = []
    jolt = 0
    oneStep = 0
    threeStep = 0
    with open('input.txt', 'r') as input:
        for line in input:
            jolts.append(int(line))
    jolts.sort()    
    for j in jolts:
        if j - jolt == 1:
            # print("found 1")
            oneStep += 1
            jolt += 1
        elif j - jolt == 3:
            # print("found 3")
            threeStep += 1
            jolt += 3
        else:
            print("Not found")
            print(jolts)
            return
    threeStep += 1
    print(oneStep)
    print(threeStep)
    print("{} * {} = {}".format(oneStep, threeStep, oneStep * threeStep))            

if __name__ == "__main__":
    puzzle1()
