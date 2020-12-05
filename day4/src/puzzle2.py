#!/bin/env python3
def puzzle2():
    entries = set()
    allowed1 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    # Read in all the rules
    with open('input.txt', 'r') as input:
        l = 0
        for line in input:
            l += 1
            if line == "\n":
                # print(entries)
                if len(allowed1 & entries) == 7:
                    valid += 1
                entries = set()
            else:
                keyval = line.split(' ')
                for i in keyval:
                    (key, val) = i.split(':')
                    if val[-1:] == '\n':
                        val = val[:-1]
                    if key == "byr":
                        val = int(val)
                        if val >= 1920 and val <= 2002:
                            entries.add(key)
                        else:
                            print('{} byr'.format(l))
                    if key == "iyr":
                        val = int(val)
                        if val >= 2010 and val <= 2020:
                            entries.add(key)
                        else:
                            print('{} iyr'.format(l))
                    if key == "eyr":
                        val = int(val)
                        if val >= 2020 and val <= 2030:
                            entries.add(key)
                        else:
                            print('{} eyr'.format(l))
                    if key == "hgt":
                        if val[-2:] == "cm":
                            val = int(val[:-2])
                            if val >= 150 and val <= 193:
                                entries.add(key)
                            else:
                                print('{} hgt'.format(l))
                        elif val[-2:] == "in":
                            val = int(val[:-2])
                            if val >= 59 and val <= 76:
                                entries.add(key)
                            else:
                                print('{} hgt'.format(l))
                    if key == "hcl":
                        if val[0] == '#':
                            val = val[1:]
                            check = 0
                            for c in val:
                                if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']:
                                    check += 1
                            if check == 6:
                                entries.add(key)
                            else:
                                print('{} hcl'.format(l))
                    if key == "ecl":
                        if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                            entries.add(key)
                        else:
                            print('{} ecl'.format(l))
                    if key == "pid":
                        check = 0
                        for c in val:
                            if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                                check += 1
                        if check == 9:
                            entries.add(key)
                        else:
                            print('{} pid'.format(l))
    if len(allowed1 & entries) == 7:
        valid += 1
    print(valid)
            
if __name__ == "__main__":
    puzzle2()
