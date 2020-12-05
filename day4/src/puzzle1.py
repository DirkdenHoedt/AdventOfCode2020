#!/bin/env python3
# passport = []
# valid = 0

def puzzle1():
    entries = set()
    allowed1 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    valid = 0
    # Read in all the rules
    with open('input.txt', 'r') as input:
        for line in input:
            if line == "\n":
                # print(entries)
                if len(allowed1 & entries) == 7:
                    valid += 1
                entries = set()
            else:
                keyval = line.split(' ')
                for i in keyval:
                    (key, _) = i.split(':')
                    entries.add(key)
    if len(allowed1 & entries) == 7:
        valid += 1
    print(valid)

# def process():
#     # print("p")
#     global passport, valid
#     entries = []
#     allowed1 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
#     allowed2 = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
#     for p in passport:
#         ps = p.split(' ')
#         for i in ps:
#             # print (i)
#             (idp, _) = i.split(':')
#             entries.append(idp)
#     if (len(allowed1 & set(entries)) == 7) or (len(allowed2 & set(entries)) == 8):
#         valid += 1
#     passport = []

            
if __name__ == "__main__":
    puzzle1()
