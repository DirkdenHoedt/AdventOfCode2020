#!/bin/env python3

def puzzle2():
    instr = []
    instrLen = 0
    with open('input.txt', 'r') as input:
        for line in input:
            line = line.split(' ')
            instr.append((line[0], int(line[1])))
    instrLen = len(instr)
    
    for i in range(len(instr)):
        if instr[i][0] == 'acc':
            continue

        local = instr.copy()
        if local[i][0] == 'jmp':
            local[i] = ('nop', local[i][1])
        elif local[i][0] == 'nop':
            local[i] = ('jmp', local[i][1])
        # print(local)
        
        acc = 0
        pc = 0
        executedInstr = set()
        while True:
            if pc not in executedInstr:
                executedInstr.add(pc)
            else:
                break
            if pc >= instrLen:
                print(acc)
                return
            if local[pc][0] == 'acc':
                acc += local[pc][1]
                pc += 1
            elif local[pc][0] == 'nop':
                pc += 1
            elif local[pc][0] == 'jmp':
                pc += local[pc][1]

if __name__ == "__main__":
    puzzle2()