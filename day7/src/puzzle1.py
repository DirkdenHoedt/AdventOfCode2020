#!/bin/env python3


def puzzle1():
    tree = {}
    acceptedBags = ['shiny gold']
    foundNew = True
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
        while foundNew == True:
            foundNew = False
            for rootBag in tree:
                for bag in tree[rootBag]:
                    if bag in acceptedBags and rootBag not in acceptedBags:
                        acceptedBags.append(rootBag)
                        foundNew = True
    print(tree)
    print(acceptedBags[1:])
    print(len(acceptedBags[1:]))

if __name__ == "__main__":
    puzzle1()
