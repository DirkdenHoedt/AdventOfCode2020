#!/bin/env python3


def puzzle1():
    acc = 0
    pc = 0
    executedInstr = set()
    instr = []
    with open('input.txt', 'r') as input:
        for line in input:
            line = line.split(' ')
            instr.append((line[0], int(line[1])))
    while True:
        if pc not in executedInstr:
            executedInstr.add(pc)
        else:
            break
        if instr[pc][0] == 'acc':
            acc += instr[pc][1]
            pc += 1
        if instr[pc][0] == 'nop':
            pc += 1
        if instr[pc][0] == 'jmp':
            pc += instr[pc][1]
    
    print(acc)

if __name__ == "__main__":
    puzzle1()
