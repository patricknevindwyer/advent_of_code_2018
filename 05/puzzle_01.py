#!/usr/bin/python3

import sys

def read_polymer(filename):
    with open(filename, "r") as file:
        return file.read()


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
    reduced = react(polymer)
    print("polymer(%d) reduced(%d)" % (len(polymer), len(reduced)))
        