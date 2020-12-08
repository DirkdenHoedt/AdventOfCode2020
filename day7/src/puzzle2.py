#!/bin/env python3
tree = {}

def findBagAmount(bagName):
    global tree
    rootBag = tree[bagName]
    bagCount = 0
    for bag in rootBag:
        bagCount += rootBag[bag] + (rootBag[bag] * findBagAmount(bag))
    return bagCount

def puzzle2():
    global tree
    bagQueue = ['shiny gold']
    totalBags = 0
    with open('input.txt', 'r') as input:
        for line in input:
            if line[-1:] == "\n":
                line = line[:-1]
            bags = line.split(',')
            partName = bags[0].split(' ')
            name = partName[0] + ' ' + partName[1]
            tree[name] = {}
            if partName[4] == 'no':
                continue
            else:
                tree[name][partName[5] + ' ' + partName[6]] = int(partName[4])
            if len(bags) > 1:
                # print(bags)
                for bag in bags[1:]:
                    bag = bag[1:].split(' ')
                    tree[name][bag[1] + ' ' + bag[2]] = int(bag[0])
    print(findBagAmount('shiny gold'))

if __name__ == "__main__":
    puzzle2()