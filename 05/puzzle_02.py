#!/usr/bin/python3

import sys

def read_polymer(filename):
    with open(filename, "r") as file:
        return file.read()


def reagents(polymer):
    return list(set(polymer.lower()))


def remove_reagent(polymer, reagent):
    rest = []
    for c in polymer:
        if c.lower() != reagent:
            rest.append(c)
    return "".join(rest)
        

def react(polymer):
    idx = 0
    
    while idx < (len(polymer) - 1):
        head = polymer[idx]
        rest = polymer[idx + 1]
        
        # do we have a leading reaction?
        if head != rest and head.lower() == rest.lower():
            polymer = polymer[:idx] + polymer[idx + 2:]
            idx -= 1
            if idx < 0:
                idx = 0
        else:
            idx += 1
    return polymer


if __name__ == "__main__":
    polymer = read_polymer(sys.argv[-1])
    
    smallest = len(polymer)
    for reagent in reagents(polymer):
        r_poly = remove_reagent(polymer, reagent)
        rr_poly = react(r_poly)
        print("%s :: %d" % (reagent, len(rr_poly)))
        if len(rr_poly) < smallest:
            smallest = len(rr_poly)
    print("polymer(%d) smallest(%d)" % (len(polymer), smallest))
        