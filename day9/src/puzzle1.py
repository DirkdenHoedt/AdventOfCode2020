#!/bin/env python3

def puzzle1():
    preamble = []
    with open('input.txt', 'r') as input:
        for line in input:
            if len(preamble) < 25:
                preamble.append(int(line))
                continue
            searchNumber = int(line)
            found = False
            for i in preamble:
                for j in preamble:
                    if (i + j) == searchNumber and i != j:
                        preamble.append(searchNumber)
                        preamble.pop(0)
                        found = True
                        break
                if found:
                    break
            if not found:
                print(searchNumber)
                break
                        

if __name__ == "__main__":
    puzzle1()
